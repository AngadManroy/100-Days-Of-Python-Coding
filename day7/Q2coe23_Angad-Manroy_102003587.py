# Simple Hill Climb with heureistic = +-n
import copy

initial_state = [[],[],[],['B','C','D','A']]
goal_state = [[],[],[],['A','B','C','D']]
visited = []

def compare(newstate):
    if newstate == goal_state:
        return True
    return False

def heuristic(newstate):
    d=0
    goal = goal_state[3]

    for i in range(len(newstate)):
        sublist = newstate[i]
        if len(sublist) > 0:
            for j in range(len(sublist)):
                if sublist[j] != goal[j]: # comparing current state with final stacked goal state
                    d-=j
                else:
                    d+=j
    return d

def children(cur_heuristic,newstate):
    state = copy.deepcopy(newstate)
    for i in range(len(state)):
        temp = copy.deepcopy(state)
        if len(temp[i]) > 0:
            clear_block = temp[i].pop()
            for j in range(len(temp)):
                temp2 = copy.deepcopy(temp)
                if j != i:
                    temp2[j] = temp2[j] + [clear_block]
                    if temp2 not in visited:
                        new_heuristic = heuristic(temp2)
                        if new_heuristic > cur_heuristic:
                            child = copy.deepcopy(temp2)
                            return child

    return 0

if __name__=="__main__":
    if compare(initial_state):
        print("****Goal Reached****")
        exit()
    
    newstate = copy.deepcopy(initial_state)
    while(4):
        visited.append(copy.deepcopy(newstate))
        print(newstate)
        cur_heuristic = heuristic(newstate)
        child = children(cur_heuristic,newstate)
        if (child==0):
            print("Final Solution: ",newstate)
            exit()
        newstate = copy.deepcopy(child)