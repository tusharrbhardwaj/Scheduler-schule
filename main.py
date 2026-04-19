# #This is main.py for Schedular-Schule which builds master schedule for universities.
# '''
# Goals :
#     1.	No person (student or teacher) is scheduled for two classes at the same time.
#     2.	No room is double-booked.
#     3.	Every class fits inside its assigned room.
#     4.	We don't waste money heating a 500-seat auditorium for a 10-person poetry seminar.
#     5.	You have to navigate complex, overlapping constraints. Most importantly, you must handle Student Group Conflicts:
#         •	If "Group A" (e.g., Year 1 Computer Science) needs to attend both "Intro to Math" and "Intro to Programming", those two classes cannot overlap.
#         •	Even if the professor for Math is different from the professor for Programming, the fact that a student needs both makes the classes "connected".

# Stage 0 : Fetch demo data from ./data directory 
# Stage 1: Greedy Baseline ---- ./src/greedySolver.py
# '''

# '''
# Stage 0 : fetching data through fetchData.py
# '''

# # from src import graphEngine

from data import Transformation, Schedule
from src import greedySolver
from data import dbDataInsert

# from src import fetchData

transform = Transformation()
classes = transform.readData("classes")
timeslots = transform.transform_timeslot()
classrooms = transform.transform_classrooms()

greedy = greedySolver.Greedy(classes,timeslots,classrooms)

sorted_classes = greedy.sorting_classes()
scheduled, unscheduled = greedy.greedy_schedule()


upload = dbDataInsert.Update()
upload.update_schedule(scheduled)

Schedule.greedy_schedule()
