class efficient:
    
    def __init__(self, graph_schedule, classrooms):
        self.graph_schedule = graph_schedule
        self.classrooms = classrooms
        
    def optimized_room_allocation(self):
        timeslot_map = {}
        for eachclass in self.graph_schedule:
            timeslot = eachclass[1]
            
            if timeslot in timeslot_map:
                timeslot_map[timeslot].append([eachclass[0], eachclass[-1]])
            else:
                timeslot_map[timeslot] = [[eachclass[0], eachclass[-1]]]
        
        # making classroom input for dp to consume
        capacity = [value for value in self.classrooms.values()]
        print(capacity)
        
        # making dp input as in class_id = [] and strenth = [] for each timeslot
        for each_timeslot in timeslot_map.values():
            strength = []
            classes = []
            for eachclass in each_timeslot:
                strength.append(eachclass[1])
                classes.append(eachclass[0])
            print(f"classes = {classes}")
            print(f"stength = {strength}")
        
            
        return timeslot_map
    
    def dynamic_program(self):
        pass