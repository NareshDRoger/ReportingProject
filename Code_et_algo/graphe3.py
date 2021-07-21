from FUNCTIONS import *
import csv

if __name__ == '__main__':
    filename = '../WorldCups.csv'
    filenameGoldGoal = '../Fichier_Temporaire_Graphe3/ballonOr.csv'
    dataframe = getDataframe(filename)
    dataframeGoal = getDataframe(filenameGoldGoal)

    #FILTRER LE FICHIER DES BALLONS D'OR SUR JUSTE LE PREMIER QUI A RECU LE BALLON D'OR (non les 2nd et 3eme)
    row = 0
    for i in dataframeGoal.values:
        if(i[2] != "1st"):
            dataframeGoal.drop(row,inplace=True)
        row += 1
    dataframeGoal.to_csv("../Fichier_Temporaire_Graphe3/ballonOrTemporaire.csv")






    #-----------------------------------------------------------------------------------------------------#
    #VA COMPLETER LE FICHIER ../ballonOrPays.xlsx encore sur les pays des joueurs ballon d'or
    #ON VA FAIRE 2 GRPAHE : UN SUR LES ANNNES (en x) ET LES PAYS BALLON D'OR (en y)
    #L'AUTRE SUR LES ANNES (en x) ET LES PAYS GAGNAT, 2eme ,... (en y)
    #VAUX MIEUX PRENDRE UNE FOURCHETTE D'ANNE PAR EXEMPLE ENTRE 1970 et 1990
    #Graphe 1 pas de 1 plt.xticks(np.arange(1970, 1990, 1))
    #Grapeh 2 pas de 4
    #-----------------------------------------------------------------------------------------------------#







    #initialise l'excel ballonOrPays
    fileExcel = '../Fichier_Temporaire_Graphe3/ballonOrPays.xlsx'
    dataframeFinalGold = getDataframeFromExcel(fileExcel)
    # FILTRER SUR LES PREMIERS DU BALLON D'OR
    row = 0
    for i in dataframeFinalGold.values:
        if (i[0] < 1970 or i[0] > 1990):
            dataframeFinalGold.drop(row, inplace=True)
        row += 1
    row2 = 0
    for i in dataframe.values:
        if (i[0] < 1970 or i[0] > 1990):
            dataframe.drop(row2, inplace=True)
        row2 += 1




    colYearCup = getOneColumn(dataframe, 0)
    colCountryCup = getOneColumn(dataframe, 1)
    colWinnerCup = getOneColumn(dataframe, 2)
    colSecondCup = getOneColumn(dataframe, 3)
    colThirdCup = getOneColumn(dataframe, 4)
    colFourthCup = getOneColumn(dataframe, 5)
    colYearGold = getOneColumn(dataframeFinalGold, 0)
    colPlayerGold = getOneColumn(dataframeFinalGold, 2)
    colCountryGold = getOneColumn(dataframeFinalGold, 6)



    #COUPE DU MONDE PODIUM
    fig, ax = plt.subplots(figsize=(10, 10))
    # WINNER
    ax.plot(colYearCup, colWinnerCup, marker="s", color='gold', LineStyle='none')
    # SECOND
    ax.plot(colYearCup, colSecondCup, marker="s", color='magenta', LineStyle='none')
    # THIRD
    ax.plot(colYearCup, colThirdCup, marker="s", color='lime', LineStyle='none')

    # FOURTH
    ax.plot(colYearCup, colFourthCup, marker="s", color='red', LineStyle='none')
    plt.xticks(np.arange(1970, 1990, 1))
    titleHist = "PODIUM DE LA COUPE DU MONDE de 1970 à 1990"
    plt.title(titleHist)
    plt.grid(linewidth=0.25)
    plt.show()



    #BALLON D'OR
    fig2, ax = plt.subplots(figsize=(10, 10))
    # BALLON D'OR
    ax.plot(colYearGold, colCountryGold, marker=".", color='black', LineStyle='none')


    plt.xticks(np.arange(1970, 1990, 1))
    titleHist2 = "BALLON D'OR de 1970 à 1990"
    plt.title(titleHist2)
    plt.grid(linewidth=0.25)
    plt.show()
    






