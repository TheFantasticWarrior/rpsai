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
def softmax(x):
    return [round(np.exp(a)/sum(np.exp(x)),1) for a in x]
def string_matching():
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
    return x

if input=="":
    output=random.choice("RPS")
    past=""
    score=[0,0,0]
    dif=[]
    off=[]
    lastm=""
else:
    input,output==output,input
    past+=encode[input][output]
    if lastm!="":
        dif.append((lastm+3-actions.index(input))%3)

    if len(past)<10:
        output=random.choice("RPS")
    if len(past)>3:
        p=np.array(string_matching())
        matching=np.argmax(p)
        print(softmax(p))
        output=actions[(matching-2)%3]
        lastm=matching
    if len(past)==999:
        print(dif)