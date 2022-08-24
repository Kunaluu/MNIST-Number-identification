nStudents=0
nProfs=0
a=int(input("Enter the number of emails:"))
for i in range(a):
    b=input("Enter email:")
    if b.endswith('@student.mitwpu.edu.in'):
        nStudents+=1
    elif b.endswith('@prof.mitwpu.edu.in'):
        nProfs+=1
print("The number of student mails are:", nStudents)
print("The number of prof mails are:", nProfs)
