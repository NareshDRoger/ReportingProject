from FUNCTIONS import *




if __name__ == '__main__':

    filename = 'C:/Users/hejar/OneDrive/Bureau/ESGI/Reporting et restitution (S2)/PROJET/WorldCupMatches.csv'
    dataframe = getDataframe(filename)


    WICH_COLUMN = 9

    print(getNumberOfUniqueValue(dataframe,WICH_COLUMN))
    print(getClasses(dataframe,WICH_COLUMN))

