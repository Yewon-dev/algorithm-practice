# 문제풀이 (미로탈출)
# N x M 크기의 직사각형 형태의 미로가 있음. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 함.
# 현재 위치는 (1, 1)
# 미로의 출구는 (N, M)
# 한 번에 한 칸씩 이동, 괴물이 있는 부분은 0, 없는 부분은 1
# 탈출하기 위한 최소 칸의 개수

from collections import deque

def bfs(x, y):

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 밖의 공간 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1] 

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(map(int, input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))