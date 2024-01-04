num = int(input("Enter an integer to calculate the sum to the given number: "))
result = 0
if num < 0:
    print("This does not start from at least 1.")
for i in range(1, num + 1):
    result = result + i
print(result)