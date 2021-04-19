# 연습 문제 (개미전사)
# 개미전사는 식량창고를 공격하여 식량을 얻으려고 함
# 각 식량찬고에는 정해진 수의 식량을 저장하고 있으며
# 개미 전사는 선택적으로 식량창고를 약탈할 예정임
# 모든 식량창고는 일직선상에 존재하며 식량창고 중에서 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있음
# 따라서 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 함

n = int(input())
k = list(map(int, input().split(' ')))

d = [0] * 100

d[0] = k[0]
d[1] = max(k[0], k[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + k[i])

print(d[n-1])
        
    
    