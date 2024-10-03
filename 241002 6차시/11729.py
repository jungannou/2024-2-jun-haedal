N=int(input())
K=0
moves=[]
def hanoi (num,source,auxiliary,target):
    global K,moves # K와 moves가 def 안에서는 정의되지 않았으므로, 외부의 것을 def 안으로 데리고 온다.
    if num==1:
        K=K+1 # 이동휫수 +1
        moves.append((source,target)) #바로 움직이면 되니깐.
        return
    else:
        hanoi(num-1,source,target,auxiliary)
        moves.append((source,target)) #맨 밑에 거를 source에서 target으로 실제로 움직임.
        K=K+1 # 이동휫수 +1
        hanoi(num-1,auxiliary,source,target)

hanoi (N,1,2,3)
print(K)
for i in moves:
    print(i[0],i[1],sep=' ')