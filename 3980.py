T = int(input())

for _ in range(T):
    arr = [list(map(int, input().split())) for _ in range(11)]
    visited = [0] * 11
    
    max_r_v = 0
    
    def dfs(r):
        global max_r_v
        if r == 11:
            total = sum(visited)
            if max_v < total:
                max_v = total
            return
        
        for c in range(11):
            if arr[r][c] > 0:
                visited[r] = arr[r][c]
                
                dfs(r + 1)

                visited[r] = 0
    
    dfs(0)