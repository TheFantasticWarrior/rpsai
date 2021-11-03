import random
import numpy as np
encode={"R":{"R":"0","P":"1","S":"2"},
        "P":{"R":"3","P":"4","S":"5"},
        "S":{"R":"6","P":"7","S":"8"},}
decode={"0":("R","R"),"1":("R","P"),"2":("R","S"),
        "3":("P","R"),"4":("P","P"),"5":("P","S"),
        "6":("S","R"),"4":("S","P"),"8":("S","S")}
actions=["R","P","S"]
def sigmoid(x):
    return round(1/(1 + np.exp(-x)),2)
def probability():
    def search(n):
        x=0
        for i in range(1,len(past)):
            c=past[:-i].count(past[-i:]+n)
            if c==0:
                return x
            else:
                x+=c*sigmoid(2*i)
    l=[search(str(i)) for i in range(9)]
    x=[sum(l[i-3:i]) for i in range(3,10,3)]
    nx=[round(np.exp(a)/sum(np.exp(x)),2) for a in x]
    return nx
    return decode[str(x.index(max(x))*3)][0]

if input=="":
    output=random.choice("RPS")
    past=""
    last=[]
    qlist=np.zeros([3,3,3])
else:
    past+=encode[input][output]
    if len(past)<10:
        output=random.choice("RPS")
    if len(past)>3:
        p=np.array(probability())
        f,s=sorted(p)[:2]
        dif=f-s
        nx,ny=np.argsort(p)[::-1][:2]
        alpha=0.5
        beta=0.8
        reward=1 if (actions[(actions.index(input)+1)%3]==output)\
                else -0.8 if (actions[(actions.index(input)-1)%3]==output) else -0.4
        if len(past)>10:
            qlist[x,y,actions.index(output)]*=(1-alpha)
            qlist[x,y,actions.index(output)]+=alpha*(old_reward+beta*max(qlist[nx,ny,:]))
            a,b=sorted(qlist[nx,ny,:],reverse=True)[:2]
            if a<-0.5:
                output=random.choice("RPS")
            elif a-b<0.1:
                output=random.choice("RPS")
                """output=np.where(qlist[nx,ny,:]==(a or b))
                output=decode[str(random.choice(*output)*3)][0]"""
            else:
                output=actions[np.argmax(qlist[nx,ny,:])]
        """output=decode[str(p.index(max(p))*3)][0]    
        output=actions[(actions.index(output)+1)%3]"""
        x,y=nx,ny
        old_reward=reward
        #print(input,qlist[nx,ny,:],output)
    if len(past)==999:
        print(qlist)