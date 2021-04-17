# 재귀함수
# 재귀함수의 종료조건을 반드시 명시

# 팩토리얼 구현 예제

def factorial_recursive(n):
  if n <= 1:
    return 1
  
  return n * factorial_recursive(n-1)

print("재귀적으로 구현: ", factorial_recursive(5))
