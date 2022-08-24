#using loops
dict1 = {}
n = int(input("Enter the number of elements you want in a dictionary:"))
for i in range(n):
    keys = int(input("Enter key:\n"))
    values =  int(input("Enter value:\n"))
    dict1[keys] = values
print("The original dictionary is:",dict1)

sorted_values = sorted(dict1.values())
sorted_dict = {}
for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
            break
print("The sorted dictionary is:",sorted_dict)
