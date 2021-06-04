from FUNCTIONS import *

import matplotlib.pyplot as plt





if __name__ == '__main__':

    filename = 'C:/Users/hejar/OneDrive/Bureau/ESGI/Reporting et restitution (S2)/PROJET/WorldCupMatches.csv'
    dataframe = getDataframe(filename)


    WICH_COLUMN = 15
    #columnName = getOneHeader(dataframe,WICH_COLUMN)

    print(getNumberOfUniqueValue(dataframe,WICH_COLUMN))
    print(getClasses(dataframe,WICH_COLUMN))
    #showPie(dataframe,WICH_COLUMN)
    showSubPie(dataframe,WICH_COLUMN,10)




