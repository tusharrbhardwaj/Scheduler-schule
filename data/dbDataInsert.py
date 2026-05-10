'''
This file helps user to insert data into tables of the database connected.
'''

import csv
import pyinputplus as pyip
from data import connection
from utils import success, error, info

try:
    conn = connection()
    cur = conn.cursor()
except Exception as e:
    error("Connectivity Error : ", e)


class Insert:
    
    def __init__(self,table_name):
        self.table_name = table_name
        self.table_headers = []
        self.csv_data = []
        self.serialvariable = ''
    
    def read_csv(self):
        try:
            
            with open(f"dataInput/{self.table_name}.csv") as csvfile:
                data = csv.reader(csvfile)
                self.csv_data = [row for row in data if row] #if row condition removes blank row from csv to avoid conflict with db
            success("Fetched data from csv file to upload to DB")
        
        except Exception as e:
            error("Could not read data from file \n", e)
                
            
    def upload_data(self):
        try:
            
            query = "SELECT column_name FROM information_schema.columns WHERE table_name = %s"
            cur.execute(query,(self.table_name,))
            columns = cur.fetchall()
            for eachheader in columns:
                self.table_headers.append(eachheader[0])
            
            self.read_csv()
            
            #Normalizing data headers to compare and validate data
            csv_headers = [col.strip().lower() for col in self.csv_data[0]]
            db_headers = [col.strip().lower() for col in self.table_headers]
            
            
            if csv_headers == db_headers:
                success("Data validation Successfull")
                
                placeholders = ', '.join(['%s'] * len(self.table_headers))
                column_str = ', '.join(self.table_headers)
                query = f"INSERT INTO {self.table_name} ({column_str}) VALUES ({placeholders}) ON CONFLICT DO NOTHING"
                
                confirmation = pyip.inputYesNo("Are you sure to make your changes permanent? : ")
                
                if confirmation == 'yes':
                    cur.executemany(query, self.csv_data[1:])
                    conn.commit()
                    success("Data Insterted Successfully")
                    info(f"{len(self.csv_data[1:])} rows processed")
                    
                else:
                    conn.rollback()
                    error("Data Insertion Aborted")
                 
            else:
                error("Data validation Unsuccessfull")
                info("CSV:", csv_headers)
                info("DB :", db_headers)
        
        except Exception as e:
            error("Some error occured while uploading data to DB \n", e)   
        
class Update:
    def __init__(self):
        pass
    
    def update_greedyschedule(self, scheduled):
        try:
            table = "greedy_schedule"
            
            cur.execute(f"TRUNCATE TABLE {table};")
            
            query = f"INSERT INTO {table} (class_id, cid, module, group_id, timeslot_id, room_no, prof_id) values (%s, %s, %s, %s, %s, %s, %s)"
            cur.executemany(query, scheduled)
            conn.commit()
            success(f"Greedy Scheduled Saved Successfully!\n")
            info(f"{len(scheduled)} rows inserted")
            
        except Exception as e:
            error("Greedy Schedule could not be updated.\n", e)
            
    def update_graphschedule(self, graph_schedule):
        try:
            table = "graph_schedule"
            
            cur.execute(f"TRUNCATE TABLE {table};")
            
            query = f"INSERT INTO {table} (class_id, timeslot_id, prof_id, cid, group_id, total_students) values (%s, %s, %s, %s, %s, %s)"
            cur.executemany(query, graph_schedule)
            conn.commit()
            success(f"Graph Scheduled Saved Successfully!\n")
            info(f"{len(graph_schedule)} rows inserted")
            
        except Exception as e:
            error("Graph Schedule could not be updated.\n", e)
        
    def update_dp_result(self, allocation):
        try:
            table = 'dp_result'

            cur.execute(f"TRUNCATE TABLE {table}")
            
            query = f"INSERT INTO {table} (class_id, room_no) values (%s, %s)"
            data = [(class_id, room_no) for class_id, room_no in allocation.items()]
            cur.executemany(query, data)
            conn.commit()
            success(f"DP with graph Scheduled Saved Successfully!\n")
            info(f"{len(allocation)} rows inserted")
            
        except Exception as e:
            error("Dp result could not be updated.\n", e)
            

if __name__ == "__main__":
    table_name = input("Enter the name of the table you want to enter data into : ")
    upload = Insert(table_name)
    upload.upload_data()