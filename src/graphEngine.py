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

import fetchData

# ------------------------------------------------------------
# Data Loading Section
# ------------------------------------------------------------

data = fetchData.Data()

# Professor data
p_ids, p_availablity = data.readProfJson()

# Room capacity data (not used in this stage)
r_capacity = data.readRooms()

# Student group data
groups, group_size = data.readStudents()

# Class constraints (contains class ID, professor, etc.)
classes = data.readClassConstrains()

# Mapping of student groups to classes
grouped_classes = data.classGroups()

# Available time slots (dictionary: T1 → {day, start, end})
timeslots = data.readTimeslots()


# ------------------------------------------------------------
# Graph Generator Class
# ------------------------------------------------------------

class graph_generator():
    """
    Generates a conflict graph and applies graph coloring
    to assign time slots to classes.

    Attributes:
        graph (dict): Adjacency list representing conflicts
    """
    
    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}

    def conflict_graph(self):
        """
        Builds the conflict graph.

        Each node = class
        Edge exists if:
        - Same professor
        - Same student group

        Returns:
            dict: Graph with class IDs as keys and list of conflicting class IDs as values
        """
        for eachclass in classes:
            
            # Initialize adjacency list for each class
            self.graph[eachclass['id']] = []

            # ------------------------------------------------
            # 1. Professor Conflict
            # ------------------------------------------------
            for smpf in classes:
                if (
                    eachclass['professor'] == smpf['professor']
                    and smpf['id'] != eachclass['id']
                ):
                    self.graph[eachclass['id']].append(smpf['id'])

            # ------------------------------------------------
            # 2. Student Group Conflict
            # ------------------------------------------------
            for eachgroup in grouped_classes:
                conflict_group = grouped_classes[eachgroup]

                if eachclass['id'] in conflict_group:
                    for everygrp in conflict_group:
                        if (
                            everygrp != eachclass['id']
                            and everygrp not in self.graph[eachclass['id']]
                        ):
                            self.graph[eachclass['id']].append(everygrp)

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

    def coloring_graph(self):
        """
        Apply greedy graph coloring (Welsh–Powell heuristic).

        Assigns the smallest possible color (time slot index)
        such that no adjacent nodes share the same color.

        Returns:
            dict: Mapping of class ID → color index
        """
        sorted_nodes_graph = self.sorted_graph()
        colored_graph = {}

        for eachnode in sorted_nodes_graph:
            color = 0
            used_colors = set()

            # Collect colors used by neighbors
            neighbors = self.graph[eachnode]
            for eachneighbor in neighbors:
                if eachneighbor in colored_graph:
                    used_colors.add(colored_graph[eachneighbor])

            # Assign smallest unused color
            while color in used_colors:
                color += 1

            colored_graph[eachnode] = color

        return colored_graph

    def timeslot_mapping(self):
        """
        Maps assigned colors to actual time slots.

        Converts color indices (0,1,2...) → timeslot keys (T1, T2, ...)

        Prints:
            Class → Assigned timeslot details
        """
        colored_graph = self.coloring_graph()

        # Extract timeslot keys in order
        timeslot_keys = list(timeslots.keys())

        for eachclass in colored_graph:
            color_index = colored_graph[eachclass]

            # Check if enough timeslots exist
            if color_index >= len(timeslot_keys):
                print(f"{eachclass} ---> No available timeslot")
                continue

            # Map color → timeslot
            slot_key = timeslot_keys[color_index]
            print(f"{eachclass} ---> {timeslots[slot_key]}")

    def validate_schedule(self):
        """
        Validates that no conflicting classes share the same timeslot.

        Prints:
            - Conflict details if found
            - Success message if schedule is valid
        """
        colored_graph = self.coloring_graph()
        conflict_found = False

        for node in self.graph:
            for neighbor in self.graph[node]:
                if colored_graph[node] == colored_graph[neighbor]:
                    print(f"Conflict: {node} and {neighbor} share same slot")
                    conflict_found = True

        if not conflict_found:
            print("Schedule Validated successfully")


# ------------------------------------------------------------
# Execution Section
# ------------------------------------------------------------

graphing = graph_generator()

# Build conflict graph
finalgraph = graphing.conflict_graph()

# Generate coloring result
deg = graphing.coloring_graph()
print("Colored Graph:", deg)

print("\nTimeslot Mapping:\n")
graphing.timeslot_mapping()

print("\nValidation:\n")
graphing.validate_schedule()