import pandas as pd
import time

def readFile(fileName):
    file = pd.read_csv(fileName)
    df = pd.DataFrame(file)

    r = dict()
    for i in range(len(df)):
        document = df[i:i + 1]
        userId = str(document['userId'][i])
        movieId = str(document['movieId'][i])
        rating = document['rating'][i]
        if userId not in r:
            r[userId] = dict()
        r[userId][movieId] = rating
    return r

def get_pred_rating(df,userId,MovieId): #读取预测评分
    rating = df.iloc[int(userId)-1][MovieId]
    return float(rating)

def read_movie_name(df,movieId):
    name = df[df['movieId'] == int(movieId)]['title'].values[0]
    return str(name)#116797

# file = pd.read_csv("movies.csv")
# df = pd.DataFrame(file)
# print(read_movie_name(df,'116797'))