#너무 어려워서 ㅠㅠㅠㅠ 챗GPT한테 물어보고, 해설이라도 최대한 자세하게 썼습니다!

def detect_yesorno(s,t): # s와 t를 넣었을 때, 문제의 조건에 맞게 출력하는 함수 생성
    s_idx=0
    t_idx=0 #s와 t 문자열에서의 인덱스 변수를 생성함.

    while s_idx < len(s) and t_idx < len(t): #부트캠프 노션에 없어서 따로 찾아 봤습니다!
        # 이 함수는 while 뒤의 조건을 만족할 때 계속 작동하네요.
        # 여기서 len(s) 앞에 부등호가 붙은 이유는 len(s)는 1 index, 문자열 접근은 0 index여서 입니다!
        if s[s_idx]==t[t_idx]:
            s_idx+=1  #s_idx=0, t_idx=0일때 부터 탐색. s[0] in t의 경우, s_idx는 1 올라갑니다.
        t_idx+=1 # 예를 들어, s[4]==t[7]의 경우, s_idx는 5로 올라가고, t_idx는 8로 올라갑니다. 그 이후엔, s[5], t[8]부터의 문자열만 탐색합니다.
                 # s[0] not in t의 경우, s_idx=0, t_idx=len(t)-1 탐색 후,
                 # s_idx는 0으로 남아있지만, t_idx==len(t)가 되므로, while 반복문을 나가게 됩니다.

    if s_idx==len(s):
        print("Yes") # 만약에 s의 모든 문자가 순서대로 t에 담겨 있다면, s_idx는 len(s)의 값과 동일하게 될 것입니다.
                     # 왜냐하면 s[0]이 t에 있으면, s_idx의 값은 1이 되므로, 쭉쭉 올라가서, s[len(s)-1]이 t에 있으면, s_idx는 len(s)이 됩니다.
    else:
        print("No") # 아니라면, t에도 순서대로 있는, s의 문자들 중 마지막 문자의 인덱스 값+1이 s_idx로 남아있으므로, len(s)보다 작을 것입니다.
                    # 사실, s_idx==len(s)의 경우에도, s의 마지막 문자도 t에 순서대로 포함되기에, (s의 마지막 문자 인덱스 값)+1=(len(s)-1)+1이 s_idx로 남아있네요.
                    # s의 문자들 중 아무것도 t에 없으면 s_idx는 0.

try:
    while True:
        s, t=map(str,input().split())
        detect_yesorno(s,t) #함수 호출

except EOFError:
    pass # 문자열+스페이스+문자열 이런 식의 입력만 받은 후 Yes 또는 No를 출력해야 하는데
         # 더 이상의 input이 없을 때 발생하는 에러인 EOFError의 경우, pass로 예외 처리 했습니다! 끄읕~