from FUNCTIONS import *






if __name__ == '__main__':

    filename = '../WorldCupMatches.csv'
    dataframe = getDataframe(filename)


    WICH_COLUMN = 0
    columnName = getOneHeader(dataframe,WICH_COLUMN)
    titleHist = "EVOLUTION DU NOMBRE DE MATCH PAR ANNEE"
    showHistogram_qualitativVar(dataframe, WICH_COLUMN, titleHist, "Années", "Nombre de match")

    print(getClasses(dataframe, WICH_COLUMN))
    #print(getClasses(dataframe, WICH_COLUMN).index)




