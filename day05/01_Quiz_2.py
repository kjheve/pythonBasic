# 키보드로 두 수를 입력받아, 두 수 사이의 모든 정수의 합을 출력하시오.
# 단, 입력받은 두 수는 합에 포함하지 않는다.

print("== 2개의 정수를 입력 받습니다. ==")
num1 = int(input("정수1 입력 : "))
num2 = int(input("정수2 입력 : "))
print("="*20)

min = min(num1, num2)
max = max(num1, num2)

# case 1)
# sum = 0
# for i in range(min+1, max):
#     sum += i

# case 2)
sum = sum(range(min+1, max))

print(f'두 수 사이의 합 : {sum}')


