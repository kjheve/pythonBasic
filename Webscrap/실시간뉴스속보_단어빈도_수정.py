# 수정전 버전은 수집+단어빈도 시각화
# 수정된건 단어빈도 시각화만

# 정규표현식
import re
import pandas as pd
import matplotlib.pyplot as plt


# 자연어 처리 라이브러리
from konlpy.tag import Okt    # 형태소 분석
from nltk.probability import FreqDist  # 빈도 분석

# 형태소 분석기 초기화
okt = Okt()

# 한국어 불용어 리스트 (필요에 따라 추가)
stopwords = ['이것은', '또', '다른', '입니다', '...', '이', '가', '를', '에', '최고', '을', '(', ')', '은', '의', '·', "'", '…', '는', '하고', '있다', ']', '[']

# 텍스트 전처리 및 형태소 분석 함수
def preprocess_text(text):
    # 한글([가-힣]과 공백(\s)을 제외하고 모두 제거
    text = re.sub(r'[^가-힣]\s', '', text) # 정규 표현식 사용
    # 형태소 분석
    tokens = okt.morphs(text)
    # 불용어 제거 : 형태소 분석된 단어 목록을 가져와서 불용어 단어는 제거
    tokens = [ word for word in tokens if word not in stopwords ]
    return tokens


# 읽어오기
df = pd.read_excel('실시간뉴스속보2.xlsx')


# 제목, 요약문 텍스트 전처리 및 형태소 분석
tokens = df['제목'].apply(preprocess_text) + df['요약'].apply(preprocess_text)
tokens = [ item for sublist in tokens for item in sublist ]
print(tokens)
print(len(tokens))

# 단어빈도 분석
fdist = FreqDist(tokens) # 빈도 계산해주는 객체 FreqDist()
print(fdist.most_common(10)) # 빈도 높은 단어 10개 출력


# 시각화

# 한글 폰트설정
plt.rc("font", family='Malgun Gothic')
# 마이너스폰트 설정
plt.rc("axes", unicode_minus=False)

common_words = fdist.most_common(10)
words = [ word[0] for word in common_words ] # 단어
counts = [ word[1] for word in common_words ] # 빈도

plt.figure(figsize=(10, 8))
plt.bar(words, counts)
plt.xlabel('단어')
plt.ylabel('빈도')
plt.title('단어 빈도수 시각화')
plt.xticks(rotation=45)
plt.show()

