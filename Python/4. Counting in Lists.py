ls = []
i = 0
want = int(input("Please enter the desired value: "))
want_Occurrences = 0
while i < 10:
    i += 1
    value = int(input("Please enter the " + str(i) + "th number in the list: "))
    ls.append(value)
for s in range(len(ls)):
    if want == ls[s]:
        want_Occurrences += 1 
print(want_Occurrences) 
