from FUNCTIONS import *




if __name__ == '__main__':

    filename = 'C:/Users/hejar/OneDrive/Bureau/ESGI/Reporting et restitution (S2)/PROJET/WorldCupMatches.csv'
    dataframe = getDataframe(filename)


    var1 = 5
    var2 = 18

    t = contegenceTable(dataframe,var1,var2)
    print(t)