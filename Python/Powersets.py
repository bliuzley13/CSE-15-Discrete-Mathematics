a = set()
while True:
    input_Value = input('Enter one more element: [Y/N] ')
    input_Value.upper()
    if input_Value == "N":
        break
    new_Element = int(input("Enter the new element in the set: "))
    a.add(new_Element)

powerSet = set()
new_Element = list(a)
n = len(new_Element)

for i in range(1<<n):
    current = tuple([new_Element[j] for j in range(n) if(i & (1<<j))])
    powerSet.add(current)

print(powerSet)