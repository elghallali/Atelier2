def intersectionOfSets(set1,set2):
    return set1.intersection(set2)

def differenceOfSets(set1, set2):
    return set1.difference(set2)


set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}

intersection = intersectionOfSets(set1,set2)
print(intersection)
set1 = differenceOfSets(set1,set2)
print(set1)