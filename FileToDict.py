import json

# file = open('json.txt', 'r')
# js = file.read()
# test = json.loads(js)
# print(test)
# file.close()

def fileToDict(FileName): #当字典的元素仍为字典时，无法使用
    fr = open(FileName,'r+')
    dic = eval(fr.read())   #读取的str转换为字典
    fr.close()
    return dic

def fileToDictJson(FileName):  #当字典的元素仍为字典时，使用json
    file = open(FileName, 'r')
    js = file.read()
    dic = json.loads(js)
    file.close()
    return dic


# rank1 = fileToDict("users_recommendation.txt")
# rank2 = fileToDict("users_recommendation1.txt")
# print(rank1 == rank2)