# inFp = None                           # 파일 안 쓰므로 주석 처리
inList, inStr = [], ""                 # 리스트와 문자열 초기화

# inFp = open("C:/Temp/data1.txt", "r")  # 파일 열기 삭제
# inList = inFp.readlines()              # 대신 리스트 직접 작성
inList = [
    "CookBook 파이썬을 공부합니다.\n",
    "완전 재미있어요. ^^ \n",
    "파이썬을 공부하기 잘했네요~~\n"
]

lineNum = 1                            # 줄 번호 변수

for inStr in inList:
    print("%d: %s" % (lineNum, inStr), end = "")
    lineNum += 1

# inFp.close()                         # 파일 닫기 생략