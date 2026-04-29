"""
Graph Engine for Timetable Scheduling (Stage 2: Graph Theory)

This module builds a conflict graph between classes and applies a graph
coloring algorithm (Welsh–Powell heuristic) to assign time slots such that
no conflicting classes occur at the same time.

Conflicts are defined as:
1. Same professor assigned to multiple classes
2. Same student group assigned to multiple classes

Outcome:
- Conflict-free timetable
- Efficient use of minimum time slots
"""

class graph_generator():
    """
    Generates a conflict graph and applies graph coloring
    to assign time slots to classes.

    Attributes:
        graph (dict): Adjacency list representing conflicts
    """
    
    def __init__(self, classes, timeslots, prof_availablity):
        """Initialize an empty graph."""
        self.classes = classes
        self.timeslots = timeslots
        self.prof_availablity = prof_availablity
        self.class_map = {cl['class_id'] : cl for cl in self.classes}
        self.unscheduled = []
        self.graph = {}
        self.result = []

    def conflict_graph(self):
        self.graph = {}
        """
        Builds the conflict graph.

        Each node = class
        Edge exists if:
        - Same professor
        - Same student group

        Returns:
            dict: Graph with class IDs as keys and list of conflicting class IDs as values
        """
        for eachclass in self.classes:
            
            # Initialize adjacency list for each class
            self.graph[eachclass['class_id']] = set()

            # ------------------------------------------------
            # 1. Professor Conflict
            # ------------------------------------------------
            for conflicts in self.classes:
                
                if eachclass['class_id'] == conflicts['class_id']:
                    continue
                
                if (eachclass['prof_id'] == conflicts['prof_id']):
                    self.graph[eachclass['class_id']].add(conflicts['class_id'])
                    
                if (
                    eachclass['cid'] == conflicts['cid']
                    and eachclass['group_id'] == conflicts['group_id']
                ):  
                    self.graph[eachclass['class_id']].add(conflicts['class_id'])
                            
        return self.graph

    def sorted_graph(self):
        """
        Sort nodes based on degree (number of conflicts).

        This follows Welsh–Powell strategy:
        Nodes with higher conflicts are colored first.

        Returns:
            list: Class IDs sorted by descending degree
        """
        degree = []

        for node in self.graph:
            degree.append((node, len(self.graph[node])))

        # Sort by highest degree first
        degree.sort(key=lambda x: x[1], reverse=True)

        # Extract only node names
        sorted_nodes_graph = [node for node, _ in degree]

        return sorted_nodes_graph

    
    def is_prof_available(self, prof_id, timeslot):
        
        prof_slots = self.prof_availablity.get(prof_id, [])
        
        for slot in prof_slots:
            if(slot['day'] == timeslot["day"]
                and slot['start_time'] <= timeslot['start_time']
                and slot['end_time'] >= timeslot['end_time']
                ):
                    return True
            
        return False
    
    def coloring_graph(self):
        self.unscheduled = []
        """
        Apply greedy graph coloring (Welsh–Powell heuristic).

        Assigns the smallest possible color (time slot index)
        such that no adjacent nodes share the same color.

        Returns:
            dict: Mapping of class ID → color index
        """
        sorted_nodes_graph = self.sorted_graph()
        colored_graph = {}

        
        timeslot_keys = list(self.timeslots.keys())
        
        for eachnode in sorted_nodes_graph:
            cls = self.class_map[eachnode]
            prof_id = cls['prof_id']

            used_colors = set()
                
            # Collect colors used by neighbors
            neighbors = self.graph[eachnode]
            for eachneighbor in neighbors:
                if eachneighbor in colored_graph:
                    used_colors.add(colored_graph[eachneighbor])
            
            color = 0
            
            while True:
                if color >= len(timeslot_keys):
                    self.unscheduled.append(eachnode)
                    # print(f"{eachnode} is unscheduled class")
                    break
                
                timeslot = self.timeslots[timeslot_keys[color]]
                # Assign smallest unused color
                if color not in used_colors and self.is_prof_available(prof_id, timeslot):
                    colored_graph[eachnode] = color
                    break
                else:
                    color += 1

        return colored_graph, self.unscheduled
    

    def timeslot_mapping(self, colored):
        self.result = []
        """
        Maps assigned colors to actual time slots.

        Converts color indices (0,1,2...) → timeslot keys (T1, T2, ...)

        Prints:
            Class → Assigned timeslot details
        """
        colored_graph = colored
        # Extract timeslot keys in order
        timeslot_keys = list(self.timeslots.keys())

        for eachclass in colored_graph:
            color_index = colored_graph[eachclass]

            # Check if enough timeslots exist
            if color_index >= len(timeslot_keys):
                print(f"{eachclass} ---> No available timeslot")
                continue

            # Map color → timeslot
            slot_key = timeslot_keys[color_index]
            cls = self.class_map[eachclass]
            
            '''to add prof to result'''
            self.result.append([eachclass, slot_key, cls['prof_id'], cls['cid'], cls['group_id'], cls['total_students']])
        return self.result

    def validate_schedule(self, colored):
        """
        Validates that no conflicting classes share the same timeslot.

        Prints:
            - Conflict details if found
            - Success message if schedule is valid
        """
        colored_graph = colored
        conflict_found = False

        for node in self.graph:
            for neighbor in self.graph[node]:
                if node in colored_graph and neighbor in colored_graph:
                    if colored_graph[node] == colored_graph[neighbor]:
                        print(f"Conflict: {node} and {neighbor} share same slot")
                        conflict_found = True

        if not conflict_found:
            print("Schedule Validated successfully")


# graphing = graph_generator()

# # Build conflict graph
# finalgraph = graphing.conflict_graph()

# # Generate coloring result
# deg = graphing.coloring_graph()
# print("Colored Graph:", deg)

# print("\nTimeslot Mapping:\n")
# graphing.timeslot_mapping()

# print("\nValidation:\n")
# graphing.validate_schedule()