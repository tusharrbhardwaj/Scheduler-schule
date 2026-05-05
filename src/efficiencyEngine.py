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
        self.capacity = [value for value in self.classrooms.values()]
        self.capacity = sorted(self.capacity, reverse=True)
        
        # making dp input as in class_id = [] and strenth = [] for each timeslot
        for each_timeslot in timeslot_map.values():
            strength = []
            classes = []
            for eachclass in each_timeslot:
                strength.append(eachclass[1])
                classes.append(eachclass[0])
                
                
            self.dynamic_program(strength, classes)

        
            
        return timeslot_map
    
    def dynamic_program(self, strength, classes):
        used_room = set()
        path = {}
        i = 0
        for eachcls in classes:
            eligible = {}
            index = classes.index(eachcls)
            for eachroom in self.classrooms:
                seat_wasted = 0
                capacity = self.classrooms[eachroom]
                temp_path = []
                temp = {}
                if eachroom in used_room:
                    continue
                else:
                    if strength[index] <= capacity:
                        seat_wasted = seat_wasted + capacity-strength[index]
                        temp[eachcls] = eachroom
                        temp_path.append(temp)
                        i += 1
                
                        eligible[eachroom] = seat_wasted
                
                if len(eligible) == 0:
                    print("Cannot Schedule this class")
                    
            
            best_room = min(eligible, key = eligible.get)
                    
            path[i] = temp_path
            used_room.add(best_room)
        
        
            
            
                