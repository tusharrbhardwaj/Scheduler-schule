# This is graph engine which maps conflicts at classes which can not go together
'''
Stage 2: Graph Theory (The "Collision" Engine)
•	The Mission: Prevent scheduling conflicts before they occur.
•	The Logic: Construct a conflict graph where each node represents a class. Two nodes are connected if the classes share at least one student group or the same professor. Using this graph, apply a graph coloring algorithm (such as Welsh–Powell) to assign time slots so that no connected classes are scheduled at the same time.
•	The Report: Compare your greedy result from Stage 1 to your graph coloring result. Did graph coloring prevent more conflicts? Why?
•	The Result: A structured map of "safe" vs. "unsafe" time slots.

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

#Grouped_classes : list with data in dictonary fromat for student-group assigmnment to classes
grouped_classes = data.classGroups() 

#timneslots : returns dictonary with data in form of dictonary
timeslots = data.readTimeslots()

'''
---------------------------------------------------------------------------------------------
'''

'''
graph is a conflict-mapped graph in which classes act as node and their edges are conflcits with those classes
there are two types of conflicts here except the room conflict which we tried to solve in ./src/greedySolver.py, 
1. booking prof at same time 
2. same student group assigned for two classes at same time
'''

class graph_generator():
    
    def __init__(self):
        self.graph = {}

    def conflict_graph(self):
        for eachclass in classes:
            #adding Prof conflict
            self.graph[eachclass['id']] = [smpf['id'] for smpf in classes if eachclass['professor'] == smpf['professor'] and (smpf['id'] != eachclass['id'])]
            
            #adding group conflict
            for eachgroup in grouped_classes:
                conflict_group = grouped_classes[eachgroup]
                if eachclass['id'] in conflict_group:
                    for everygrp in conflict_group:
                        if everygrp not in self.graph[eachclass['id']] and everygrp != eachclass['id']:
                            self.graph[eachclass['id']].append(everygrp)
        
    
        return self.graph
    
    def sorted_graph(self):
        degree =[]
        for node in self.graph:
            degree.append((node, len(self.graph[node])))
            
        degree.sort(key=lambda x:x[1],reverse=True)
        sorted_nodes_graph = [each_calculated_node[0] for each_calculated_node in degree]
        
        return sorted_nodes_graph
    
    def coloring_graph(self):
        sorted_nodes_graph = self.sorted_graph()
        colored_graph = {}
        timeslot_list = ["T1","T2","T3","T4","T5","T6","T7","T8","T9","T10","T11","T12","T13","T14","T15","T16","T17","T18","T19","T20"]
       
        for eachnode in sorted_nodes_graph:
            color = 0
            used_colors = set()
            neighbors = self.graph[eachnode]
            for eachneighbor in neighbors:
                if eachneighbor in colored_graph:
                    used_colors.add(colored_graph[eachneighbor])
                
            while color in used_colors:
                color += 1
            
            colored_graph[eachnode] = color
                
                        
            
        return colored_graph
        
    def timeslot_mapping(self):
        colored_graph = self.coloring_graph()

        # Get timeslot keys like ["T1", "T2", ...]
        timeslot_keys = list(timeslots.keys())

        for eachclass in colored_graph:
            color_index = colored_graph[eachclass]

            if color_index >= len(timeslot_keys):
                print(f"{eachclass} ---> No available timeslot")
                continue

            slot_key = timeslot_keys[color_index]
            print(f"{eachclass} ---> {timeslots[slot_key]}")
            
    def validate_schedule(self):
        colored_graph = self.coloring_graph()

        for node in self.graph:
            conflict = False
            for neighbor in self.graph[node]:
                if colored_graph[node] == colored_graph[neighbor]:
                    print(f"Conflict: {node} and {neighbor} share same slot")
                    conflict = True
        if not conflict:   
            print("Schedule Validated successfully")
         

graphing = graph_generator()
finalgraph = graphing.conflict_graph()
# for key,value in finalgraph.items():
#     print(f'{key} ---> {value}')

deg = graphing.coloring_graph()
# for each in deg:
#     print(each, "---->",deg[each])
print(deg)

graphing.timeslot_mapping()
graphing.validate_schedule()