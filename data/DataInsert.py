'''
This file helps user to insert data into tables of the database connected.
'''

import csv

from db_connect import connection

conn = connection()
cur = conn.cursor()


class Insert:
    
    def __init__(self,table_name):
        self.table_name = table_name
        self.data = []
        self.columns = []
        
    
    def visiting_table(self):
        query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{self.table_name}'"
        cur.execute(query)
        response = cur.fetchall()
        for each in response:
            for i in each:
                print(i)
                self.columns.append(i)
        
        
    
    def read_csv(self):
        
        try:
            with open(f"dataInput/{self.table_name}.csv") as filedata:
                reader = csv.reader(filedata)
                next(reader)
                for row in reader:
                    self.data.append(row)
        except Exception as e:
            print(f"Error occured {e}")
            

     
    def insert_data(self):
        self.columns.pop(0)
        column_str = ', '.join(self.columns)
        place_holders = ', '.join(['%s'] * len(self.columns))
        formated_data = [tuple(row) for row in self.data]
        print(formated_data)
        query = f"INSERT INTO {self.table_name} ({column_str}) VALUES ({place_holders})"
        try:
            cur.executemany(query, formated_data)
            print("Data Inserted Successfully")
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(f"Some error occured {e}")
        

        
name = input('Enter The name of the table, you want to enter data into : ')           
        
start = Insert(name)
start.visiting_table()
start.read_csv()
start.insert_data()
cur.close()
conn.close()