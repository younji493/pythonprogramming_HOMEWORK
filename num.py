jinsu = int(input("입력 진수 결정(16/10/8/2) : "))

input_data = input("값 입력 : ")

# 입력받은 값을 10진수로 바꾸기
number = int(input_data, jinsu)

# 각각의 진수로 출력해 보기
print("16진수 ==> ", hex(number))
print("10진수 ==> ", number)
print("8진수 ==> ", oct(number))
print("2진수 ==> ", bin(number))