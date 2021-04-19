# 연습 문제 (병사 배치하기)
# N명의 병사가 무작위로 나열되어 있다.
# 각 병사는 특정한 값의 전투력을 보유하고 있다
# 병사를 배치할 때 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치
# 배치과정에서 특정한 위치에 있는 병사를 열외시키는 방법 이용
# 그러면서 남아있는 병사의 수가 최대

# 큰 -> 작 순서가 아니라 작 -> 큰 순서로 생각해서 
# 가장 긴 증가하는 부분 수열 (LIS) 알고리즘 적용

# D[i] : array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 점화식 : 모든 0 <= j < i에 대하여, D[i] = max(D[i], D[j] + 1)
#                                     if array[j] < array[i]


n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 LIS 알고리즘 이용
array.reverse()

# 다이나믹 프로그래밍을 위함 1차원 dp 테이블 초기화
d = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            d[i] = max(d[i], d[j] + 1)

# 열외해야 하는 병사의 최소 수를 출력
print(n - max(d))