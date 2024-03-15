# 매개변수로 두 개의 리스트를 받아,
# 두 개의 리스트에 저장된 모든 데이터의 평균을 리턴하는 함수를 작성하시오

def sumList(ls1, ls2):
    sumlist = []
    sumlist.extend(ls1)
    sumlist.extend(ls2)
    # sumlist = ls1 + ls2
    return sum(sumlist) / len(sumlist)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print(sumList(list1, list2))
