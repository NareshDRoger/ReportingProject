from FUNCTIONS import *
import csv

if __name__ == '__main__':
    filename = '../WorldCups.csv'
    filenameGoldGoal = '../ballonOr.csv'
    dataframe = getDataframe(filename)
    dataframeGoal = getDataframe(filenameGoldGoal)


    row = 0
    for i in dataframeGoal.values:
        if(i[2] != "1st"):
            dataframeGoal.drop(row,inplace=True)
        row += 1
    #print(dataframeGoal)

    dataframeGoal.to_csv("../ballonOrModifie.csv")


    colYearCup = getOneColumn(dataframe, 0)
    colCountryCup = getOneColumn(dataframe, 1)
    colWinnerCup = getOneColumn(dataframe, 2)
    colSecondCup = getOneColumn(dataframe, 3)
    colThirdCup = getOneColumn(dataframe, 4)
    colFourthCup = getOneColumn(dataframe, 5)



    #-----------------------------------------------------------------------------------------------------#
    #VA COMPLETER LE FICHIER ../ballonOrPays.xlsx encore sur les pays des joueurs ballon d'or
    #ON VA FAIRE 2 GRPAHE : UN SUR LES ANNNES (en x) ET LES PAYS BALLON D'OR (en y)
    #L'AUTRE SUR LES ANNES (en x) ET LES PAYS GAGNAT, 2eme ,... (en y)
    #VAUX MIEUX PRENDRE UNE FOURCHETTE D'ANNE PAR EXEMPLE ENTRE 1970 et 1990
    #Graphe 1 pas de 1 plt.xticks(np.arange(1970, 1990, 1))
    #Grapeh 2 pas de 4
    #-----------------------------------------------------------------------------------------------------#







    #initialise l'excel ballonOrPays
    fileExcel = '../ballonOrPays.xlsx'
    dataframeFinalGold = getDataframeFromExcel(fileExcel)
    #prendre les colones qu'on veut et les mettrei en series.Series
    colYearGold = getOneColumn(dataframeFinalGold,0)
    colTest = getOneColumn(dataframeFinalGold,3)
    colCountryGold = getOneColumn(dataframeFinalGold,6)
    print(colCountryGold)
    #faire comme dans le grapeh 2
    #En x => années
    #En y => pays
    #une courbes sur les ballons d'or
    #une courbe sur les winnner
    #...runners-up
    #..
    #.

    fig, ax = plt.subplots(figsize=(6.5, 6.5))
    # WINNER
    ax.plot(colYearCup, colWinnerCup, marker=".", color='gold',LineStyle='none')
    # SECOND
    ax.plot(colYearCup, colSecondCup, marker=".", color='magenta',LineStyle='none')
    # THIRD
    ax.plot(colYearCup, colThirdCup, marker=".", color='lime',LineStyle='none')

    # FOURTH
    ax.plot(colYearCup, colFourthCup, marker=".", color='red',LineStyle='none')
    plt.xticks(np.arange(1930, 2014, 8))
    titleHist = "PODIUM ET SITUATION DU PAYS HOTE"
    #plt.title(titleHist)
    plt.grid(linewidth=0.25)
    plt.show()



    fig2, ax = plt.subplots(figsize=(6.5, 6.5))
    # BALLON D'OR
    ax.plot(colYearGold, colTest, marker=".", color='gold', LineStyle='none')
    plt.xticks(np.arange(1958, 2019, 2))
    #titleHist = "PODIUM ET SITUATION DU PAYS HOTE"
    # plt.title(titleHist)
    plt.grid(linewidth=0.25)
    plt.show()





