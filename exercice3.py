def occurrence(list,n):
    count = 0
    for i in list:
        if i == n:
            count += 1
    return count
def compterOccurrence(list):
    mySet= set(list)
    myDict = {}
    for i in mySet:
        myDict[i] = occurrence(list,i)
    return myDict

list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

print(compterOccurrence(list))