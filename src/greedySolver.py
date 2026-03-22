# This file is the greedy algorithm implementation that creates a "decent" schedule instantly
'''
Problem - Statement 
    Sort your list of classes by "Difficulty" (e.g., number of students enrolled). 
    Place them one by one into the first available room and time slot that does not violate a hard constraint.
    
Approach :

'''

'''
---------------------------------------------------------------------------------------------
Redundent code to skip main.py in development phase
'''

import fetchData

data = fetchData.Data() #data object for class Data in .src/fetchData.py

#p_ids : list & p_availablity : dictonary 
p_ids, p_availablity = data.readProfJson()

#r_capacity : list
r_capacity = data.readRooms()

#groups : list && group_size : dictonary
groups, group_size = data.readStudents()

#classes : list with data in dictonary format
classes = data.readClassConstrains()

'''
---------------------------------------------------------------------------------------------
'''

'''
booked_rooms is a dictonary which will track the room and its time blockage.
here ---
key : room_id
value : [timeslot, class_id]
'''
booked_rooms = {}

'''
timeslots containts time block, each of 3 hours now which starts from 08:00 in the morning to 20:00 in night.
Henceforth 15:00 being last to be book time since the avergae duration of classes are 3 hours, booking at 15:00 would imply its end at 20:00 (end time of time-block)
'''
timeslots = ["08:00", "11:00", "14:00", "17:00"]

'''
booked_prof is a dictonary which will track the prof and their time blockage.
here ---
key : prof_id
value : [timeslot, class_id]
'''
booked_prof = {}

'''
unsceduled_classes for any edge case classes where it can not either be scheduled or need be scheduled somewhere else
'''
unsceduled_classes = []
eq=[]
neq=[]
class Greedy:
    
    def __init__(self):
        pass
    
    def sorting_classes(self):
        '''
        sorting_classes sorts the classes forn list classes in descending order with respect to number of students in it.
        This will help assigning the larger classes room first so that large room does not get assigned to smaller calsses.
        '''
        classes.sort(key = lambda x: x["students"], reverse=True)

        return classes

    def greedy_schedule(self):
        
        sorted_classes = self.sorting_classes()
        for eachclass in sorted_classes:
            assigned = False
            for timeslot in timeslots:
                for r_id, capacity in r_capacity.items():
                    if int(capacity) >= eachclass["students"] and (timeslot not in booked_rooms[r_id]):
                        booked_rooms[r_id] = [eachclass[timeslot,'id']]
                        assigned = True
                        break
        
            if not assigned:
                unsceduled_classes.append(eachclass['id'])
                
        print(booked_rooms)    
            
    
                    



dsort = Greedy()

soreted = dsort.sorting_classes()

dsort.greedy_schedule()