import seaborn as sns
from FUNCTIONS import *
import pandas as pd
import numpy as np


if __name__ == '__main__':

    filename1 = '../WorldCupMatches.csv'
    filename2 = '../WorldCupPlayers.csv'
    filename3 = '../WorldCups.csv'
    dataframe = getDataframe(filename3)



    corr = dataframe.corr()
    sns.heatmap(corr,
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values,
                annot=True)
    plt.show()