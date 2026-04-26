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
timeslots containts time block, each of 3 hours now which starts from 08:00 in the morning to 20:00 in night.
Henceforth 15:00 being last to be book time since the avergae duration of classes are 3 hours, booking at 15:00 would imply its end at 20:00 (end time of time-block)
'''
# timeslots = ["08:00", "11:00", "14:00", "17:00"]

import datetime



class Greedy:
    
    def __init__(self, classes, timeslots, classrooms, prof_availablity):
        self.classes = classes
        self.timeslots = timeslots
        self.classrooms = classrooms
        self.prof_availablity = prof_availablity
        
        '''
        booked_rooms is a dictonary which will track the room and its time blockage.
        here ---
        key : (timeslot,room_id)
        value : class_id
        '''
        self.booked_rooms = {}
        
        '''
        booked_prof is a dictonary which will track the prof and their time blockage.
        here ---
        key : (timeslot, prof_id)
        value : class_id
        '''
        self.booked_prof = {}
        '''
        
        unsceduled_classes for any edge case classes where it can not either be scheduled or need be scheduled somewhere else
        '''
        self.scheduled_classes = []
        self.unsceduled_classes = []
        
    
    def sorting_classes(self):
        '''
        sorting_classes sorts the classes forn list classes in descending order with respect to number of students in it.
        This will help assigning the larger classes room first so that large room does not get assigned to smaller calsses.
        '''
        self.classes.sort(key = lambda x: x["total_students"], reverse=True)
        return self.classes

    
    def is_prof_available(self, prof_id, timeslot):
        
        prof_slots = self.prof_availablity.get(prof_id, [])
        
        for slot in prof_slots:
            if(slot['day'] == timeslot["day"]
                and slot['start_time'] <= timeslot['start_time']
                and slot['end_time'] >= timeslot['end_time']
                ):
                    return True
            
        return False
    
    
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
        
        #sorting room to ensure small room is occupied first and then it moves to bigger room instead of dictnoary order
        sorted_rooms = sorted(self.classrooms.items(), key=lambda x: x[1])
        
        # Step 2: Iterate through each class and try to assign it
        for eachclass in sorted_classes:
            assigned = False
            
            # Step 3: Try each timeslot
            for timeslot_id, timeslot in self.timeslots.items():
                
                if self.is_prof_available(eachclass["prof_id"], timeslot):
                
                    # Step 4: Try each room for the current timeslot
                    for r_id, capacity in sorted_rooms:
                        
                        # Check 1: Room must have enough capacity
                        # Check 2: Room must be free at this timeslot
                        if (capacity >= eachclass["total_students"]) and ((timeslot_id, r_id) not in self.booked_rooms):
                            
                            # Check 3: Professor must be free at this timeslot
                            if (timeslot_id, eachclass["prof_id"]) not in self.booked_prof:
                                
                                # Assign class to this room and timeslot
                                self.booked_rooms[(timeslot_id, r_id)] = eachclass["class_id"]
                                self.booked_prof[(timeslot_id, eachclass["prof_id"])] = eachclass["class_id"]
                                
                                # Store scheduled class with wasted capacity info
                                self.scheduled_classes.append([eachclass["class_id"], timeslot_id, r_id, eachclass["prof_id"]])
                                assigned = True
                                break  # Exit room loop once assigned
                    
                    # If assigned, stop checking further timeslots
                    if assigned:
                        break
                    
            # If class could not be assigned to any slot
            if not assigned:
                self.unsceduled_classes.append(eachclass['class_id'])

        return self.scheduled_classes, self.unsceduled_classes
        # # Step 5: Print scheduled classes        
        # for schedule in scheduled_classes:
        #     print(f"Scheduled {schedule[0]} {schedule[1]} {schedule[2]} Wasted {schedule[3]} seats")    
         
        # print("following are the unscheduled classes")   
        # for unschedule in unsceduled_classes:
        #     print(unschedule)
            
    
                    



# dsort = Greedy()

# soreted = dsort.sorting_classes()

# dsort.greedy_schedule()