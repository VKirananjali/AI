from collections import deque
def water_jug_pbm(jug1,jug2,target):
    que=deque()
    que.append([0,0])
    solvable=False
    visited=set()
    path=[]
    while que:
        cs=que.popleft()
        if((cs[0],cs[1]) in visited):
            continue
        path.append([cs[0],cs[1]])
        visited.add((cs[0],cs[1]))
        if(cs[0]==target or cs[1]==target):
            solvable=True
            if(cs[0]==target):
                if(cs[1]!=0):
                    path.append([cs[0],0])
            else:
                if(cs[0]!=0):
                    path.append([0,cs[1]])
            for i in range(len(path)):
                print("(",path[i][0],",",path[i][1],")")
            break
            
        # filling jugs
        que.append([cs[0],jug2])
        que.append([jug1,cs[1]])
        
        #emptying jugs
        que.append([cs[0],0])
        que.append([0,cs[1]])
        
        ad=min(jug1-cs[0],cs[1]) #pour from 2 to 1
        que.append([cs[0]+ad,cs[1]-ad])

        ad=min(jug2-cs[1],cs[0]) #pour from 1 to 2
        que.append([cs[0]-ad,cs[1]+ad])

    if(not solvable):
        print("no solution found")

water_jug_pbm(4,3,2)
