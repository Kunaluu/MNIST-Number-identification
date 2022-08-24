#using sorted fn
dict1 = {}
n = int(input("Enter elements in the dictionary:\n"))
for i in range(n):
    keys = int(input("Enter key:\n"))
    values = int(input("Enter value:\n"))
    dict1[keys] = values
print("Original dictionary:",dict1)

sorted_dict = {}
sorted_keys = sorted(dict1, key = dict1.get)
for i in sorted_keys:
    sorted_dict[i] = dict1[i]
print("Sorted Dictionary:\n",sorted_dict)