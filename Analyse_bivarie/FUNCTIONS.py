import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


#RETOURNE LE DATAFRAME
def getDataframe(filename):
    df = pd.read_csv(filename, delimiter=',')
    df.dropna(axis=0, how='all', inplace=True)
    return df


#RETOURNE LE NOM D'UN HEADER DU DATAFRAME
def getOneHeader(df,index):
    return df.columns[index]



#RETOURNE UNE COLONNE DU DATAFRAME
def getOneColumn(df,index):
    return df[df.columns[index]]



#RETOURNE TOUTE LES CLASSES DE LA COLONNE
def getNumberOfUniqueValue(df,index):
    l = list(getOneColumn(df,index))
    return len(set(l))


#AVOIR LES CLASSES ET LE NOMBRE D'ELEMENT
def getClasses(df,index):
    return df[df.columns[index]].value_counts()


#RETOURNE LE MEAN ET MEDIAN DE LA COLONNE
def getMeanAndMedian(df,index):
    l = list(getOneColumn(df, index))
    return np.mean(l), np.median(l)




#RETOURNE LE SKEW ET KURTOSIS DE LA COLONNE
def getSkewAndKurtosis(df,index):
    l = list(getOneColumn(df, index))
    return stats.skew(l), stats.kurtosis(l)





#FAIRE LA TABLE DE CONTAGENCE
def contegenceTable(df,index1,index2):
    h1 = getOneHeader(df,index1)
    h2 = getOneHeader(df,index2)

    l1 = list(df[df.columns[index1]])
    l2 = list(df[df.columns[index2]])

    df1 = pd.DataFrame(l1, columns=[h1])
    df2 = pd.DataFrame(l2, columns=[h2])

    return pd.crosstab(df2[h2], df1[h1], normalize='all')
    # pd.crosstab(df["lum"], df["atm"], normalize='columns')





#FAIRE LA TABLE DE CORRELATION
def correlationTable(df,index1,index2):
    dfResult = df[[getOneHeader(df,index1), getOneHeader(df,index2)]]

    corrMatrix = dfResult.corr()
    return corrMatrix