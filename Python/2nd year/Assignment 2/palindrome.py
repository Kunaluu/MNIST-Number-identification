def Palindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = str(input("Enter a string\n"))
ans = Palindrome(s)
 
if (ans):
    print("It is a palindrome")
else:
    print("It is not a palindrome")