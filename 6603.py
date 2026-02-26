while True:
    T = list(map(int, input().split()))
    if len(T) == 1:
        break
    
    k = T[0]
    S = T[1:]

    visited = [0] * 6

    def dfs(a, b):
        if a == 6:
           print(*visited)
           return
           
        for j in range(b, len(S)):
            visited[a] = S[j]
    
            dfs(a+1, j+1)

            visited[a] = 0
    
    dfs(0, 0)
    print()