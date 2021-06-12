from FUNCTIONS import *


if __name__ == '__main__':
    filename = '../WorldCupMatches.csv'
    dataframe = getDataframe(filename)

    WICH_COLUMN_1 = 5
    WICH_COLUMN_2 = 6
    WICH_COLUMN_3 = 7
    WICH_COLUMN_4 = 8
    WICH_COLUMN_5 = 9

    h1 = getOneHeader(dataframe, WICH_COLUMN_1)
    h2 = getOneHeader(dataframe, WICH_COLUMN_2)
    h3 = getOneHeader(dataframe, WICH_COLUMN_3)
    h4 = getOneHeader(dataframe, WICH_COLUMN_4)
    h5 = getOneHeader(dataframe, WICH_COLUMN_5)

    colLenght = len(getOneColumn(dataframe,WICH_COLUMN_1))

    """
    for i in range(colLenght):
        if(str(dat.loc[i]) != " "):
            print(str(dat.loc[i]).split()[0])
    """

    #CREER 2 DATAFRAME AVEC 2 COLONNES CHACUN
    dataframeH1H2 = getTwoColumn(dataframe,h1,h2)
    dataframeH3H4 = getTwoColumn(dataframe, h3, h4)
    dataframeH5 = getOneColumn(dataframe, WICH_COLUMN_5)
    newDataframe1 = pd.DataFrame(columns=["Home_Team_Name_and_Goals"])


    for i in range(colLenght):
        if(str(dataframeH5.loc[i]) != " "):
            newDataframe1 = newDataframe1.append({"Home_Team_Name_and_Goals": str(dataframeH5.loc[i]).split()[0]}, ignore_index=True)
        else :
            if(int(dataframeH1H2.loc[i][1]) > int(dataframeH3H4.loc[i][0])):
                newDataframe1 = newDataframe1.append({"Home_Team_Name_and_Goals": dataframeH1H2.loc[i][0]}, ignore_index=True)
            else:
                newDataframe1 = newDataframe1.append({"Home_Team_Name_and_Goals": dataframeH3H4.loc[i][1]},ignore_index=True)


    #print(newDataframe1)
    print(getClasses(newDataframe1, 0))

    #showHistogram_qualitativVar(dataframe, WICH_COLUMN, titleHist, "Années", "Nombre de match")
    titleHist = "CLASSEMENT DES 10 PAYS AVEC LE PLUS DE VICTOIRE DE MATCHS\n (Toutes années confondues)"

    showHistogram_qualitativVar(newDataframe1, 0, titleHist, "Pays", "Nombre de match gagné")
