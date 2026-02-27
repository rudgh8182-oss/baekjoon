S, B = map(int, input().split())

step = [-1, 1, 2]

min_cnt = 10000
cnt = 0
def dfs(S):
    global cnt
    if S == B:
        if min_cnt > cnt:
            min_cnt = cnt
            cnt = 0
        return
 
    for i in range(3):
        if i == 2:
            if S * 2 < B * 2:
                S = S * step[i]
                cnt += 1
                dfs(S)
                S = S // step[i]
            
        else:
            S = S + step[i]
            cnt += 1
            dfs(S)
            S = S - step[i]

dfs(0)
print(min_cnt)