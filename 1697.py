# from collections import deque
# S, B = map(int, input().split())

# def bfs(S, B):
#     MAX = 100001
#     visited = [-1] * MAX

#     queue = deque([S])
#     visited[S] = 0

#     while queue:
#         count = queue.popleft()

#         if count == B:
#             return visited[count]
        
#         for i in (count - 1, count + 1, count * 2):
#             if 0 <= i < MAX and visited[i] == -1:
#                 visited[i] = visited[count] + 1
#                 queue.append(i)
        
# print(bfs(S, B))

def bfs(S, B):
    MAX = 100001
    visited = [-1] * MAX

    queue = [S]
    visited[S] = 0

    head = 0

    while queue:
        count = queue[head]
        head += 1

        if count == B:
            return visited[count]
        
        for i in (count - 1, count + 1, count * 2):
            if 0 <= i < MAX and visited[i] == -1:
                visited[i] = visited[count] + 1
                queue.append(i)

S, B = map(int, input().split())
print(bfs(S, B))