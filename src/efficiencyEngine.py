class efficient:
    
    def __init__(self, graph_schedule, classrooms):
        self.graph_schedule = graph_schedule
        self.classrooms = classrooms
        self.capacity = []
        
    def optimized_room_allocation(self):
        timeslot_map = {}
        for eachclass in self.graph_schedule:
            timeslot = eachclass[1]
            
            if timeslot in timeslot_map:
                timeslot_map[timeslot].append([eachclass[0], eachclass[-1]])
            else:
                timeslot_map[timeslot] = [[eachclass[0], eachclass[-1]]]
        
        # making classroom input for dp to consume
        
        # making dp input as in class_id = [] and strenth = [] for each timeslot
        for each_timeslot in timeslot_map.values():
            strength = []
            classes = []
            
            
            for eachclass in each_timeslot:
                strength.append(eachclass[1])
                classes.append(eachclass[0])
                
            strength, classes = map(list, zip(*sorted(zip(classes, strength), key=lambda x: x[1], reverse=True)))
            self.dynamic_program(strength, classes)

        
            
        return timeslot_map
    
    def dynamic_program(self, strength, classes):
        used_room = set()
        index = 0

        self.dp(index, used_room, strength, classes)
        
        # allocation = {}
        
        # for cls_index, eachcls in enumerate(classes):
            
            
        #     eligible = {}
            
        #     for eachroom, capacity in self.classrooms.items():
                
                
        #         if eachroom in used_room:
        #             continue
                
                
        #         if strength[index] <= capacity:
        #             eligible[eachroom] = capacity - strength[index]

            
        #     if not eligible:
        #         print(f"Cannot Schedule class {eachcls}")
        #         continue
            
        #     best_room = min(eligible, key = eligible.get)
                    
        #     allocation[eachcls] = best_room
        #     used_room.add(best_room)
        
        # print(allocation)
    
    
    def dp(self, index, used_room, strength, classes):
        if index == len(strength):
            return 0
        
        best = 0
        rooms = used_room
        
        for eachroom, capacity in self.classrooms.items():
            
            if eachroom not in used_room and capacity >= strength[index]:
                waste = capacity - strength[index]
                rooms.add(eachroom)
                print("room", eachroom, "to", classes[index])
                total = waste + self.dp(index+1, used_room, strength, classes)
            
        return total
        
            
            
                