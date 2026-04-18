import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connection():  
    db_url = os.getenv("DB_URL")
    conn = psycopg2.connect(db_url)
    # print("successfull")  # --- line to debug
    return conn

'''
To test this file
'''

# connection()