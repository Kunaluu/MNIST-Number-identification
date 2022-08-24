#code to find the factorial of a number
def factorial(x):
    if(x == 1) or (x == 0):
        return 1
    else:
        return x*factorial(x - 1)
number = int(input("Please enter a number of your choice:\n"))  
factorial(number)  
print("The factorial of the given number is:",factorial(number))




