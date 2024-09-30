a,b,c=map(int,input().split())

if a==b and b==c:
    print(10000+1000*a)

elif a!=b and b!=c and c!=a:
    print(100*max(a,b,c))

else:
    if a==b:
        print(1000+100*a)
    elif b==c:
        print(1000+100*b)
    else:
        print(1000+100*c)