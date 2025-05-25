inFp, outFp = None, None
inStr = ""

srcName = input("소스 파일명을 입력하세요: ")
dstName = input("타깃 파일명을 입력하세요: ")

inFp = open(srcName, "r", encoding="utf-8")
outFp = open(dstName, "w", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()

print(f"--- {srcName} 파일이 {dstName} 파일로 복사되었음 ---")