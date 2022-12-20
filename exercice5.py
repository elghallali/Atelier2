def verifyElements(list,dict):
    res= []
    for item in list:
        if item in dict.values():
            res.append(item)
    return res

list = [47, 64, 69, 37, 76, 83, 95, 97]
dict = {'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}

print(verifyElements(list, dict))