x = int(input("Please enter the first number"))
y = int(input("Please enter the 2nd number"))
#code for addition
def add_numbers(x, y):
    sum_numbers = (x + y)
    return sum_numbers
#code for multiplication
def multiply_numbers(x , y):
    multiply_no = (x * y)
    return multiply_no
print("The addition is", add_numbers(x , y))
print("The multiplication is", multiply_numbers(x , y))
