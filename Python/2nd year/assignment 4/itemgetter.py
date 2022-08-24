#using item getter()
import operator
from collections import OrderedDict
dict1 = {}
n = int(input("Enter the number of elements you want in a dictionary:"))
for i in range(n):
    keys = int(input("Enter key:\n"))
    values =  int(input("Enter value:\n"))
    dict1[keys] = values
print("The original dictionary is:",dict1)
sorted_tuples =sorted(dict1.items(),key = operator.itemgetter(1))
print("The sorted tuple is:\n",sorted_tuples)
sorted_dict = OrderedDict()
for k,v in sorted_tuples:
    sorted_dict[k] = v
print("The dictionary sorted according to the values is:",sorted_dict)