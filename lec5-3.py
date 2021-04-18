# 파라메트릭 서치 - Parametric Search
# 최적화 문제를 결정 문제 ("예" 혹은 "아니오")로 바꾸어 해결하는 기법
# 예시 : 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제

# 연습문제 - 정렬된 배열에서 특정 수의 개수 구하기
# 수열에서 x가 등장하는 횟수 구하시오

from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index - left_index

n, x = map(int, input().split(' '))
array = list(map(int, input().split(' ')))

count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)