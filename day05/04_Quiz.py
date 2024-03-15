# 매개변수로 두 개의 리스트를 받아, 첫 번째 매개변수로 받은 리스트에
# 두 번째 리스트의 데이터를 삭제한 리스트를 리턴하는 함수를 만드시오.
# 단, 첫 번째 매개변수로 들어온 리스트가 반드시 두 번째 매개변수로 들어온 리스트보다 데이터의 수가
# 많다고 가정한다.
# 두 매개변수 : [1, 3, 5, 7, 9], [1, 5]  => [3, 7, 9]

list1 = [1, 3, 5, 7, 9]
list2 = [1, 5]

# case 1) append
# result = []
# for i in list1:
#     if i not in list2:
#         result.append(i)
# print(result)

# case 2) remove
# def listMinus(list1, list2):
#     for i in list2:
#         if i in list1:
#             list1.remove(i)
#     return list1
# print(listMinus(list1, list2))

# case 3) 리스트 컴프리헨션
def remove_ele(list1, list2):
    result = [ ele for ele in list1 if ele not in list2 ]
    return result
print(remove_ele(list1, list2))

