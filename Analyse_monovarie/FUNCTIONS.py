import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import scipy


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




#AFFICHE L'HISTOGRAMMEN POUR UNE COLONNE QUANTITATIVE
def showHistogram_quantitavVar(df,index,columnName):
    print(getNumberOfUniqueValue(df, index))
    mean,median = getMeanAndMedian(df,index)
    figure, axes = plt.subplots()
    n, bins, patches = plt.hist(df[columnName], bins=getNumberOfUniqueValue(df,index)+20, edgecolor='black')
    axes.set_ylabel("Nombre de match")
    axes.set_xlabel(columnName)
    #axes.plot([mean, mean], [0, max(n)], label='Moyenne')
    #axes.plot([median, median], [0, max(n)], label='Médiane')
    axes.xaxis.set_major_locator(plt.MultipleLocator(10))
    plt.grid(linewidth=0.25)
    plt.show()



#AFFICHE L'HISTOGRAMME ZOOMMEE
def showHistogram_quantitavVar_ZOOM(df,index,columnName,xmin,xmax,ymin,ymax):
    mean,median = getMeanAndMedian(df,index)
    figure, axes = plt.subplots()
    n, bins, patches = plt.hist(df[columnName], bins=getNumberOfUniqueValue(df,index), edgecolor='black')
    axes.set_ylabel("Quantité")
    axes.set_xlabel(columnName)
    axes.plot([mean, mean], [0, max(n)], label='Moyenne')
    axes.plot([median, median], [0, max(n)], label='Médiane')
    plt.axis([xmin, xmax, ymin, ymax])
    plt.show()




#AFFICHE L'HISTOGRAMMEN POUR UNE COLONNE QUALITATIVE
def showHistogram_qualitativVar(df,index,columnName):
    df[df.columns[index]].value_counts().plot(kind='bar')#.sort_index().plot(kind='bar')
    plt.title(columnName)
    plt.grid(linewidth=0.25)
    plt.show()



#AFFICHE LE CAMEMBER (toujours qualitative)
def showPie(df,index):
    #plt.stitle("BONJOUR")
    plt.figure(figsize=(8, 8))
    df[df.columns[index]].value_counts().plot(kind='pie',
                                              normalize=True,
                                              autopct=lambda x: str(round(x, 2)) + '%',
                                              shadow=True,
                                              labeldistance=None)
    plt.legend(loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.1))
    plt.show()




#AFFICHER LE CAMMEBER DE LA SERIE DE L'EMPLACEMENT 0 à whereToCut
def showSubPie(df,index,whereToCut):
    #plt.stitle("BONJOUR")
    plt.figure(figsize=(8, 8))
    serie = df[df.columns[index]].value_counts()
    (serie.iloc[:whereToCut]).plot(kind='pie',
                                              normalize=True,
                                              autopct=lambda x: str(round(x, 2)) + '%',
                                              shadow=True,
                                              labeldistance=None)
    plt.legend(loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.1))
    plt.show()

