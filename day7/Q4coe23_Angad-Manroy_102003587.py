#backtracking not allowed
open = [ ('a',0) ]
closed =[]
priority=[]

if __name__=="__main__":
    heuristic = [ ('b',1) , ('c',3) , ('d',2) , ('e',2) , ('f',3) , ('g',0) ]
    beta = int(input("press [2] for beta =2, press [3] for beta =3"))
    adjacency = [ [0,1,1,0,0,0,0] ,
                  [1,0,0,1,1,0,0] ,
                  [1,0,0,0,0,1,1] , 
                  [0,1,0,0,0,0,0] ,
                  [0,1,0,0,0,0,0] ,
                  [0,0,1,0,0,0,0] ,
                  [0,0,1,0,0,0,0] ]
    for i in len(adjacency):
        