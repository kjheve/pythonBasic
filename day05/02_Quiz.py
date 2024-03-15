# 키보드로 세 문자열을 입력받고, 입력받은 세 문자열을 리스트에 저장하시오.
# 그 후 리스트에 저장된 문자열 중 가장 긴 문자열과 가장 짧은 문자열의 글자 수 차이를 출력하시오.

print("== 3개의 문자열을 입력 받습니다. ==")
str1 = input("문자열1 입력 : ")
str2 = input("문자열2 입력 : ")
str3 = input("문자열3 입력 : ")
print("="*20)

list = []
list.append(str1)
list.append(str2)
list.append(str3)

print(f'문자열 확인 : {list[0]}, {list[1]}, {list[2]}')
print(f'문자열 길이 : {len(list[0])}, {len(list[1])}, {len(list[2])}')

longStr = len(list[0])
shortStr = len(list[0])
# print(type(longStr)) # type : int

if longStr < len(list[1]):
    longStr = len(list[1])
if longStr < len(list[2]):
    longStr = len(list[2])

if shortStr > len(list[1]):
    shortStr = len(list[1])
if shortStr > len(list[2]):
    shortStr = len(list[2])

print("="*20)
print(f'가장 긴 문자열 길이 : {longStr}')
print(f'가장 짧은 문자열 길이 : {shortStr}')

print(f'=> 문자열 글자 수 차이 {longStr-shortStr}')



