import csv

from dbConnect import connection

conn = connection()
cur = conn.cursor()

class Fetch:
    def __init__(self, table_name):
        self.table_name = table_name
    
    
    def data(self):
        query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{self.table_name}'"
        cur.execute(query)
        columns = cur.fetchall()
        cur.execute(f"SELECT * FROM {self.table_name}")
        fetched_data = cur.fetchall()
        return columns, fetched_data
    
    # def joinfetch(self):
    #     query = f'''
            
        
    #         '''


