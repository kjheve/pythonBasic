import json

data = {'name' : '홍길동',
        'age' : 30}

#json 형식으로 파일에 저장하기
# with open() as:
# indent : 들여쓰기 옵션

with open('data.json', mode='w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


#json 파일을 읽어와 파이썬 객체로 변환하기
with open('data.json', mode='r', encoding='utf-8') as f:
    data_loaded = json.load(f)

print(data_loaded)
print(type(data_loaded))

#키를 통해 값 읽기
print(data_loaded['name'])
#키를 리스트로 가져오기
data_list = list(data_loaded.keys())
print(data_list)
#값 가져오기 .values()
#엔트리(entry)로 가져오기 .items()

