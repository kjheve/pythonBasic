# 자바스크립트의 배열 고차함수 vs 파이썬

# 3. filter --------------------------------------
# const array = [1, 2, 3]
# result = array.filter(item => item % 2 != 0)
# console.log(result)   // [1, 3]

array = [1, 2, 3]
result = list(filter(lambda item : item % 2 != 0, array))
print(result)  # [1, 3]


print("="*30)
# 4. reduce --------------------------------------
# const array = 1, 2, 3[]
# const result = array.reduce((acc, curr) => acc + curr), 0)
# console.log(result)

from functools import reduce
array = [1, 2, 3]
result = reduce(lambda acc, curr : acc + curr, array)
print(f'합 : {result}')

