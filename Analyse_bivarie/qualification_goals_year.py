from FUNCTIONS import *
from matplotlib.pyplot import figure

if __name__ == '__main__':
    filename = '../WorldCups.csv'
    dataframe = getDataframe(filename)


    col1 = getOneColumn(dataframe,0)
    col2 = getOneColumn(dataframe, 6)
    col3 = getOneColumn(dataframe, 7)

    titleOfHist = "EVOLUTION DU NOMBRE DE QUALIFICATION D'EQUIPE\nET DU NOMBRE DE BUT MARQUE PAR ANNEE"

    fig, ax = plt.subplots()
    ax.plot(col1, col3, marker="o", color='teal',label='Evolution du nombre de qualification')
    ax.plot(col1, col2, marker="o", color='orange', label='Evolution des buts marqués')
    ax.legend()
    ax.set_xlabel("Années")
    ax.set_ylabel("Nombres")
    plt.title(titleOfHist)
    plt.xticks(np.arange(1930, 2014, 10))
    plt.yticks(np.arange(10, 180, 10))
    #plt.yticks(np.arange(10, 40, 2))
    plt.grid(linewidth=0.25)
    plt.show()
