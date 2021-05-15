import sys
import string
import pandas as pd
from tqdm import tqdm

def occurrence_M():
    """
    Creates an 28x28 dictionary containing all possibilities with characters a-z, space and # for all special characters and punctuation.
    Then transforms into a dataframe for easier use later on.
    :return: pd.Dataframe
    """
    occ_m = dict()
    for key in string.ascii_lowercase + " #":
        occ_m[key] = {}
        for value in string.ascii_lowercase + " #":
            occ_m[key][value] = 0
    occ_m = pd.DataFrame.from_dict(occ_m)
    return occ_m

def to_perc(occ_m):
    """
    Transforms every cell into a percentage using the sum of a row
    :param occ_m: pd.Dataframe
    :return: dict()
    """
    rows_sum = occ_m.sum(axis=1).values
    for c, b in enumerate(occ_m):
        if rows_sum[c] != 0:
            occ_m.loc[b] = occ_m.loc[b].apply(lambda x: (x / rows_sum[c]) * 100)
    return occ_m.to_dict()

# Uncomment line below if you want to create train dictionary
# text = open("mapper.txt", "r")

# occ_m = occurrence_M()

for line in tqdm(sys.stdin): # write text instead of tqdm(sys.stdin) If you want to create train dictionary
    occ_m = occurrence_M()
    bigram_lst = eval(line)
    for bigram in bigram_lst:
        word, count = bigram
        occ_m[word[1]][word[0]] += int(count)
    print(occ_m.to_dict())

# to_perc(occ_m)




