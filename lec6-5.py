# 연습 문제 (금광)
# n x m 크기의 금광이 있음. 각 칸은 특정한 크기의 금이 들어 있음
# 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작함
# m-1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동
# 채굴자가 얻을 수 있는 금의 최대 크기를 구하시오


T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원의 dp 테이블 초기화
    d = []
    index = 0
    for i in range(n):
        d.append(array[index:index + m]) # 열의 크기(m)단위로 슬라이싱
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0: # 첫번째 열일 때
                left_up = 0
            else:
                left_up = d[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1: # 마지막 열일 떄
                left_down = 0
            else:
                left_down = d[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = d[i][j-1]

            d[i][j] = d[i][j]+ max(left, left_down, left_up)
    
    result = 0
    for i in range(n):
        result = max(result, d[i][m-1])
    print(result)
