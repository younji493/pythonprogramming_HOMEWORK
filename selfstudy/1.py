# inFp = None          # 입력 파일 (파일을 안 쓰므로 주석 처리)
inStr = ""             # 읽어 온 문자열
lines = [              # 원래 파일 내용 대신 리스트로 정의
    "CookBook 파이썬을 공부합니다.\n",
    "완전 재미있어요. ^^\n",
    "파이썬을 공부하기 잘했네요~~\n"
]

i = 0                  # 인덱스용 변수
lineNum = 1            # 줄 번호

while True:
    if i >= len(lines):    # 더 이상 읽을 줄이 없으면 종료
        break
    inStr = lines[i]
    print("%d: %s" % (lineNum, inStr), end = "")
    i += 1
    lineNum += 1

# 파일을 열지 않았기 때문에 inFp.close()는 필요 없음