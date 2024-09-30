hour, minute=map(int,input().split(' '))
time=int(input())
if minute+time<60:
    print(hour, minute+time,sep=' ')
elif hour+(minute+time)//60>23:
    print((hour+(minute+time)//60)%24,(minute+time)%60,sep=' ')
else:
    print(hour+(minute+time)//60,(minute+time)%60,sep=' ')