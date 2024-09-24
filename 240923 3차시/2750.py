N=int(input())
empty=[]
for i in range(N):
    num=int(input())
    empty.append(num)

empty.sort()
for i in range(N):
    print(empty[i])