from execution import execute

how_deep = int(input("URL 얼마나 깊이 볼까 ? : "))
Url = input("URL을 입력하세요 : ")
Keyword = input("아니 시발 도대체 무슨 키워드를 알고싶은건데?? : ")
option = int(input("옵션정보 입력 (1 : 2) : "))

execute(Url, how_deep, Keyword, option)