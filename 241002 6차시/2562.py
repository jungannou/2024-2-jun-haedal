list=[]
pick=0

for i in range (9):
    a=int(input())
    list.append(a)

for i in range (9):
    if list[i]==max(list):
        pick=i+1

print(max(list))
print(pick)