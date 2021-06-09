from FUNCTIONS import *





if __name__ == '__main__':

    filename = 'C:/Users/hejar/OneDrive/Bureau/ESGI/Reporting et restitution (S2)/PROJET/WorldCupMatches.csv'
    dataframe = getDataframe(filename)


    WICH_COLUMN = 3
    columnName = getOneHeader(dataframe, WICH_COLUMN)

    #print(getNumberOfUniqueValue(dataframe,WICH_COLUMN))
    #print(getClasses(dataframe,WICH_COLUMN))
    #showHistogram_qualitativVar(dataframe, WICH_COLUMN, columnName)



