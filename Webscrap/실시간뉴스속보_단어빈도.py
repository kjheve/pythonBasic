# %%
"""
## Request로 웹페이지 정보 긁어오기
"""
import matplotlib.pyplot as plt
# %%
# http 요청, 응답 수행
import requests
# html문서 파싱 (DOM요소 다루듯 접근하는 기능 제공)
from bs4 import BeautifulSoup

# 정규표현식
import re

import pandas as pd
import pyautogui
import time

# 자연어 처리 라이브러리
from konlpy.tag import Okt    # 형태소 분석
from nltk.probability import FreqDist  # 빈도 분석

# 형태소 분석기 초기화
okt = Okt()

# 한국어 불용어 리스트 (필요에 따라 추가)
stopwords = ['이것은', '또', '다른', '입니다', '...', '이', '가', '를', '에', '최고', '을', '(', ')', '은', '의', '·', "'", '…', '는', '하고', '있다']

# 텍스트 전처리 및 형태소 분석 함수
def preprocess_text(text):
    # 한글([가-힣]과 공백(\s)을 제외하고 모두 제거
    text = re.sub(r'[^가-힣]\s', '', text) # 정규 표현식 사용
    # 형태소 분석
    tokens = okt.morphs(text)
    # 불용어 제거 : 형태소 분석된 단어 목록을 가져와서 불용어 단어는 제거
    tokens = [ word for word in tokens if word not in stopwords ]
    return tokens

req_page = int(pyautogui.prompt('몇 페이지를 읽어올까요?'))

df = pd.DataFrame()
for page in range(1, req_page+1):

    # http 요청
    url=(
        f'https://finance.naver.com/news/news_list.naver?'
        f'mode=LSS2D&section_id=101&section_id2=258&page={page}'
    )
    # print(url)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    params = {}
    res = requests.get(url, headers=headers, params=params)
    res.raise_for_status() # 문제가 생겼을 때 오류를 내뱉고 프로그램 종료
    # print(res.status_code)

    # BeautifulSoup으로 불러온 url 파싱
    html = BeautifulSoup(res.text, 'html.parser')

    # 뉴스 리스트만 선택해서 list로
    news_list = html.select_one('#contentarea_left > ul')


    articleSubject_list = news_list.select('.articleSubject')
    articleSummary_list = news_list.select('.articleSummary')

    # 제목 목록 가져오기 -------------------------------------------------
    news_subjects = [ subject.text.strip() for subject in articleSubject_list ]
    # 링크 목록 가져오기 -------------------------------------------------
    news_home_url = 'https://finance.naver.com'
    news_links = [f"{news_home_url}{subject.select_one('a')['href']}" for subject in articleSubject_list]
    # 요약문
    summary_texts = [''.join([element.strip() for element in summary.contents if isinstance(element, str)]) for summary in articleSummary_list]
    # 언론사 -------------------------------------------------
    media_companies = [ subject.select_one('.press').text for subject in articleSummary_list ]
    # 작성일시 -------------------------------------------------
    news_cdates = [ subject.select_one('.wdate').text for subject in articleSummary_list ]

    # zip()함수를 사용해서 여러 리스트의 요소를 묶기
    zipped_lists = zip(news_subjects, news_links, summary_texts, media_companies, news_cdates)
    result_list = list(zipped_lists)


    # 데이터 프레임
    col_name = ['제목', 'URL', '요약', '언론사', '작성일시']
    df_tmp = pd.DataFrame(result_list, columns=col_name)

    # 데이터 프레임 추가
    # df.apeend(df_tmp, index=False)
    df = pd.concat([df, df_tmp], ignore_index=True)
    # df = pd.concat([df, df_tmp])

    # 지연 시간 주기 2초
    time.sleep(2)





# %%
# 저장하기
# df.to_excel(f'실시간뉴스속보{req_page}.xlsx', index=False)
# df.to_csv(f'실시간뉴스속보{req_page}.csv', index=False, encoding='utf-8-sig')


# 제목, 요약문 텍스트 전처리 및 형태소 분석
tokens = df['제목'].apply(preprocess_text) + df['요약'].apply(preprocess_text)
tokens = [ item for sublist in tokens for item in sublist ]
print(tokens)
print(len(tokens))

# 단어빈도 분석
fdist = FreqDist(tokens) # 빈도 계산해주는 객체 FreqDist()
print(fdist.most_common(10)) # 빈도 높은 단어 10개 출력


# 시각화
import matplotlib.pyplot as plt

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

