from FUNCTIONS import *






if __name__ == '__main__':

    filename = 'C:/Users/hejar/OneDrive/Bureau/ESGI/Reporting et restitution (S2)/PROJET/WorldCupMatches.csv'
    dataframe = getDataframe(filename)


    WICH_COLUMN = 0
    columnName = getOneHeader(dataframe,WICH_COLUMN)
    showHistogram_quantitavVar(dataframe, WICH_COLUMN,columnName)





