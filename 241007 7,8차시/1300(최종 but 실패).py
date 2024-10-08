# 2차원 배열을 직접 만들지 말고, B[k]보다 작은 게 몇 개인지를
# 확인하는 이진탐색법을 써보라는 GPT의 도움을 받았습니다..ㅠ
N=int(input())
k=int(input())

import math #소수점 이하 올림 함수 호출을 위해

def how_many_smaller(n,N): # 배열 A[N*N]에서, n보다 작은 자연수가 몇 개인지 알려주는 함수
    num=0 #n보다 작은 자연수의 개수
    for i in range(1,N+1): # A[N*N]에서, A[1],A[2], .... 를 차례대로 조사함.
        if i>=n:
            break

        elif n>N:  # 이 조건의 경우, 예를 들어, n,N=6,3일 때, A[1]=[1,2,3]인데, n/i를 조사할 때, 3/1까지만 조사해야하지, 6/1까지 조사하면 안 된다.
            if N*i>=n: # 위의 예시 그대로, A[2]=[2,4,6]인 경우, n/i를 조사할 때, 마지막 항이 6(n값)이상이므로, 다 조사해도 된다.
                num=num+math.ceil(n/i)-1 # n//i 가 자연수면 당연히 성립. n//i가 자연수가 아니면, n,i=11,2 일 때, math.ceil(11/2)=math.ceil(5.5)=6. 11보다 작은 짝수는 5개이므로 성립.
            if N*i<n:
                num=num+N # A[i]의 마지막 항이 n보다 작으므로, A[i]의 원소 N개 모두 n보다 작다.

        elif n<=N: #이 조건을 만족하면, A[1],A[2],...,A[N]에서 마지막 항이 n보다 크므로, 다 조사해도 된다.
            num=num+math.ceil(n/i)-1

    return num

#how_many_smaller 함수는 정상적으로 잘 작동하는데, 밑에서 뭐가 오류인지 잘 모르겠어요 ㅠㅠㅠ
#만약에 mid가 배열 A[n*n]에 포함되어 있지 않다면 문제가 될 거 같은데,, 잘 모르겠습니다 ㅠㅠㅠㅠㅠㅠ

def binary_search(N,k): #배열 B에서 오름차순 정렬 후, B[k](1-idx)의 값을 찾는 함수.
    start = 1
    end = N*N

    while start < end:
        mid = (start + end) // 2
        count=how_many_smaller(mid,N) #함수 호출 횟수 최소화.

        if count < k: #mid보다 작은 게 k개보다 적다면, B[k] (1-base-idx)는 mid보다 크니까.
            start = mid + 1
        else:
            end = mid

    return start # B[k] (1-b-i) 의 값과 같다.

print(binary_search(N,k))