# 자바스크립트의 배열 고차함수 vs 파이썬

# 1. forEach --------------------------------------
# const array = [1, 2, 3]
# array.forEach(item => console.log(item))

# case 1) for문
array = [1, 2, 3]
for item in array:
    print(item)
# case 2) 리스트 컴프리헨션
[ print(item) for item in array ]


print("="*30)
# 2. map --------------------------------------
# const array = [1, 2, 3]
# const result = array.map(item => item * item)
# console.log(result) // [1, 4, 9]

array = [1, 2, 3]
# def f(item):
#     return item * item
# result = list(map(f, array))
result = list(map(lambda item : item*item, array))
print(result)