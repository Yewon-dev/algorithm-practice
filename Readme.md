# Ready for Coding-test w/ Python

## 시간 복잡도 계산

- **Big-O Notation**

  | 순위    | 명칭                      |
  | ------- | ------------------------- |
  | 𝑂(1)    | 상수 시간 (Constant time) |
  | 𝑂(㏒𝑁)  | 로그 시간 (Log time)      |
  | 𝑂(𝑁)    | 선형 시간                 |
  | 𝑂(𝑁㏒𝑁) | 로그 선형 시간            |
  | 𝑂(𝑁²)   | 이차 시간                 |
  | 𝑂(𝑁³)   | 삼차 시간                 |
  | 𝑂(2ⁿ)   | 지수 시간                 |

  

## 수행 시간 측정 소스코드

``` python
import time
start_time = time.time() # 측정 시작

## 프로그램 소스 코드

end_time = time.time() 	# 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
```



## 자료형

- **정수형(Integer)** : 양의 정수, 음의 정수, 0
- **실수형(Real Number)** : 소수점 아래의 데이터를 포함하는 수 자료형
- **지수 표현 방식**
  - e나 E 다음에 오는 수는 10의 지수부
  - 1e9 == 10의 9제곱 (1,000,000,000)
