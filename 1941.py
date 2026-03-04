from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(r, c, prin):
    global cnt
    
            
    Q = deque()
    Q.append((r, c, prin))

    while Q:
        r, c, prin = Q.popleft()

        if len(prin) == 7:
            if prin.count('S') >= 4:
                cnt += 1
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 5 and 0 <= nc < 5:
                Q.append((nr, nc, prin + arr[nr][nc]))

        





arr = [list(input()) for _ in range(5)]

cnt = 0
visited = [[0] * 5 for _ in range(5)]

for r in range(5):
    for c in range(5):
        bfs(r, c, arr[r][c])
        
print(cnt)