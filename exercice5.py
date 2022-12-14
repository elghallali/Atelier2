def verifyElements(list,dict):
    for item in list:
        if item in dict:
            continue
        else:
            list.remove(item)
    return list

list = [47, 64, 69, 37, 76, 83, 95, 97]
dict = {'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}

print(verifyElements(list, dict))