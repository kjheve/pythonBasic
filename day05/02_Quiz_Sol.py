# max() 와 min() 함수로 간단히

str1 = input('문자열1 : ')
str2 = input('문자열2 : ')
str3 = input('문자열3 : ')

strs = [len(str1), len(str2), len(str3)]

print(f'문자열 글자 수 차이 = {abs(max(strs)-min(strs))}')

