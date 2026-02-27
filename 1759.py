L, C = map(int, input().split())
word = list(input().split())
word.sort()

visited = [0] * L

def dfs(r, start):
    if r == L:
        cnt = 0
        for j in range(L):
            if visited[j] in ['a', 'e', 'i', 'o', 'u']:
                cnt += 1
        if 1<= cnt <= L-2:
            print(''.join(visited))
        return
    
    for i in range(start, C):
        visited[r] = word[i]

        dfs(r + 1, i + 1)

        visited[r] = word[i]

dfs(0, 0)