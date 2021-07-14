from FUNCTIONS import *


if __name__ == '__main__':
    filename = '../WorldCups.csv'
    dataframe = getDataframe(filename)

    colYear = getOneColumn(dataframe, 0)
    colCountry = getOneColumn(dataframe,1)
    colWinner = getOneColumn(dataframe,2)
    colSecond = getOneColumn(dataframe,3)
    colThird = getOneColumn(dataframe,4)
    colFourth = getOneColumn(dataframe,5)

    colCheck_Country_Podium = []


    #x année
    #y pays
    

    fig, ax = plt.subplots(figsize=(6.5,6.5))
    #PAYS D'ACCEUIL
    ax.plot(colYear, colCountry, marker="s", color='teal', label='Evolution du nombre de qualification',LineStyle='none')
    #WINNER
    ax.plot(colYear, colWinner, marker=".", color='gold', label='Evolution du nombre de qualification',
            LineStyle='none')
    #SECOND
    ax.plot(colYear, colSecond, marker=".", color='magenta', label='Evolution du nombre de qualification',
            LineStyle='none')
    #THIRD
    ax.plot(colYear, colThird, marker=".", color='lime', label='Evolution du nombre de qualification',
            LineStyle='none')

    #FOURTH
    ax.plot(colYear, colFourth, marker=".", color='red', label='Evolution du nombre de qualification',
            LineStyle='none')

    plt.xticks(np.arange(1930, 2014, 8))
    titleHist = "PODIUM ET SITUATION DU PAYS HOTE"
    plt.title(titleHist)
    plt.grid(linewidth=0.25)
    plt.show()






