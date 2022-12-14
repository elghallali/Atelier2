
def compterOccurrence(list):
    counts = {}
    for item in list:
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] += 1
    return counts

list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

print(compterOccurrence(list))