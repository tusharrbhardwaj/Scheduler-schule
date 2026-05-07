class efficient:
    
    def __init__(self, graph_schedule, classrooms):
        self.graph_schedule = graph_schedule
        self.classrooms = classrooms
        self.capacity = []
        self.best_choices = {}
        self.memo = {} #for memoization
        
    def optimized_room_allocation(self):
        timeslot_map = {}
        all_allocations = {}
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
                
            classes, strength = map(list, zip(*sorted(zip(classes, strength), key=lambda x: x[1], reverse=True)))
            
            allocation = self.dynamic_program(strength, classes)
            all_allocations.update(allocation)            

        
            
        return all_allocations
    
    def dynamic_program(self, strength, classes):
        used_room = set()
        self.memo = {}
        self.best_choices = {}
        index = 0

        self.dp(index, used_room, strength, classes)
        
        allocation = self.path(classes)

        print(allocation)
        return allocation
        
    
    def dp(self, index, used_room, strength, classes):
        
        state = (index, tuple(sorted(used_room))) #converted used_room set to tuple to make it hasable so that it can be used as keys in memo{}
        best_room = None

        if state in self.memo:
            return self.memo[state]
        
        if index == len(strength):
            return 0
        
        best = float('inf') #maximize waste by putting best as infinity
        
        for eachroom, capacity in self.classrooms.items():
            
            if eachroom not in used_room and capacity >= strength[index]:
                waste = capacity - strength[index]
                rooms = used_room.copy() #making copy of set to avoid uploading to the original set directly
                rooms.add(eachroom)
                
                total = waste + self.dp(index+1, rooms, strength, classes)

                if total < best:
                    best = total
                    best_room = eachroom  
        
        if best_room is not None:
            self.best_choices[state] = best_room
            self.memo[state] = best
        
        return best
    
    def path(self, classes):
        used_room = set()
        index = 0
        best_room = None
        allocation = {}
        

        while index < len(classes):
            state = (index, tuple(sorted(used_room)))
            
            if state not in self.best_choices:
                print(f"No feasible allocation for class {classes[index]}")
                allocation[classes[index]] = None
                break

            best_room = self.best_choices[state]
            allocation[classes[index]] = best_room
            
            used_room.add(best_room)
            index += 1
        
        return allocation
            
            
                