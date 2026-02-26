T = int(input())

for _ in range(T):
    arr = [list(map(int, input().split())) for _ in range(11)]
    visited = [0] * 11
    
    max_v = 0
    
    def dfs(r):
        global max_v
        if r == 11:
            total = sum(visited)
            if max_v < total:
                max_v = total
            return
        
        for c in range(11):
            if visited[c] == 0:
                if arr[r][c] > 0:
                    visited[c] = arr[r][c]
                
                    dfs(r + 1)

                    visited[c] = 0
    
    dfs(0)

    print(max_v)