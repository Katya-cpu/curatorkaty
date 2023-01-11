f=open("C:/Users/467/Desktop/k8-0.txt")
s=f.read()
f.close()
k=1
mk=0
simv=''
massimv=[]
for i in range (len(s)-1):
    if s[i]==s[i+1]:
        k+=1
        simv=s[i]
        mk=max(mk,k)
    else:
        if k!=1:
            massimv.append(simv)
            massimv.append(mk)
        k=1
kon=massimv[-1]
j=0
for i in range (1,len(massimv),2):
    if massimv[i]==kon:
        j=i
        break
massimv=massimv[j-1:]
print(*massimv)
