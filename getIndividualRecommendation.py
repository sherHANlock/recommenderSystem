from DataSplit import *
from DictToFile import *
from FileToDict import *
from Recommend import *
from UserSimilarity import *

from read_csv import *

def getRank(user):
    r = readFile("ratings.csv")

    (train, cv, test) = SplitData(r)

    # W = PearsonSimilarity2(train,r)

    W = fileToDictJson("s_data/similarity_pearson3.txt")

    N = 20
    K = 160

    rank = GetRecommendation(user,train,W,K,r)

    return sorted(rank, key=rank.__getitem__,reverse=True)[0:N]#['1', '318', '296', '589', '527', '457', '588', '50', '150', '47', '2858', '260', '2571', '595', '32', '380', '1270', '1198', '1210', '4993']


# print(getMovieName(getRank('17')))
