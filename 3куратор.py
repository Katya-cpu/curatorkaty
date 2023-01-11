from itertools import *
k=0
for x in product('САШУЛ','САШУЛЯ','САШУЛЯ','САШУЛЯ','САШУЛЯ','САШУЛЯ','САШУЛЯ'):
    s=''.join(x)
    if s.count('С')==1 and s.count('Я')==1:
        k+=1
print(k)
    
