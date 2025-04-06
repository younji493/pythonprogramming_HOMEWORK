for dan in range(2, 10):
    print("# " + str(dan) + "단 #", end='\t')
print()

for i in range(1, 10):
    for dan in range(2, 10):
        result = dan * i
        if result < 10:
            print(str(dan) + "X " + str(i) + "= " + str(result), end='\t')
        else:
            print(str(dan) + "X " + str(i) + "=" + str(result), end='\t')
    print()
