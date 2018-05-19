
fact = 1
n = int(input("Enter a number: "))
for i in range(n,0,-1):
    if (i == 0):
        fact = 1
    else:
        fact = fact * i
        #print(fact)

print(fact)

def factorial(k):
    if(k==0):
        return 1
    else:
        fact1 = k * factorial(k - 1)
    return fact1

print(factorial(5))
