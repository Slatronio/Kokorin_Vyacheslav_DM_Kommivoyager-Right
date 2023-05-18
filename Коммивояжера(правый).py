def minus1(c: dict,  t: list):
    pq=0
    for i1 in list(c.keys()):
        for i2 in list(c[i1].keys()):
            c[i1][i2]=c[i1][i2]-t[pq]
        pq+=1
    return c

def minus2(c:dict, t:list):
    pq=0
    for i1 in list(c[list(c.keys())[0]].keys()):
        for i2 in list(c.keys()):
            c[i2][i1]=c[i2][i1]-t[pq]
        pq+=1
    return c

def min_collumn(c:dict, t:list):
    for i1 in list(c[list(c.keys())[0]].keys()):
        q=[]
        for i2 in list(c.keys()):
            q.append(c[i2][i1])
        if min(q) == math.inf:
            t.append(0)
        else:
            t.append(min(q))
    return t

def zero_not_zero(c:dict, cc:dict):
    for i1 in list(c.keys()):
        for i2 in list(c[i1].keys()):
            if c[i1][i2]==0:
                q=[]
                keysC1=list(c.keys())
                keysC1.remove(i1)
                keysC2=list(c[i1].keys())
                keysC2.remove(i2)
                C1=[]
                C2=[]
                for pp in keysC1:
                    C1.append(c[pp][i2])
                for pp in keysC2:
                    C2.append(c[i1][pp])
                cc[i1][i2]=min(C1)+min(C2)
    return cc
                    
def delete(c:dict,cc:dict):
    q=[]
    ind1=0
    ind2=0
    for i1 in list(c.keys()):
        for i2 in list(c[i1].keys()):
           if c[i1][i2]==0:
               q.append(cc[i1][i2])
    for i1 in list(c.keys()):
        for i2 in list(c[i1].keys()):
            if cc[i1][i2]==max(q) and c[i1][i2]==0:
               ind1=i1
               ind2=i2
               break
    if ind2 in list(c.keys()):
        c[ind2][ind1]=math.inf
    del c[ind1]
    del cc[ind1]
    for i in list(c.keys()):
        del c[i][ind2]
        del cc[i][ind2]
    for i in list(cc.keys()):
        for j in list(cc[i].keys()):
            cc[i][j]=0
    return c,cc
    
import math
c={1:{1:math.inf,2:12,3:22,4:28,5:32},
   2:{1:12,2:math.inf,3:10,4:40,5:20},
   3:{1:22,2:10,3:math.inf,4:50,5:10},
   4:{1:28,2:27,3:17,4:math.inf,5:27},
   5:{1:32,2:20,3:10,4:60,5:math.inf}}
cc={1:{1:0,2:0,3:0,4:0,5:0},
    2:{1:0,2:0,3:0,4:0,5:0},
    3:{1:0,2:0,3:0,4:0,5:0},
    4:{1:0,2:0,3:0,4:0,5:0},
    5:{1:0,2:0,3:0,4:0,5:0}}
k=0
for tips in range(len(c)-1):
    t=[]
    for j in list(c.keys()):
        if min(list(c[j].values()))==math.inf:
            t.append(0)
        else:
            t.append(min(list(c[j].values())))
    c=minus1(c,t)
    k+=sum(t)
    t=[]
    t=min_collumn(c,t)
    k+=sum(t)
    c=minus2(c,t)
    cc=zero_not_zero(c,cc)
    for i in list(c.keys()):
        print(c[i])
    print('_________________')
    c,cc=delete(c,cc)
print(k)
