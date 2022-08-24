#using bubble sort
def sort_tuple(tup):
    n = len(tup)

    for i in range(n):
        for j in range(n-i-1):
            if tup[j][0] > tup[j + 1][0]:
                tup[j],tup[j + 1] = tup[j + 1], tup[j]
    return tup

tup = [("aaaa",28),("aa",30),("bab",29),("bb",21),("csa","C")]

print(sort_tuple(tup))