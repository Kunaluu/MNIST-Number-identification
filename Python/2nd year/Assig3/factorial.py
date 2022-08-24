import math
import factorial
def factorial_recursive(n):
    if n==1:
        return n
    else:
        return n*factorial_recursive(n-1)

def factorial_iterative(n):
    fact=1
    if n<0:
        print("Sorry factorial does not exist for negative nos.")
    elif n==0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,n+1):
            fact = fact*i
        return fact

def ternary_operator(n):
    return 1 if (n==1 or n==0 )else n*ternary_operator(n-1)

n =int(input("enter the number: "))
print("Factorial of no. is using iterative method is :", factorial_iterative(n))
print("Factorial of no. is using recursive method is : ",factorial_recursive(n))
print("Factorial of no. is using ternary operator is : ", ternary_operator(n))
print("Factorial of no. is using dictionary is :",math.factorial(n))

s=factorial.fact(n)
print("Factorial of a no. using module is :",s)