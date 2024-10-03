def sosu(a):
    if a==2:
        return True
    if a>2:
        for i in range (2,a):
            if a%i==0:
                return False
        return True
# 소수 판별 함수

M = int(input())
N = int(input())
list=[]

for i in range(M, N + 1):
    if sosu(i)==True:
        list.append(i)

if not list: # list가 비어있다면
    print(-1)
else:
    print(sum(list))
    print(list[0])