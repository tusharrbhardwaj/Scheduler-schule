from datetime import time
from data import dbFetch


class Transformation:
    
    def __init__(self):
        self.data = {}
        self.timeslots = {}

        
    def readData(self, name):
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
        
        return transformed_data
    
    def transform_timeslot(self):
        rawdata = self.readData("timeslots")
        i = 1
        for eachrow in rawdata:
            temp ={}
            temp['day'] = eachrow['day']
            temp['start_time'] = eachrow['start_time'].strftime("%H:%M")
            temp['end_time'] = eachrow['end_time'].strftime("%H:%M")
            
            self.data[i] = temp
            i+=1
            
        return self.data
    
    def transform_classrooms(self):
        rawdata = self.readData("classrooms")
        for each in rawdata:
            self.timeslots[each['room_no']] = each['cr_capacity']
            
        return self.timeslots
  
# # name = input("Enter name : ")    
# transform = Transformation()
# # data = transform.transform_timeslot()
# data = transform.transform_classrooms()
# print(data)
    
                
        
        
       
        
    
        
