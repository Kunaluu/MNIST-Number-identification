#assignment 2
a=(input("Enter a string="))
print(a)
print("length of string is=", len(a))
print(a*10)
print("first 3 characters=", a[0:3])
print("last 3 characters=", a[-3:])
print("The string backwards=", a[::-1])
if(len(a)>7):
   print("seventh character of string is=", a[7])
else:
   print("seventh character not present")
print("string with its first and last characters removed=", a[1:-1])
print("string in all caps=", a.upper())
print("string with every a replaced with an e=", a.replace('a','e'))
print("string with every letter replaced by space=", a.replace('a',' '))