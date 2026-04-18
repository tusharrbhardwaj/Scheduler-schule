'''
This file helps user to insert data into tables of the database connected.
'''

import csv
import pyinputplus as pyip
from data import connection

conn = connection()
cur = conn.cursor()


class Insert:
    
    def __init__(self,table_name):
        self.table_name = table_name
        self.table_headers = []
        self.csv_data = []
        self.serialvariable = ''
    
    def read_csv(self):
        with open(f"dataInput/{self.table_name}.csv") as csvfile:
            data = csv.reader(csvfile)
            self.csv_data = [row for row in data if row] #if row condition removes blank row from csv to avoid conflict with db
        
        
         
    def upload_data(self):
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
            print("Data validation Successfull")
            
            placeholders = ', '.join(['%s'] * len(self.table_headers))
            column_str = ', '.join(self.table_headers)
            query = f"INSERT INTO {self.table_name} ({column_str}) VALUES ({placeholders}) ON CONFLICT DO NOTHING"
            
            confirmation = pyip.inputYesNo("Are you sure to make your changes permanent? : ")
            if confirmation == 'yes':
                cur.executemany(query, self.csv_data[1:])
                conn.commit()
                print("Data Insterted Successfully")
                print(f"{len(self.csv_data[1:])} rows processed")
                
            else:
                conn.rollback()
                print("Data Insertion Aborted")
           
            
        else:
            print("Data validation Unsuccessfull")
            print("CSV:", csv_headers)
            print("DB :", db_headers)
            
        
        
        
table_name = input("Enter the name of the table you want to enter data into : ")
upload = Insert(table_name)
upload.upload_data()