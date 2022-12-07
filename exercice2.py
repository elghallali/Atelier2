def deviserList(list):
    if len(list)%3 == 1:
        list.extend([0, 0])
    elif len(list)%3 == 2:
        list.append(0)
    else:
        list
    
    c = len(list) // 3
    result = []
    for i in range(3):
        test = []
        for j in range(c):
            test.append(list[i*c+j])
        result.append(test[::-1])
    return result

list = [11, 45, 8, 23, 14, 12, 78, 45, 89, 12, 3]

print(deviserList(list))