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
from data import dbDataInsert
from src import greedySolver
from src import graphEngine
from rich.console import Console
from rich.table import Table



# Stage 1: Fetch
transform = Transformation()
classes = transform.readData("classes")
timeslots = transform.transform_timeslot()
classrooms = transform.transform_classrooms()
class_groups = transform.transform_classgroups()
prof_availablity = transform.transform_prof_availablity()
#insert in db
upload = dbDataInsert.Update()

console = Console(record=True)


def greedy_scheduling():
    try:
        # Stage 2: Schedule
        greedy = greedySolver.Greedy(classes, timeslots, classrooms, prof_availablity)
        scheduled, unscheduled = greedy.greedy_schedule()

        # Stage 3: Store
        upload.update_greedyschedule(scheduled)

        # Stage 4: Fetch + Display
        data = Schedule.greedy_schedule()

        table = Table(title="Greedy Schedule", show_lines=True)

        for col in data[0]:
            table.add_column(col, justify="center")

        for row in data[1:]:
            table.add_row(*[str(x) for x in row])

        console.print(table)

        # Save output
        with open('output/greedy_output.txt', 'w') as file:
            file.write(console.export_text())

        print("Data saved to output/greedy_output.txt")
        
        print(f"{len(unscheduled)} classes left unscheduled using greedySolver : \n", unscheduled)

    except Exception as e:
        print("Scheduling pipeline failed:\n", e)
        

def graph_engine():
        
        #schedule
        graph = graphEngine.graph_generator(classes,class_groups,timeslots)
        
        graph.conflict_graph() 
        graph.coloring_graph()
        graph_schedule = graph.timeslot_mapping()
        graph.validate_schedule()
        
        #upload
        upload.update_graphschedule(graph_schedule)

        #fetch and display
        
        data = Schedule.graph_schedule()

        console = Console(record=True)
        table = Table(title="Graph Schedule", show_lines=True)

        for col in data[0]:
            table.add_column(col, justify="center")

        for row in data[1:]:
            table.add_row(*[str(x) for x in row])

        console.print(table)

        # Save output
        with open('output/graph_output.txt', 'w') as file:
            file.write(console.export_text())

        print("Data saved to output/graph_output.txt")

# # Generate coloring result
# deg = graphing.coloring_graph()
# print("Colored Graph:", deg)

# print("\nTimeslot Mapping:\n")
# graphing.timeslot_mapping()

# print("\nValidation:\n")
# graphing.validate_schedule()

        
if __name__ == "__main__":
        greedy_scheduling()
        # graph_engine()
        
        
# add room constraint to graphEngine

# add prof pref to greedy 