# Q)
# 이름, 나이, 국어점수, 영어점수를 데이터로 갖는 student 딕셔너리를 만드시오.
# 각 데이터는 키보드로 입력받아 저장하고, 저장된 데이터를 출력하시오
name = input("이름 : ")
age = int(input("나이 : "))
korean_score = int(input("국어점수 : "))
english_score = int(input("영어점수 : "))

student = {
    "이름": name,
    "나이": age,
    "국어점수": korean_score,
    "영어점수": english_score
}
print(student)


# ----------------------------------------------------------------

# Q)
# 위의 문제에서 만든 딕셔너리 데이터에 총점 데이터를 추가하시오.
# 총점 데이터는 국어, 영어 점수의 합으로 들어가야 합니다.

# list = list(student.values())
# student['합계점수'] = list[2] + list[3]
# print(student)

student['합계점수'] = int(student['국어점수']) + int(student['영어점수'])
print(student)


# # ------------------------------------------------------
# # 국어점수와 영어점수만을 선택하여 합산하는 함수 (reduce사용)
# from functools import reduce
# def calculate_total(total, key):
#     if key in ['국어점수', '영어점수']:
#         return total + student[key]
#     return total
#
# # reduce 함수를 사용하여 총점 계산
# total_score = reduce(calculate_total, student.keys(), 0)
#
# # 총점을 딕셔너리에 추가
# student['합계점수'] = total_score
#
# # 결과 출력
# print(student)
