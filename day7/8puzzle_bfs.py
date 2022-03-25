from doctest import NORMALIZE_WHITESPACE
import numpy
import copy

initial_state = numpy.array([ [1,2,3] , [8,0,4] , [7,6,5] ])
goal_state = numpy.array([ [2,8,1] , [0,4,3] , [7,6,5] ])
q=[]
visited =[]

def pos(newstate):
    for i in range(0,3):
        for j in range(0,3):
            if newstate[i][j] == 0:
                return [i,j]

def up(newstate,pos):
    print("Enter up")
    copys = copy.deepcopy(newstate)
    row = pos[0]
    col = pos[1]
    if row == 0:
        print("Exit up")
        return copys
    else:
        copys[row][col] = copys[row-1][col]
        copys[row-1][col] = 0
    print("Exit up")
    return copys

def down(newstate,pos):
    print("Enter dowon")
    copys = copy.deepcopy(newstate)
    row = pos[0]
    col = pos[1]
    if row == len(newstate)-1:
        print("Exit down")
        return copys
    else:
        copys[row][col] = copys[row+1][col]
        copys[row+1][col] = 0
    print("Exit down")
    return copys

def left(newstate,pos):
    print("Enter left")
    copys = copy.deepcopy(newstate)
    row = pos[0]
    col = pos[1]
    if col == 0:
        print("Exit left")
        return copys
    else:
        copys[row][col] = copys[row][col-1]
        copys[row][col-1] = 0
    print("Exit left")
    return copys

def right(newstate,pos):
    print("Enter right")
    copys = copy.deepcopy(newstate)
    row = pos[0]
    col = pos[1]
    if col == len(newstate)-1:
        print("Exit right")
        return copys
    else:
        copys[row][col] = copys[row][col+1]
        copys[row][col+1] = 0
    print("Exit right")
    return copys

def compare(newstate):
    global goal_state
    if numpy.array_equal(newstate,goal_state):
        return True
    else:
        return False

def enq(newstate):
    global q
    q.append(newstate)

def deq():
    global q
    q.pop(0)

def occured(newstate):
    global visited
    for states in visited:
        if numpy.array_equal(newstate,states):
            return True
    else:
        return False

if __name__ == "__main__":
    enq(initial_state)
    cnt=0

    while(8):
        cnt+=1
        zero = pos(q[0])

        newstate = up(q[0],zero)
        if compare(newstate):
            print("*****Found******")
            print(cnt)
            exit()
        if not occured(newstate):
            visited.append(newstate)
            q.append(newstate)
        
        newstate = down(q[0],zero)
        if compare(newstate):
            print("*****Found******")
            print(cnt)
            exit()
        if not occured(newstate):
            visited.append(newstate)
            q.append(newstate)

        newstate = left(q[0],zero)
        if compare(newstate):
            print("*****Found******")
            print(cnt)
            exit()
        if not occured(newstate):
            visited.append(newstate)
            q.append(newstate)

        newstate = right(q[0],zero)
        if compare(newstate):
            print("*****Found******")
            print(cnt)
            exit()
        if not occured(newstate):
            visited.append(newstate)
            q.append(newstate)

        deq()