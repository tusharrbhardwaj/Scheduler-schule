# This file is the greedy algorithm implementation that creates a "decent" schedule instantly
'''
Problem - Statement 
    Sort your list of classes by "Difficulty" (e.g., number of students enrolled). 
    Place them one by one into the first available room and time slot that does not violate a hard constraint.
    
Approach :

'''

import json #to read and extract data from json files in ./data


class Data:
    def __init__(self):
        pass


    def readProfJson(self):
        '''
        readProfJson fetches data from ./data directory.
        It specifically fetches from prof_avalaiblity.json and returns data in an organized method as:
            prof_ids : for easiar access to professors in available_profs
            p_availablity : dictonary conatiaint p_ids as key and their availablity time as nested dictonary
        '''
        with open('./data/prof_availablity.json') as available_profs_data:
            available_profs = json.load(available_profs_data)
            p_ids = [prof["id"] for prof in available_profs["professors"]]
            p_availablity = {prof["id"] : prof["availability"] for prof in available_profs["professors"]}
            
        return p_ids,p_availablity
    
    def readRooms(self):
        '''
        readRooms fetches data from ./data/rooms.json.
        It returns the room with their respective capacities in a dictonary format which are stored as "r_capacity".
        '''
        with open('./data/rooms.json') as available_rooms_data:
            available_rooms = json.load(available_rooms_data)
            r_capacity = {room["id"] : room["capacity"] for room in available_rooms["rooms"]}
            
            return r_capacity
        
    def readStudents(self):
        '''
        readStudents fetches data from ./data/std_grouping.json.
        returns:
            groups : dictonary with group_id as key and its value as list of the students that are in the group
            group_size : returns the group_id with its size for proper assignemnt of room and time.
        '''
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
             
            
        

