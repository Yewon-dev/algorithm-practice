# 연습 문제 (떡볶이 떡 만들기)
# 떡 절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단.
# 높이가 H보다 긴 떡은 H 위의 부분이 잘림
# 손님은 잘린 부분의 떡을 가져감
# 손님이 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램

n, m = map(int, input().split(' '))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while(start <= end):
    total = 0
    mid = (start + end)/2
    for x in array:
        if x > mid:
            total += x - mid
    
    if total > m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)