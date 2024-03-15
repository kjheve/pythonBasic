print('hi')


# 제곱 함수
def square(x):
    return x ** 2

# 리스트 정의
numbers = [1, 2, 3, 4, 5]

# map() 함수를 사용하여 제곱 계산
squared_numbers = map(square, numbers)

# 결과 출력
print(list(squared_numbers))  # [1, 4, 9, 16, 25]