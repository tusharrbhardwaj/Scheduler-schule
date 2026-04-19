from data import connection

conn = connection()
cur = conn.cursor()

class Fetch:
    def __init__(self, table_name):
        self.table_name = table_name
    
    
    def data(self):
        '''
        clear exisiting data from table
        '''
        try:
            
            cur.execute("DELETE FROM greedy_schedule")
            conn.commit()
            
            query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{self.table_name}'"
            cur.execute(query)
            columns = cur.fetchall()
            cur.execute(f"SELECT * FROM {self.table_name}")
            fetched_data = cur.fetchall()
            print(f"Successfully fetched data from {self.table_name}")
            return columns, fetched_data
        
        except Exception as e:
            print(f"Some Error Ocuured while fetching data from table {self.table_name} : {e}")
            return None, None
    
    def schedule_fetch(self):
        
        try:
            
            query = f'''
            SELECT 
                gs.class_id,
                p.prof_name,
                gs.room_no,
                t.day,
                t.start_time,
                t.end_time,
                c.total_students,
                r.cr_capacity,
                (r.cr_capacity - c.total_students) AS wasted_seats

            FROM greedy_schedule gs

            JOIN classes c 
                ON gs.class_id = c.class_id

            JOIN professor p 
                ON gs.prof_id = p.prof_id

            JOIN classrooms r 
                ON gs.room_no = r.room_no

            JOIN timeslots t 
                ON gs.timeslot_id = t.timeslot_id

            ORDER BY 
                t.day,
                t.start_time,
                gs.room_no;
            '''
            
            cur.execute(query)
            data = cur.fetchall()
            print("Greedy_Schedule fetched from DB")
            return data
        
        except Exception as e:
            print("Data could not be uploaded to greedy_schedule \n", e)
            return None