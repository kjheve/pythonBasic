import json
import sys

# 예외 만들기 (저장 -> 이미등록된단어)
class overlapWord(Exception):
    def __str__(self):  #toString()
        return "[실패] 이미 등록된 단어 입니다."

# 단어 class
class Word:
    # 생성자
    def __init__(self):
        try:
            self.words = self.readOnFile()
        except FileNotFoundError as e:
            print("dictionary.json 파일이 존재하지 않습니다.", e)
            print("프로그램을 종료합니다.")
            sys.exit(1)
        except Exception as e:
            print("파일 내 빈 딕셔너리 '{}'이(가) 작성되어야 합니다.", e)
            print("프로그램을 종료 합니다")
            sys.exit(1)
        # self.words = {'student': '학생',
        #               'teacher': '선생님',
        #               'classroom': '교실',
        #               'smart': '영리한'
        #               }

    # json파일을 딕셔너리로 불러오기
    def readOnFile(self):
        with open('dictionary.json', mode='r', encoding='utf-8') as f:
            return json.load(f)

    # words를 json파일로 저장
    def saveOnFile(self):
        with open('dictionary.json', mode='w', encoding='utf-8') as f:
            json.dump(self.words, f, ensure_ascii=False, indent=4)

    # 저장
    def saveWord(self):
        # 1. 단어장 5개 체크
        if len(self.words) >= 5:
            print("[실패] 최대 5개 단어만 저장할 수 있습니다.")
            return
        # 2. 단어장 추가
        word = input("단어를 입력 : ").lower()
        try:
            if word in self.words.keys():   # 중복 단어 체크
                raise overlapWord
            mean = input("의미를 입력 : ")
            self.words[word] = mean  # words 딕셔너리 추가 처리
            self.saveOnFile() # json 저장
        except overlapWord as e:
            print(e)

    # 검색
    def searchWord(self):
        search = input("검색할 단어를 입력 : ").lower()
        found = False  # 검색 플래그
        for word, mean in self.words.items():
            if word.lower().startswith(search.lower()):
                print(f'{word}의 뜻은 {mean} 입니다. ({search}를 입력함)')
                found = True
        if not found:
            print("[실패] 단어를 찾을 수 없습니다")

    # 수정 (단어 뜻)
    def editWord(self):
        edit = input("수정할 단어를 입력 : ").lower()
        if edit in self.words:
            editMean = input("바꿀 의미 입력 : ")
            self.words[edit] = editMean # 수정 처리
            self.saveOnFile()  # json 저장
            print("[성공] 수정 완료")
        else:
            print("[실패] 단어장에 없는 단어")

    # 삭제
    def delWord(self):
        delete = input("삭제할 단어를 입력 : ").lower()
        if delete in self.words:
            del self.words[delete] # 삭제 처리
            self.saveOnFile()  # json 저장
            print("[성공] 삭제 완료")
        else:
            print("[실패] 단어장에 없는 단어")

    # 목록
    def listWord(self):
        # 1. 단어장 갯수 0개
        if (len(self.words) == 0):
            print("[실패] 단어장의 갯수가 0개")
            return
        # 2. 정렬
        orderby = input("정렬 순서를 선택([1]ASC [2]DESC) : ")
        if orderby == '1':
            print("=]:> 단어장 출력(오름차순) <:[=")
            sortWords = sorted(self.words.items())
        elif orderby == '2':
            print("=]:> 단어장 출력(내림차순) <:[=")
            sortWords = sorted(self.words.items(), reverse=True)
        else:
            print("[경고] 올바른 메뉴를 선택바람!")
            return
        # 3. 단어 출력
        i = 1
        for word, mean in sortWords:
            print(f' [{i}] {word:<10} : {mean}')
            i += 1
        print()

    # 통계
    def statsWord(self):
        # 1. 저장 된 단어의 갯수
        count = len(self.words)
        print(f'저장 된 단어의 갯수 : {count}')
        if (len(self.words) == 0):
            print("[실패] 단어장의 갯수가 0개라 메인으로 되돌아 갑니다")
            return
        # 2. 단어의 문자수가 가장 많은 단어
        longWord = max(self.words, key=len)
        print(f'가장 긴 단어 : {longWord}, 글자 수 : {len(longWord)}')
        # 3. 단어 글자수 내림차순 출력(단어만)
        sortWords = sorted(self.words.keys(), key=len,reverse=True)
        print("--단어 길이 내림차순 정렬--")
        for word in sortWords:
            print(word, end=" ")
        print()


# main 시작
dictionary = Word()
stop = False
while (not stop):
    try:
        print('==== 영어 단어장 프로그램 ====')
        print('[1]저장 [2]검색 [3]수정 [4]삭제\n[5]목록 [6]통계 [7]종료')
        print("=" * 30)
        menu = int(input("메뉴를 선택 : "))
        if menu < 1 or menu > 7:
            print("[경고] 메뉴 선택시 1 ~ 7사이 숫자를 입력 바람")
        match menu:
            case 1:
                # print("저장")
                dictionary.saveWord()
            case 2:
                # print("검색")
                dictionary.searchWord()
            case 3:
                # print("수정")
                dictionary.editWord()
            case 4:
                # print("삭제")
                dictionary.delWord()
            case 5:
                # print("목록")
                dictionary.listWord()
            case 6:
                # print("통계")
                dictionary.statsWord()
            case 7:
                # print("종료")
                stop = True
    except Exception as e:
        print(f'[경고] 올바른 메뉴를 선택 해 주세요\n에러메세지 : {e}')

# 종료시 문구
print()
print("######   ##  ##   ####")
print("##       ### ##   ## ##")
print("##       ######   ##  ##")
print("####     ######   ##  ##")
print("##       ## ###   ##  ##")
print("##       ##  ##   ## ##")
print("######   ##  ##   ####")
print('[system] dictionary.json에 저장됨')