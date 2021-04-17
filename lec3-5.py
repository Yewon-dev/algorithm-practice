# 문제풀이
# 1. 음료수 얼려먹기
# - N x M 크기의 얼음틀이 있습니다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다. 구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결되어 있는 것으로 간주합니다. 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.

def dfs(x, y):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False

  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    # 해당노드 방문처리
    graph[x][y] = 1
    # 상, 하, 좌, 우 재귀적으로 호출
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  
  return False


n, m = map(int, input().split(' '))

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True: #  방문처리가 되어 있다면
      result += 1

print(result)


