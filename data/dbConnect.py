import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connection():  
    try:
        db_url = os.getenv("DB_URL")
        conn = psycopg2.connect(db_url)
        print("Connection to DB Successfull")
        return conn
    
    except Exception as e:
        print("Error Connecting to DB \n", e)
        return None
        

'''
To test this file
'''

# connection()