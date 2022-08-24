n1 = int(input("Enter the no. of elements in list1 : \n"))
list1 = list()
for i in range (0,n1):
    temp1 = int(input("Enter elements of the list1 : \n"))
    list1.append(temp1)

n2 = int(input("Enter the no. of elements in list2 : \n"))
list2 = list() 
for i in range(0,n2):
    temp2 = int(input("Enter elements of the list 2 : \n"))
    list2.append(temp2)

list3 = list()
list3 = list1 + list2
print("The merged list is : \n",list3)

def Remove(duplicate):
    final_list = list()
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


n=len(list3)
list3.sort()
print("The final sorted list is : \n",Remove(list3))