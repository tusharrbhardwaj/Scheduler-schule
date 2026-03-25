'''
fetchData.py fetches all the relative data from ./data's json files.
'''

import json #to read and extract data from json files in ./data


class Data:
    def __init__(self):
        pass


    def readProfJson(self):
        '''
        readProfJson fetches data from ./data directory.
        try :
            It specifically fetches from prof_avalaiblity.json and returns data in an organized method as:
                prof_ids : for easiar access to professors in available_profs
                p_availablity : dictonary conatiaint p_ids as key and their availablity time as nested dictonary
        except:
            throws an error stating Error loading file prof_availablity.json
        
        '''
        try:
            with open('./data/prof_availablity.json') as available_profs_data:
                available_profs = json.load(available_profs_data)
                p_ids = [prof["id"] for prof in available_profs["professors"]]
                p_availablity= {prof["id"] : prof["availability"] for prof in available_profs["professors"]}
                
            return p_ids, p_availablity
        
        except Exception as e:
            print(f"Error loading file prof_availablity.json: {e}")
            
            return None, None
    
    
    
    def readRooms(self):
        '''
        readRooms fetches data from ./data/rooms.json.
        
        try:
            It returns the room with their respective capacities in a dictonary format which are stored as "r_capacity".
        except:
            throws an error stating Error loading file rooms.json
        '''
        try:
            with open('./data/rooms.json') as available_rooms_data:
                available_rooms = json.load(available_rooms_data)
                r_capacity = {room["id"] : room["capacity"] for room in available_rooms["rooms"]}
                
                return r_capacity
            
        except Exception as e:
            print(f"Error loading file rooms.json: {e}")
            
            return {}
        
    
    
    def readStudents(self):
        '''
        readStudents fetches data from ./data/std_grouping.json.
        try:
            returns:
                groups : dictonary with group_id as key and its value as list of the students that are in the group
                group_size : returns the group_id with its size for proper assignemnt of room and time.
        except:
            throws an error stating Error loading file std_grouping.json
        '''
        try:
            with open('./data/std_grouping.json') as group_data: 
                groups_raw = json.load(group_data)
                '''
                groups creates a dictonary using dictonary and list comprehension.
                the key in this dictonary is the group_id and then using list comprehension it stores all the student_ids that have the same group in a list and assign that list as the
                value pair for that key.
                '''
                groups = { 
                        student["group"] : [std["id"] 
                                            for std in groups_raw["students"] 
                                            if std["group"] == student["group"]]
                        for student in groups_raw["students"]
                        }
                
                '''
                group_size also uses list comprehension with addition to .items() method of dictonary which returns tuples of key-value pair.
                '''
                group_size = {grp[0] : len(grp[1]) for grp in groups.items()}
                
                return groups,group_size
        
        except Exception as e:
            print(f"Error loading file std_grouping.json: {e}")
            
            return None, None
            
    '''
    for an imaginary situation with demo data where classes are assigned to professors
    '''        
    def readClassConstrains(self):
        '''
        readClassConstrains fetches data from ./data/constraints.js
        try:
            returns:
                classes : list of classes with class_data in dictonary format
        except:
            throws an error stating Error loading file constraints.js
        '''
        try:
            with open('./data/constraints.json') as class_constraints: 
                classes_raw = json.load(class_constraints)
                classes = [class_data for class_data in classes_raw["classes"]]
                
                return classes
                       
        
        except Exception as e:
            print(f"Error loading file constraints.js: {e}")
            
            return None, None
        
    '''
    Timeslot.json containts timeslots that could be create of average 3 hours each
    '''    
    def readTimeslots(self):
        '''
       readTimeslots fetches data from ./data/timeslot.json
        try:
            returns:
                timeslots : returns dictonary with data in form of dictonary
        except:
            throws an error stating Error loading file timeslot.json
        '''
        try:
            with open('./data/timeslot.json') as alltimeslots:
                timeslots = json.load(alltimeslots)

                return timeslots                   
                       
        
        except Exception as e:
            print(f"Error loading file timeslot.json: {e}")
            
            return None, None
        
        