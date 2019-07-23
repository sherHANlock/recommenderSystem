import json

# test = {
#     'andy':{
#         'age': 23,
#         'city': 'beijing',
#         'skill': 'python'
#     },
#     'william': {
#         'age': 25,
#         'city': 'shanghai',
#         'skill': 'js'
#     }
# }

# js = json.dumps(test)
# file = open('json.txt', 'w')
# file.write(js)
# file.close()

def dictToFile(FileName,var): #当字典的元素仍为字典时，无法使用
    fw = open(FileName,'w+')
    fw.write(str(var))      #把字典转化为str
    fw.close()

def dictToFileJson(FileName,var): #当字典的元素仍为字典时，使用json
    js = json.dumps(var)
    file = open(FileName, 'w')
    file.write(js)
    file.close()


