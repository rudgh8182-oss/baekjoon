from collections import deque

arr = [list(input()) for _ in range(5)]
ans = 0

# 3단계: 뽑힌 7자리가 서로 연결되어 있는지 확인하는 BFS
def check_connection(selected):
    # 첫 번째로 뽑힌 좌표를 시작점으로 설정
    start_idx = selected[0]
    r, c = start_idx // 5, start_idx % 5
    
    q = deque([(r, c)])
    visited = set([(r, c)])
    connected_count = 1
    
    # 빠른 탐색을 위해 1차원 인덱스 리스트를 2차원 좌표 set으로 변환
    selected_set = set([(idx // 5, idx % 5) for idx in selected])
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            
            # 다음 좌표가 우리가 뽑은 7자리(selected_set) 안에 있고, 아직 방문하지 않았다면
            if (nr, nc) in selected_set and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc))
                connected_count += 1
                
    # 7개가 모두 연결되어 방문되었다면 True
    return connected_count == 7

# 1, 2단계: 25자리 중 7자리 뽑기 (백트래킹 직접 구현)
def dfs(idx, s_cnt, selected):
    global ans
    
    # 가지치기 (선택 옵션): 남은 자리를 다 'S'로 채워도 4명이 안 되면 탐색 중단
    if s_cnt + (7 - len(selected)) < 4:
        return
        
    # 기저 조건: 7자리를 모두 뽑았을 때
    if len(selected) == 7:
        # 이다솜파(S)가 4명 이상인지 확인 (가지치기로 이미 걸러지지만 명시적으로 작성)
        if s_cnt >= 4:
            # 7자리가 서로 다 연결되어 있는지 최종 확인
            if check_connection(selected):
                ans += 1
        return
        
    # idx부터 24번 자리까지 탐색하며 조합을 만듦
    for i in range(idx, 25):
        r, c = i // 5, i % 5
        is_s = 1 if arr[r][c] == 'S' else 0
        
        # 다음 자리를 뽑고, 인덱스를 i+1로 넘겨 중복 방지 (조합의 핵심)
        selected.append(i)
        dfs(i + 1, s_cnt + is_s, selected)
        selected.pop() # 백트래킹 (원상 복구)

# 0번 인덱스부터 탐색 시작, S의 개수 0, 뽑힌 자리 리스트 빈 배열
dfs(0, 0, [])

print(ans)