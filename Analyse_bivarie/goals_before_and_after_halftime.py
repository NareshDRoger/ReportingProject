from FUNCTIONS import *
from matplotlib.pyplot import figure
import seaborn as sns

if __name__ == '__main__':
    filename = '../WorldCupMatches.csv'
    dataframe = getDataframe(filename)


    col1 = getOneColumn(dataframe,6)
    col2 = getOneColumn(dataframe, 11)
    h1 = getOneHeader(dataframe, 6)
    h2 = getOneHeader(dataframe, 11)


    title = "REPARTITION DES BUTS MARQUES PAR L'EQUIPE A DOMICILE\n AVANT ET APRES LA MI-TEMPS"
    sns.regplot(x=h1, y=h2, data=dataframe, color="steelblue")
    plt.title(title)
    plt.grid(linewidth=0.25)
    plt.show()