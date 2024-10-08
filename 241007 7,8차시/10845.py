N=int(input())
queue=[]

def push(X):
    queue.append(X)

def pop():
    if not queue:
        print(-1)
    else :
        print(queue.pop(0)) # pop 하는 요소를 출력한 후, queue.pop(0)을 실행.

def size():
    print(len(queue))

def empty():
    if not queue:
        print(1)
    else:
        print(0)

def front():
    if not queue:
        print(-1)
    else:
        print(queue[0])

def back():
    if not queue:
        print(-1)
    else:
        print(queue[-1])

for i in range(N):
    command=input().split()
    if command[0]=='push':
        push(int(command[1]))
    elif command[0]=='pop':
        pop()
    elif command[0]=='size':
        size()
    elif command[0]=='empty':
        empty()
    elif command[0]=='front':
        front()
    elif command[0]=='back':
        back()