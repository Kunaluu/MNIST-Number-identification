#lambda
dict1 = {}
n = int(input("Enter the number of elements you want in a dictionary:"))
for i in range(n):
    keys = int(input("Enter key:\n"))
    values =  int(input("Enter value:\n"))
    dict1[keys] = values
print("The original dictionary is:",dict1)


sorted_tuples = sorted(dict1.items(),key = lambda item: item[1])
print("Sorted tuple is",sorted_tuples)
sorted_dict = {k:v for k, v in sorted_tuples}
print("The sorted dictionary is:",sorted_dict)