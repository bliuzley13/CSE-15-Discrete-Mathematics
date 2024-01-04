fin = 0
num1 = int(input("Please enter the first number:"))
num2 = int(input("Please enter the second number:"))
num3 = int(input("Please enter the third number:"))
num4 = int(input("Please enter the fourth number:"))
num5 = int(input("Please enter the fifth number:"))
num6 = int(input("Please enter the sixth number:"))
num7 = int(input("Please enter the seventh number:"))
num8 = int(input("Please enter the eighth number:"))
num9 = int(input("Please enter the ninth number:"))
num10 = int(input("Please enter the tenth number:"))

if (num1 > fin) and (num1 % 2 != 0):
    fin = num1
if (num2 > fin) and (num2 % 2 != 0):
    fin = num2
if (num3 > fin) and (num3 % 2 != 0):
    fin = num3
if (num4 > fin) and (num4 % 2 != 0):
    fin = num4
if (num5 > fin) and (num5 % 2 != 0):
    fin = num5
if (num6 > fin) and (num6 % 2 != 0):
    fin = num6
if (num7 > fin) and (num7 % 2 != 0):
    fin = num7
if (num8 > fin) and (num8 % 2 != 0):
    fin = num8
if (num9 > fin) and (num9 % 2 != 0):
    fin = num9
if (num10 > fin) and (num10 % 2 != 0):
    fin = num10

if (num1 % 2 == 0) and (num2 % 2 == 0) and (num3 % 2 == 0) and (num4 % 2 == 0) and (num5 % 2 == 0) and (num6 % 2 == 0) and (num7 % 2 == 0) and (num8 % 2 == 0) and (num9 % 2 == 0) and (num10 % 2 == 0):
    print("No odd numbers were entered")
else:
    print(fin)