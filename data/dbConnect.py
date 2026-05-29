import psycopg2
import os
from dotenv import load_dotenv
from utils import success, error, info


load_dotenv()


def connection():  
    try:
        db_url = os.getenv("DB_URL")
        conn = psycopg2.connect(db_url)
        success("Connection to DB Successfull")
        return conn
    
    except Exception as e:
        error("Error Connecting to DB")
        info(e)
        return None
        

'''
To test this file
'''

# connection()