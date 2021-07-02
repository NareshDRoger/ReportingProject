from FUNCTIONS import *
from matplotlib.pyplot import figure
import seaborn as sns

if __name__ == '__main__':
    filename = '../WorldCupMatches.csv'
    dataframe = getDataframe(filename)

    h1 = getOneHeader(dataframe, 5)
    h2 = getOneHeader(dataframe, 6)
    h3 = getOneHeader(dataframe, 7)
    h4 = getOneHeader(dataframe, 8)

    home = dataframe[[h1, h2]].dropna()
    away = dataframe[[h4, h3]].dropna()

    finalDaframe = pd.DataFrame(columns=['countries', 'goals'])
    finalDaframe = finalDaframe.append(
        home.rename(index=str, columns={'Home Team Name': 'countries', 'Home Team Goals': 'goals'}))
    finalDaframe = finalDaframe.append(
        away.rename(index=str, columns={'Away Team Name': 'countries', 'Away Team Goals': 'goals'}))

    finalDaframe['goals'] = finalDaframe['goals'].astype('int64')

    finalDaframe = finalDaframe.groupby(['countries'])['goals'].sum().sort_values(ascending=False)

    finalDaframe[:10].plot(x=finalDaframe.index, y=finalDaframe.values, kind="bar", #figsize=(12, 6),fontsize=14,
                                color='mediumseagreen')
    plt.xlabel('Pays')
    plt.ylabel('Nombre de buts')
    plt.title('TOP 10 DES PAYS AVEC LE PLUS DE BUTS MARQUES\n (Toutes années confondues)')
    plt.grid(linewidth=0.25)
    plt.show()