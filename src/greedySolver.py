# This file is the greedy algorithm implementation that creates a "decent" schedule instantly
'''
Stage 1: The Greedy Baseline (The "Quick Start")
•	The Mission: Implement an algorithm that creates a "decent" schedule instantly.
•	The Logic: Sort your list of classes by "Difficulty" (e.g., number of students enrolled). Place them one by one into the first available room and time slot that does not violate a hard constraint.
•	The Report: Explain why you chose your sorting key. (e.g., "We sorted by number of students because larger classes are harder to fit, so they should be prioritized".)
•	The Result: A partially functional schedule that likely leaves some classes unplaced.
'''

'''
Problem - Statement 
    Sort your list of classes by "Difficulty" (e.g., number of students enrolled). 
    Place them one by one into the first available room and time slot that does not violate a hard constraint.
    
Approach :
    greedily select classes sorted based on descecnding order of class population. 
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
key : (timeslot,room_id)
value : class_id
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
key : (timeslot, prof_id)
value : class_id
'''
booked_prof = {}

'''
unsceduled_classes for any edge case classes where it can not either be scheduled or need be scheduled somewhere else
'''
scheduled_classes = []
unsceduled_classes = []

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
        '''
        greedy_schedule implements a greedy scheduling algorithm to assign classes to available time slots and rooms.

        Approach:
        1. Classes are sorted in descending order based on number of students (larger classes are scheduled first).
        2. For each class, the algorithm iterates through all available time slots and rooms to find the first feasible assignment.
        3. A valid assignment must satisfy:
            - Room capacity is sufficient for the class size
            - Room is not already booked at that time slot
            - Professor is not already assigned to another class at that time slot
        4. If a valid slot is found, the class is scheduled immediately.
        5. If no valid assignment is found, the class is added to the unscheduled list.

        Output:
        - Prints all scheduled classes with their assigned time, room, and wasted capacity
        - Prints list of unscheduled classes (if any)

        Note:
        This is a greedy approach and does not guarantee optimal scheduling.
        It prioritizes fast assignment over minimizing wasted capacity or resolving all conflicts.
    
        '''
        
        # Step 1: Sort classes by number of students (descending order)
        sorted_classes = self.sorting_classes()
        
        # Step 2: Iterate through each class and try to assign it
        for eachclass in sorted_classes:
            assigned = False
            
            # Step 3: Try each timeslot
            for timeslot in timeslots:
                
                # Step 4: Try each room for the current timeslot
                for r_id, capacity in r_capacity.items():
                    
                    # Check 1: Room must have enough capacity
                    # Check 2: Room must be free at this timeslot
                    if (capacity >= eachclass["students"]) and ((timeslot, r_id) not in booked_rooms):
                        
                        # Check 3: Professor must be free at this timeslot
                        if (timeslot, eachclass["professor"]) not in booked_prof:
                            
                            # Assign class to this room and timeslot
                            booked_rooms[(timeslot, r_id)] = eachclass["id"]
                            booked_prof[(timeslot, eachclass["professor"])] = eachclass["id"]
                            
                            # Store scheduled class with wasted capacity info
                            scheduled_classes.append([eachclass["id"], timeslot, r_id, capacity - eachclass["students"]])
                            assigned = True
                            break  # Exit room loop once assigned
                
                # If assigned, stop checking further timeslots
                if assigned:
                    break
            
            # If class could not be assigned to any slot
            if not assigned:
                unsceduled_classes.append(eachclass['id'])
        
        # Step 5: Print scheduled classes        
        for schedule in scheduled_classes:
            print(f"Scheduled {schedule[0]} {schedule[1]} {schedule[2]} Wasted {schedule[3]} seats")    
         
        print("following are the unscheduled classes")   
        for unschedule in unsceduled_classes:
            print(unschedule)
            
    
                    



dsort = Greedy()

soreted = dsort.sorting_classes()

dsort.greedy_schedule()