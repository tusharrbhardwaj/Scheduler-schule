# This is graph engine which maps conflicts at classes which can not go together
'''
Stage 2: Graph Theory (The "Collision" Engine)
•	The Mission: Prevent scheduling conflicts before they occur.
•	The Logic: Construct a conflict graph where each node represents a class. Two nodes are connected if the classes share at least one student group or the same professor. Using this graph, apply a graph coloring algorithm (such as Welsh–Powell) to assign time slots so that no connected classes are scheduled at the same time.
•	The Report: Compare your greedy result from Stage 1 to your graph coloring result. Did graph coloring prevent more conflicts? Why?
•	The Result: A structured map of "safe" vs. "unsafe" time slots.

'''

'''
graph is a conflict-mapped graph in which classes act as node and their edges are conflcits with those classes
there are two types of conflicts here except the room conflict which we tried to solve in ./src/greedySolver.py, 
1. booking prof at same time 
2. same student group assigned for two classes at same time
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



graph = {
    
}

for eachclass in classes:
    graph[eachclass['id']] = [smpf['id'] for smpf in classes if eachclass['professor'] == smpf['professor'] and (smpf['id'] != eachclass['id'])]
    


for key,value in graph.items():
    print(f'{key} ---> {value}')