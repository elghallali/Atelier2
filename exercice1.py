def createList(list1, list2):
    return list1[1::2] + list2[::2]

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
c = createList(list1,list2)
print(c)