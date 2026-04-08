import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connection():  
    db_url = os.getenv("DB_URL")
    conn = psycopg2.connect(db_url)
    return conn

# def read():
#     conn = connection()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM professor")
    
#     data = cur.fetchall()
#     for i in data:
#         print(i)
    
#     cur.close()
#     conn.close()
    
    
# read()