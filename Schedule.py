
import numpy as np
  
Data = np.genfromtxt("data.txt", dtype=int,
                     encoding=None, delimiter=" ")
                     
processesnum=np.linspace(1,len(Data[:,0]),num=len(Data[:,0]))
Data= np.insert(Data, 0, processesnum, axis=1)

#First Come First serve
arr4=Data[Data[:, 2].argsort()]
total4=0
state4=''
for i in arr4[:,0]:
    state4+="P"
    state4+=str(i)
    state4+=":"
    state4+=str(total4)
    state4+="-"
    total4+=arr4[i-1,1]
    state4+=str(total4)
    state4+=", "

#Shortest Job first algorithm
arr3=Data[Data[:, 1].argsort()]
total3=0
state3=''
count3=0
for i in arr3[:,0]:
    state3+="P"
    state3+=str(i)
    state3+=":"
    state3+=str(total3)
    state3+="-"
    total3+=arr3[count3,1]
    state3+=str(total3)
    state3+=", "
    count3+=1

#Priority scheduling
arr=Data[Data[:, 3].argsort()]
count=0
timeline=np.empty(0).astype(int)
timeline=np.append(timeline,0)
w=np.unique(Data[:,3])
p1=[]
for time in w:
    p1=arr[arr[:,3]==w[time]]
    arr[arr[:,3]==w[time]]=arr[arr[:,3]==w[time]][arr[arr[:,3]==w[time]][:, 2].argsort()]
    for i in p1[:,1]:
        timeline=np.append(timeline,i)
state=""
prev=timeline[count]
for i in arr[:,0]:
    state+="P"
    state+=str(i)
    state+=":"

    state+=str(prev)
    state+="-"
    prev+=timeline[count+1]
    state+=str(prev)
    count+=1
    if count== len(processesnum) :
        break
    else:
        state+=", "





#Round Roubin scheduling
arr2=Data[Data[:, 2].argsort()]

timeline2=np.empty(0).astype(int)
readyQueue=np.empty(0).astype(int)
burst=Data[:,1]
timeline2=np.append(timeline2,0)
total=0
state2=""
index=0
for p in arr2[:,0]:
    if arr2[p-1,2]<= total:
        readyQueue=np.append(readyQueue,p)
        if burst[p-1]<=4:
            state2+="P"
            state2+=str(p)
            state2+=":"
            state2+=str(total)
            state2+="-"
            timeline2=np.append(timeline2,burst[p-1]+total)
            total+=burst[p-1]
            burst[p-1]=0
            readyQueue=np.setdiff1d(readyQueue,p)
            state2+=str(total)+", "

        else:
            state2+="P"
            state2+=str(p)
            state2+=":"
            state2+=str(total)
            state2+="-"
            timeline2=np.append(timeline2,4+total)
            total+=4
            burst[p-1]-=4
            state2+=str(total)+", "
while(True):
    for r in readyQueue:
        if burst[r-1]<=4:
            state2+="P"
            state2+=str(r)
            state2+=":"
            state2+=str(total)
            state2+="-"
            timeline2=np.append(timeline2,burst[r-1]+total)
            total+=burst[r-1]
            burst[r-1]=0
            readyQueue=np.setdiff1d(readyQueue,r)
            state2+=str(total)+", "
        else:
            state2+="P"
            state2+=str(r)
            state2+=":"
            state2+=str(total)
            state2+="-"
            timeline2=np.append(timeline2,4+total)
            total+=4
            burst[r-1]-=4
            state2+=str(total)+", "
    if np.array_equal(burst,np.zeros(np.size(burst),dtype=int)):
       break

print("FCFS:")
print(state4.rstrip(", "))
print("SJF:")
print(state3.rstrip(", "))
print("RR:")
print(state2.rstrip(", "))
print("Priority:")  
print(state)
