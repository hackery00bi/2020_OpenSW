import trafilatura
import re
from konlpy.tag import Okt

okt = Okt()


def url2sentences(url):  # 데이터를 크롤링하고 문장 단위로 나누어 주는 함수
    downloaded = trafilatura.fetch_url(url)
    result = trafilatura.extract(downloaded)
    web_doclist = result  # 크롤링한 데이터 받아오는 부분 (text density 적용)
    sentences = re.sub('[-=.#/?:$}]', '', web_doclist)  # 정규표현식으로 필요없는 문자 제거
    sentences = sentences.split()  # 문자열을 리스트로 변환
    for idx in range(0, len(sentences)):
        if len(sentences[idx]) <= 10:
            sentences[idx - 1] += (' ' + sentences[idx])
    sentences[idx] = ''
    return sentences


def get_nouns(sentences):  # sentences를 받아 형태소 분석 후 명사만을 추출하는 함수
    nouns = []
    for sentence in sentences:
        if sentence != '':
            nouns.append(' '.join([noun for noun in okt.nouns(str(sentence))
                                   if len(noun) > 1]))
    return nouns


def option1(url, keyword):
    final_list = []
    compare_list = get_nouns(url2sentences(url))
    for word in compare_list:
        if keyword in word:
            final_list.append(compare_list)
            break

    return final_list








