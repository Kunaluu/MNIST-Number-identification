
def check_string(string):
    count = 1
    for i in range(0,len(string)):
        if string[i] == " ":
            count = count + 1
    return count

string = str(input("Please enter a string of your choice:\n"))
print("The estimation of the number of words in this string is:",check_string(string))