N=4
K=4
mas=[3,6,8,10]
if N*K<mas[-1]-mas[1]:
    print('-1')
n=0
b=0
for i in range (len(mas)-1):
    a=mas[i+1]-mas[i]#расстояние между стоянками
    if a>K:
       print('-1')
       break
    else:
        if b>=a:#тогда он не берёт самокат
            b=K-a
        else:
            b=K-a#то, сколько осталось от самоката (сколько он может ещё проехать на предыдущем самокате)
            n+=1 #он взял самокат
print(n)
