# __author__ = 'jixuebin'
# 相似度函数
from math import *

# 改进的兴趣相似度计算公式
def ImprovedSimilarity(train):
    # build inverted table for item_users，倒排表
    item_users = dict()
    for u, items in train.items():
        for i in items:
            if i not in item_users:
                item_users[i] = set()
            item_users[i].add(u)

    # calculate co-rated items between users
    C = dict()
    N = dict()
    for i, users in item_users.items():
        for u in users:
            if u not in C:
                C[u] = dict()
            if u not in N:
                N[u] = 1
            else:
                N[u] += 1  # 记录每个用户的item个数
            for v in users:
                if u == v:
                    continue
                if v not in C[u]:
                    C[u][v] = 1 / math.log(1 + len(users))  # 惩罚用户u和用户v共同兴趣列表中热门物品对他们相似度的影响
                else:
                    C[u][v] += 1 / math.log(1 + len(users))

    # calculate final similarity matrix W，计算相似度
    W = dict()
    for u, related_users in C.items():
        if u not in W:
            W[u] = dict()
        for v, cuv in related_users.items():
            W[u][v] = cuv / math.sqrt(N[u] * N[v])
    return W


# 基于距离的用户相似度
def Dist_Similarity(train, r):
    dist = dict()
    for u in train.keys():
        for v in train.keys():
            if v == u:
                continue
            else:
                co_items = list(set(train[u]).intersection(set(train[v])))  # 用户u和用户v都产生行为的item，交集
                item_length = len(co_items)
                if item_length == 0:
                    continue
                else:
                    if u not in dist:
                        dist[u] = dict()
                    tmp = 0
                    maxdist = 0
                    for item in co_items:
                        tmp += (r[u][item] - r[v][item]) * (r[u][item] - r[v][item])
                        if abs(r[u][item] - r[v][item]) > maxdist:
                            maxdist = abs(r[u][item] - r[v][item])
                    if maxdist == 0:
                        dist[u][v] = 1
                    else:
                        dist[u][v] = 1 - math.sqrt(tmp) / math.sqrt(item_length * maxdist * maxdist)
    return dist

# 基于皮尔森相关系数的相似度
    #对应乘积求和
def multipl(a, b):
    sumofab = 0.0
    for i in range(len(a)):
        temp = a[i] * b[i]
        sumofab += temp
    return sumofab

def getAverage(user,train,r):
    sum = 0.0
    for item in train[user]:
        sum += r[user][item]
    return sum/len(train[user])

def getPearson(x, y):
    up = multipl(x,y) #分子
    den = 0 #分母
    sumOfX2 = sum([pow(i, 2) for i in x])
    sumOfY2 = sum([pow(j, 2) for j in y])
    den = sqrt(sumOfX2 * sumOfY2)
    if den == 0:
        return 0
    return up/den

def corrcoef(x,y):
    n=len(x)
    #求和
    sum1=sum(x)
    sum2=sum(y)
    #求乘积之和
    sumofxy=multipl(x,y)
    #求平方和
    sumofx2 = sum([pow(i,2) for i in x])
    sumofy2 = sum([pow(j,2) for j in y])
    num=sumofxy-(float(sum1)*float(sum2)/n)
    #计算皮尔逊相关系数
    den=sqrt((sumofx2-float(sum1**2)/n)*(sumofy2-float(sum2**2)/n))
    if den == 0:
        return 0
    if num > den:
        return 1.0
    return num/den

def PearsonSimilarity(train,r): #使用用户全部电影的平均评分
    dist = dict()
    for u in train.keys():
        for v in train.keys():
            if v == u:
                continue
            else:
                #求u、v的均值
                ave_u = getAverage(u,train,r)
                ave_v = getAverage(v,train,r)
                co_items = list(set(train[u]).intersection(set(train[v])))  # 用户u和用户v都产生行为的item，交集
                item_length = len(co_items)
                if item_length == 0:
                    continue
                else:
                    if u not in dist:
                        dist[u] = dict()
                    ratings_u = []
                    ratings_v = []
                    for item in co_items:
                        ratings_u.append(r[u][item]-ave_u)
                        ratings_v.append(r[v][item]-ave_v)

                    dist[u][v] = getPearson(ratings_u,ratings_v) #将计算出的相关系数写入dist
    return dist

def PearsonSimilarity2(train,r):  #使用共同电影的平均得分
    dist = dict()
    for u in train.keys():
        for v in train.keys():
            if v == u:
                continue
            else:
                co_items = list(set(train[u]).intersection(set(train[v])))  # 用户u和用户v都产生行为的item，交集
                item_length = len(co_items)
                if item_length < 3: #过滤掉共同电影数<3的用户
                    continue
                else:
                    if u not in dist:
                        dist[u] = dict()
                    ratings_u = []
                    ratings_v = []
                    for item in co_items:
                        ratings_u.append(r[u][item])
                        ratings_v.append(r[v][item])

                    dist[u][v] = corrcoef(ratings_u,ratings_v) #将计算出的相关系数写入dist
    return dist



