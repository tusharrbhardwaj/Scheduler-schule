import dbFetch


class Transformation:
    
    def __init__(self):
        pass

        
    def readData(self,name):
        
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
    
    
    # def prof_avail(self,name):
    #     raw_columns, fetched_data = dbFetch.Fetch(name).data()
        
    #     grouped_data = {}
        
    #     for eachrow in fetched_data:
            
    #         if eachrow[] not in grouped_data:
                
    #         else :
    #             avail[eachrow[1]][eachrow[2]] = [eachrow[3], eachrow[4]]
                
                
    #     print(avail)
                
        
        
       
        
    
        
trans = Transformation()

a = trans.readData("classrooms")
# print(a)
# b = trans.prof_avail("prof_availability")

# print(a)
r_capacity = {}
for eachclass in a:
    r_capacity[eachclass["room_id"]] = eachclass["cr_capacity"]

print(r_capacity)