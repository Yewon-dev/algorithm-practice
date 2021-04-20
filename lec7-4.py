# 연습문제 (미래도시)
# 1번 회사에서 K번 회사를 방문한 뒤에 X번 회사로 가는 것이 목표
# 플로이드 워셜 알고리즘을 수행한 뒤, (1번 노드에서 X까지의 거리 + X에서 K까지의 최단 거리) 계산

INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[a][b] = 1

x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)