                  # PYTHON PROGRAMS

# 1. PRIME NUMBER
def prime(num):
    res = True
    if num > 1:
        for i in range(2,num):
            if num%i == 0:
                res = False
    if res:
        print(f"{num} is Prime")
    else:
        print(f"{num} is Not a Prime")


for number in range(2,11):
    prime(number)

#########################################################################################################
# 2.FIBONACCI SERIES
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fibonacci(30)

##########################################################################################################
# 3.FACTORIAL
def factorial(num):
    res = 1
    for i in range(2,num+1):
        res *= i

    return res

print(factorial(5))

##########################################################################################################
# 4.SECOND LARGEST
def second_largest(li):
    largest = li[0]
    second_largest = li[0]
    for i in range(len(li)):
        if li[i]>largest:
            largest = li[i]

    for i in range(len(li)):
        if li[i]>second_largest and li[i] < largest:
            second_largest = li[i]

    return second_largest


l = [10, 20, 80, 40, 50, 500]
print(second_largest(l))

##########################################################################################################
# 5.PALINDROME
def palindrome(string):
    if string == string[::-1]:
        print("Yes Its a Palindrome")
    else:
        print("NO Its not a Palindrome")

palindrome("madam")
palindrome("rockey")

##########################################################################################################
# 6.PERFECT NUMBER
def perfect_number(num):
    divisors = []
    for i in range(1,num):
        if num%i==0:
            divisors.append(i)
    if num == sum(divisors):
        print("Yes it is a Perfect Number")
    else:
        print("Nope...!!!! It is not a perfect Number")

perfect_number(496)
perfect_number(5)

##########################################################################################################