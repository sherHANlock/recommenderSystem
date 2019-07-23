from DataSplit import *
from DictToFile import *
from FileToDict import *
from Recommend import *
from UserSimilarity import *

from read_csv import *

def getRank_group(users):
    r = readFile("ratings.csv")

    (train, cv, test) = SplitData(r)

    # W = PearsonSimilarity2(train,r)

    W = fileToDictJson("s_data/similarity_pearson3.txt")

    N = 20
    K = 160

    users_recommendation = GetRecommendation_for_group2(users, train, W, K, r)

    dic = dict()
    df = pd.read_csv('result70.csv')
    for user in users:
        for item in users_recommendation[user]:
            if item not in dic:
                dic[item] = 0
            dic[item] += get_rating(get_pred_rating(df, user, item))

    return sorted(dic, key=dic.__getitem__,reverse=True)[0:N]

# users = set()
# i = 0
# for user in ['2','3','4','5']:
#     users.add(user)
#
# print(len(users))
# print(users)
# print(getMovieName(getRank_group(users)))



