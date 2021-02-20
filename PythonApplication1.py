from random import randint
n=int(input())
i=0
b = [0]*n
used =[]
while i < n:
    q=randint(1,n+10)
    if q in used:
        continue
    else:
        used.append(q)
    a=list([randint(10,100) for i in range(q)])
    if i % 2 == 0:
        a.sort()
    else:
        a.sort(reverse=True)
    b[i] = a
    i+=1
for j in range(n):
    print(b[j])
