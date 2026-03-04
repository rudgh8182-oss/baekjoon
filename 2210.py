dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c, num):

    if len(num) == 6:
        result.add(num)
        return 
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, num + arr[nr][nc])
            

arr = [list(input().split()) for _ in range(5)]

result = set()

for r in range(5):
    for c in range(5):
        dfs(r, c, arr[r][c])
        

print(len(result))