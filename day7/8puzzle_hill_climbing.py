# Solution to 8 puzzle problem using a heuristic function(Manhattan Distanc/Misplaced Tiles)
# AIM: To make use of Hill Climb Algorithm whose generic usage is to reach the best possible state
# within our computational ability. This algorithm is used to provide good initial states to other
# algorithms and research programs.
# This also focuses on Space Complexity
# Approach: Instead of maintaining a queue of all pending unique states to be visited in our graph
# we now iterate over only those nodes which provide an improvement over current state.
# Limitation: Due to the way we approach we might not reach our goal state in 8 puzzle problem with
# this Algorithm.
import numpy
import copy
import math

initial_state = numpy.array([ [1,2,3] , [8,0,4] , [7,6,5] ])
goal_state = numpy.array([ [2,8,1] , [0,4,3] , [7,6,5] ])
q=[]
visited =[]

# 6 Utility Functions
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

# A heuristic function defined using Manhattan Distance: |x1-x2| + |y1-y1|
# as the base. USing this we attatch a cost to evry node that we can search and hence
# explore those nodes first which are closer to our goal state in the sense defined by
# our heuristic function.
def heuristic(newstate):
    global goal_state
    d=0
    for i in range(len(newstate)):
        for j in range(len(newstate)):
            gcordinates = numpy.where(goal_state == newstate[i][j])
            d+= abs( (i-gcordinates[0][0]) ) + abs( (j-gcordinates[1][0]) )
    return d

# We now have a queue of tuples that contains the heuristic function output and the state
def enq(newstate):
    global q
    package = (heuristic(newstate),newstate)
    q.append(package)

# We now keep on sorting the queue after we pop the root element at the end of 
# every iteration of the while loop so that the next node treated as root is the closest 
# to our goal state in the sense defined by heuristic function.
def deq():
    global q
    truth = False
    # Traverse the entire queue to compare the heuristic values for dif. states and incase
    # there's no state offering improvement exit from program else eliminate all states except
    # the one offering best improvement.
    for i in range(len(q)):
        if q[i][0]<q[0][0]:
            truth=True
    if truth==False:
        exit()
    else:
        q.sort(key= lambda x: x[0])
        while len(q) != 1:
            q.pop()


# Check whether the newly generated state has been encountered before.
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
        zero = pos(q[0][1])

        newstate = up(q[0][1],zero)
        if compare(newstate):
            print("*****Found******")
            print(cnt)
            exit()
        if not occured(newstate):
            visited.append(newstate)
            enq(newstate)
        
        newstate = down(q[0][1],zero)
        if compare(newstate):
            print("*****Found******")
            print(cnt)
            exit()
        if not occured(newstate):
            visited.append(newstate)
            enq(newstate)

        newstate = left(q[0][1],zero)
        if compare(newstate):
            print("*****Found******")
            print(cnt)
            exit()
        if not occured(newstate):
            visited.append(newstate)
            enq(newstate)

        newstate = right(q[0][1],zero)
        if compare(newstate):
            print("*****Found******")
            print(cnt)
            exit()
        if not occured(newstate):
            visited.append(newstate)
            enq(newstate)

        deq()