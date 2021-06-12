from FUNCTIONS import *


if __name__ == '__main__':
    filename = '../WorldCups.csv'
    dataframe = getDataframe(filename)


    colWinner = getClasses(dataframe,2)
    colRunnersUp = getClasses(dataframe,3)
    colThird = getClasses(dataframe,4)

    final = pd.concat([colWinner, colRunnersUp, colThird], axis=1)
    final.fillna(0, inplace=True)
    final = final.astype(int)
    print(final)

    titleHist = "PODIUM DE TOUTES LES COUPES DU MONDE"
    showHistogram_qualitativVar_2(final,titleHist,"Equipe","Nombre de fois")