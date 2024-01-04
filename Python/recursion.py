import sys
sys.setrecursionlimit(100000)

def factorial(n):
    if(n == 1):
        return 1
    else:
        return n * factorial(n - 1)
print("factorial(5):", factorial(5))
# Expected 120

def fib(n):
    if(n <= 1):
        return n
    else:
        return (fib(n - 2) + fib(n - 1))
print("fib(7):", fib(7))
# Expected 13

def equal(A, B):
    i = 0
    if (len(A) != len(B)):
        return False
    elif A[i] != B[i]:
        return False
    elif A[i] == B[i]:
        i+=1
        if (i == len(A)):
            return True
        return equal(A[i+1], B[i+1])
    else:
        return True

print("equal('ALICE', 'BOB'):", equal('ALICE', 'BOB'))
# Expected False
print("equal('ALICE', 'ALICE'):", equal('ALICE', 'ALICE'))
# Expected True

def addup(list):
    if len(list) <= 1:
        return list[0]
    else:
        return list[0] + addup(list[1:])

print("addup([1,2,3,4,5]):", addup([1,2,3,4,5]))
# Expected 15
print("addup(range(101)):", addup(range(101)))
# Expected 5050

def reverse(A):
    if len(A) == 0:
         return A
    else:
        return reverse(A[1:]) + A[0]

print("reverse('hello'):", reverse('hello'))
# Expected olleh

def isSorted(list):
     if len(list) <= 1:
        return True
     return list[0] <= list[1] and isSorted(list[1:])

print("isSorted([1,2,3,4]):", isSorted([1,2,3,4]))
# Expected True
print("isSorted([1,22,3,4]):", isSorted([1,22,3,4]))
# Expected False

def linearSearch(A, value):
    a = len(A)
    if a == 0:
        return False
    if A[0] == value:
        return True
    else:
        return linearSearch(A[1:], value)

print("linearSearch([1, 2, 3, 4, 5], 4):", linearSearch([1, 2, 3, 4, 5], 4))
# Expected True
print("linearSearch(range(900), -1):", linearSearch(range(900), -1))
# Expected False

def binarySearch(A, value):
    if len(A) == 0:
        return False
    mid = len(A) // 2
    if A[mid] == value:
        return True
    elif A[mid] > value:
        return binarySearch(A[:mid], value)
    elif A[mid] < value:
        return binarySearch(A[mid + 1:], value)
    else:
        return False

print("binarySearch([1, 2, 3, 4, 5], 4):", binarySearch([1, 2, 3, 4, 5], 4))
# Expected True
print("binarySearch(range(1000000), -1):", binarySearch(range(1000000), -1))
# Expected False