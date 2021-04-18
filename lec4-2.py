# 연습문제 (두 배열의 원고 교체)
# 최대 K 번의 바꿔치기 연산을 수행할 수 있는데,
# 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것
# 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것

# 예를 들어 N = 5, K = 3이고,
# A = [1, 2, 5, 4, 3]
# B = [5, 5, 6, 6, 5]

n, k = map(int, input().split(' '))

A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

A.sort()
B.sort()

for i in range(k):
    if A[i] < B[n - i - 1]:
        A[i], B[n - i - 1] = B[n - i - 1], A[i]
    else:
        break

print(sum(A))    