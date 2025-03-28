result = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계 :"))

def sigma(a, b):
    sum = 0
    for i in range(a, b+1):
        sum += i
    return sum


if result == 1:
    print("*** 수식을 입력하세요 : ")

else:
    a = int(input("첫 번째 숫자를 입력하세요 : "))
    b = int(input("두 번째 숫자를 입력하세요 : "))
    total = sigma(a, b)
    print("%d + ... + %d는 %d입니다."%(a, b, total))