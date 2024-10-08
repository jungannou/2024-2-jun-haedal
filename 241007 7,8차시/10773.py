K=int(input())
list=[]
for i in range(K):
    a=int(input())
    if a!=0:
        list.append(a)
    if a==0:
        list.pop()

print(sum(list))