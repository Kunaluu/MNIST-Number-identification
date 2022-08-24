string1 = input("Enter a string of your choice:\n")

print("The total no of characters in the string is\n",len(string1))

print("The string repeated 10 times:\n")
for i in range(1,11):
    print(string1)

print("First 3 characters of a string:\n",string1[0:4])

print("Last 3 characters of a string:\n",string1[-3:])

reverse_string = string1[::-1]
print("Reversed string:\n",reverse_string)

#7th character of a string
if(len(string1) > 7 ):
    print("The 7th character is:\n",string1[8])
else:
    print("String does not have 7 characters.")

remove_string = string1[1:-1]
print("String where first and last characters are removed:\n",remove_string)

string_caps = string1.upper()
print("String is in Caps:\n",string_caps)

string_replace = string1.replace("a","e")
print("Replacing every a with an e:\n",string_replace)

print("Every letter replaced by a space:\n",string1.replace(string1,''))