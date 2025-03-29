expr, answer = "", 0
result = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계 :"))

if result == 1:
    expr = input("*** 수식을 입력하세요 : ")
    answer = eval(expr)
    print("%s 결과는 %f입니다."%(expr, answer))

elif result == 2:
    a = int(input("첫 번째 숫자를 입력하세요: "))
    b = int(input("두 번째 숫자를 입력하세요: "))
    total = 0

    for i in range(a, b+1):
        total += i

    print("%d + ... + %d는 %d입니다."%(a, b, total))

else:
    print("1 또는 2 숫자만 입력하십시오.")