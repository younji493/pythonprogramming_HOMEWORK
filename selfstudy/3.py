fileName = input("저장할 파일명을 입력하세요 (예: memo.txt): ")

outFp = open(fileName, "w", encoding="utf-8")

while True:
    line = input("내용 입력 (Enter만 누르면 종료): ")
    if line == "":
        break
    outFp.write(line + "\n")

outFp.close()
print(f"--- 정상적으로 파일에 저장되었습니다! ---")