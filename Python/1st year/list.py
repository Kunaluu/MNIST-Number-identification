x = int(input("Enter number of elements needed"))

#creating empty list
list = []
for i in range(0,x+1):
    y = int(input("Enter a number at the index"))
    list.append(y)
    print("list in ascending order :")
    print(list)

list.sort()

print("list in descending order :")
list.reverse()
print(list)