#This is main.py for Schedular-Schule which builds master schedule for universities.
'''
Goals :
    1.	No person (student or teacher) is scheduled for two classes at the same time.
    2.	No room is double-booked.
    3.	Every class fits inside its assigned room.
    4.	We don't waste money heating a 500-seat auditorium for a 10-person poetry seminar.
    5.	You have to navigate complex, overlapping constraints. Most importantly, you must handle Student Group Conflicts:
        •	If "Group A" (e.g., Year 1 Computer Science) needs to attend both "Intro to Math" and "Intro to Programming", those two classes cannot overlap.
        •	Even if the professor for Math is different from the professor for Programming, the fact that a student needs both makes the classes "connected".

Stage 0 : Fetch demo data from ./data directory 
Stage 1: Greedy Baseline ---- ./src/greedySolver.py
'''

'''
Stage 0 : fetching data through fetchData.py
'''
from src import fetchData

data = fetchData.Data() #data object for class Data in .src/fetchData.py

#p_ids : list & p_availablity : dictonary 
p_ids, p_availablity = data.readProfJson()

#r_capacity : list
r_capacity = data.readRooms()

#groups : list && group_size : dictonary
groups, group_size = data.readStudents()

#classes : list with data in dictonary format
classes = data.readClassConstrains()

#Grouped_classes : list with data in dictonary fromat for student-group assigmnment to classes
grouped_classes = data.classGroups() 


for grp,size in group_size.items():
    print(f"{grp} : {size}")
