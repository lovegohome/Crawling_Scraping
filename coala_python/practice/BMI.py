print("BMI 계산기 입니다.")
h = int(input("신장: "))
w = int(input("몸무게: "))

BMI = (w / (h*h))*10000


print("BMI: %.2f" %BMI)
print("BMI: ", BMI)