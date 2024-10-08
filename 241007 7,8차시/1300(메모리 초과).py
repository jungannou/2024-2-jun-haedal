N=int(input())
k=int(input())

A = [[0] * N for _ in range(N)]
# 2차원 배열 어떻게 만드는지 몰라서 이것만 챗GPT 돌렸습니다ㅠㅠㅠ

for i in range(1,N+1):
    for j in range(1,N+1):
        A[i-1][j-1]=i*j

B=[]

for i in range(0,N):
    for j in range(0,N):
        B.append(A[i][j])

B.sort()
print(B[k-1])

#메모리 초과 문제 때문에 다른 방법도 찾아보겠습니당 ㅠㅠㅠ