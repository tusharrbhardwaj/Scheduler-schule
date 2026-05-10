from data import connection
from utils import success, error, info


try:
    conn = connection()
    cur = conn.cursor()
except Exception as e:
    error("Connectivity Error : ", e)

class Fetch:
    def __init__(self, table_name):
        self.table_name = table_name
    
    
    def data(self):
        '''
        clear exisiting data from table
        '''
        try:
            query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{self.table_name}'"
            cur.execute(query)
            columns = cur.fetchall()
            cur.execute(f"SELECT * FROM {self.table_name}")
            fetched_data = cur.fetchall()
            success(f"Successfully fetched data from {self.table_name}")
            return columns, fetched_data
        
        except Exception as e:
            error(f"Some Error Ocuured while fetching data from table {self.table_name} : {e}")
            return None, None
    
    def greedyschedule_fetch(self):
        
        try:
            query = f'''
            SELECT 
            gs.class_id,

            p.prof_name,
            pr.programme_name,
            gs.module,
            st.group_name,

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

            JOIN programmes pr
                ON c.cid = pr.cid

            JOIN student_groups st
                ON gs.group_id = st.group_id
    
            JOIN professor p 
                ON c.prof_id = p.prof_id

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
            success("Greedy_Schedule fetched from DB")
            return data
        
        except Exception as e:
            error("Data could not be fetched from greedy_schedule \n", e)
            return None
        
    def graphschedule_fetch(self):
        
        try:
            
            query = f'''
            SELECT 
            gs.class_id,

            p.prof_name,
            pr.programme_name,
            c.module,
            st.group_name,

            t.day,
            t.start_time,
            t.end_time

            FROM graph_schedule gs

            JOIN classes c 
                ON gs.class_id = c.class_id

            JOIN programmes pr
                ON c.cid = pr.cid

            JOIN student_groups st
                ON gs.group_id = st.group_id
    
            JOIN professor p 
                ON c.prof_id = p.prof_id

            JOIN timeslots t 
                ON gs.timeslot_id = t.timeslot_id

        ORDER BY 
            t.day,
            t.start_time;
            '''
            
            cur.execute(query)
            data = cur.fetchall()
            success("Graph_Schedule fetched from DB")
            return data
        
        except Exception as e:
            error("Data could not be fetched from graph_schedule \n", e)
            return None
        
    def dp_fetch(self):
        
        try:
            
            query = f'''
            SELECT 
            gs.class_id,

            p.prof_name,
            pr.programme_name,
            c.module,
            st.group_name,

            t.day,
            t.start_time,
            t.end_time,

            dp.room_no,
            cr.cr_capacity,
            
            c.total_students,
            (cr.cr_capacity - c.total_students) AS wasted_seats
            
            FROM graph_schedule gs

            JOIN classes c 
                ON gs.class_id = c.class_id

            JOIN programmes pr
                ON c.cid = pr.cid

            JOIN student_groups st
                ON gs.group_id = st.group_id
    
            JOIN professor p 
                ON c.prof_id = p.prof_id

            JOIN timeslots t 
                ON gs.timeslot_id = t.timeslot_id
                
            LEFT JOIN dp_result dp
                ON gs.class_id = dp.class_id

            LEFT JOIN classrooms cr
                ON dp.room_no = cr.room_no

        ORDER BY 
            t.day,
            t.start_time;
            '''
            
            cur.execute(query)
            data = cur.fetchall()
            success("Combined Graph + DP Schedule fetched from DB")
            return data
        
        except Exception as e:
            error("Data could not be fetched from dp and graph schedule \n", e)
            return None