# 연습 문제 (효율적인 화폐 구성)
# N가지 종류의 화폐가 있음.
# 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 함.

n, m = map(int, input().split())

# n개의 화폐 단위 정보 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1) # m원까지 결과를 구하기 위해


# 다이나믹 프로그래밍 (보텀업)
d[0] = 0
for i in range(n): # i : 각각의 화폐 단위
    for j in range(array[i], m + 1): # j : 금액 # 화폐단위원부터 m원까지 확인
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우 == 금액에서 화폐단위를 뺄 수 있다면
            d[j] = min(d[j], d[j - array[i]] + 1)


if d[m] == 10001:
    print(-1)
else:
    print(d[m])
    