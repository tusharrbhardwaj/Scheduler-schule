from datetime import time
from data import dbFetch



class Transformation:
    
    def __init__(self):
        self.data = {}
        self.timeslots = {}

        
    def readData(self, name):
        try:
            
            raw_columns, fetched_data = dbFetch.Fetch(name).data()
            
            columns = []
            transformed_data = []
            for each in raw_columns:
                columns.append(each[0])
            
            for eachrow in fetched_data:
                temp = {}
                i = 0
                for eachcolumn in eachrow:
                    temp[columns[i]] = eachcolumn
                    i += 1
                transformed_data.append(temp)
            
            print(f"Successfully transformed data from table {name}.\n")
            return transformed_data
        
        except Exception as e:
            print("Error while Transforming data.\n", e)
            return None
    
    def transform_timeslot(self):
        try:
            
            rawdata = self.readData("timeslots")
            i = 1
            for eachrow in rawdata:
                temp ={}
                temp['day'] = eachrow['day']
                temp['start_time'] = eachrow['start_time'].strftime("%H:%M")
                temp['end_time'] = eachrow['end_time'].strftime("%H:%M")
                
                self.data[i] = temp
                i+=1
            
            print("Timeslots cannot be transformed to usable data.\n")
            return self.data
        
        except Exception as e:
            
            print("Timeslots cannot be transformed to usable data.\n", e)
    
    def transform_classrooms(self):
        try:
            
            rawdata = self.readData("classrooms")
            for each in rawdata:
                self.timeslots[each['room_no']] = each['cr_capacity']
            
            print("Classroom data transformed successfully.\n")    
            return self.timeslots
        
        except Exception as e:
            print("Error occured while transforming classroom data.\n", e)



class Schedule:
    
   
    def __init__(self):
        pass
    
    
    def greedy_schedule():
        
        try:
            
            raw_data = dbFetch.Fetch("greedy_schedule").schedule_fetch()
            data = [("Class_id", "Professor", "Room_no", "Day", "From", "To", "Total_Students", "Room_capacity", "Seats_Wasted")]
            for each in raw_data:
                temp = []
                temp.extend([each[0], each[1], each[2], each[3], each[4].strftime("%H:%M"), each[5].strftime("%H:%M"), each[6], each[7], each[8]])
                data.append(temp)
            print("Greedy Schedule Tranformed.\n")
            return data
        
        except Exception as e:
            print("Scheduled data could not be transformed.\n", e)
            return None
    
    
    
    
# # name = input("Enter name : ")    
# transform = Transformation()
# # data = transform.transform_timeslot()
# data = transform.transform_classrooms()
# print(data)
    
                
        
        
       
        
    
        
