n=int(input())
m=int(input())

close_friend = set()
friendships=[]
all_list=set()

for i in range (m):
    a,b=map(int,input().split())
    friendships.append((a,b)) #list에 set type도 추가할 수 있네요.

for (c,d) in friendships:
    if c==1:
        close_friend.add(d)

for (e,f) in friendships:
    if e in close_friend:
        all_list.add(f)
    if f in close_friend:
        all_list.add(e)

all_list.update(close_friend) #.add를 쓰니 안 돼서, update를 썼습니다!

if 1 in all_list:
    all_list.remove(1) # close_friend 리스트에 하나라도 추가된다면, line 16 : for (e,f) in friendships:에서 본인인 1도 추가되므로 빼야함.

print(len(all_list))