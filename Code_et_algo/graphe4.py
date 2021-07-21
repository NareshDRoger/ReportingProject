from FUNCTIONS import *
from matplotlib.pyplot import figure

if __name__ == '__main__':
    filename = '../WorldCupMatches.csv'

    #NE PRENDRE QUE LE BRESIL, L'ARGENTIRE ET L'ITALY
    #METTRE DANS UN GRAND DATAFRAME

    year = 1930
    newDataframe1 = pd.DataFrame(columns=["Year", "Team", "Total_goals"])
    carreFinal = ["Quarter-finals","Semi-finals","Final","Match for third place"]

    for year in range(1950,2015,4):
        dataframe = getDataframe(filename)
        row = 0
        totalGoalBrazil = 0
        totalGoalArgentine = 0
        totalGoalItaly = 0
        for i in dataframe.values:
            if(i[0] != year):
            #if (str(i[5]) != "Brazil" and str(i[5]) != "Argentina" and str(i[5]) != "Italy"):
                dataframe.drop(row, inplace=True)
            row += 1
        for i in dataframe.values:
            if (str(i[5]) == "Brazil" and str(i[2]) not in carreFinal):
                totalGoalBrazil += int(i[6])

            if (str(i[8]) == "Brazil" and str(i[2]) not in carreFinal):
                totalGoalBrazil += int(i[7])
            if (str(i[5]) == "Argentina" and str(i[2]) not in carreFinal):
                totalGoalArgentine += int(i[6])

            if (str(i[8]) == "Argentina" and str(i[2]) not in carreFinal):
                totalGoalArgentine += int(i[7])
            if (str(i[5]) == "Italy" and str(i[2]) not in carreFinal):
                totalGoalItaly += int(i[6])

            if (str(i[8]) == "Italy" and str(i[2]) not in carreFinal):
                totalGoalItaly += int(i[7])

        #print(dataframe)
        #print("Nombre de but total du Brésil "+str(totalGoalBrazil))



        newDataframe1 = newDataframe1.append({"Year":year, "Team":"Brazil", "Total_goals":totalGoalBrazil}, ignore_index=True)
        newDataframe1 = newDataframe1.append({"Year": year, "Team": "Argentina", "Total_goals": totalGoalArgentine},ignore_index=True)
        newDataframe1 = newDataframe1.append({"Year": year, "Team": "Italy", "Total_goals": totalGoalItaly},ignore_index=True)
        print(year)


    print(newDataframe1)



    #CREER 3 DATAFRAMES
    newDataframeBrazil = pd.DataFrame(columns=["Year", "Team", "Total_goals"])
    newDataframeArgentina = pd.DataFrame(columns=["Year", "Team", "Total_goals"])
    newDataframeItaly = pd.DataFrame(columns=["Year", "Team", "Total_goals"])

    for i in newDataframe1.values:
        if(str(i[1]) == "Brazil"):
            newDataframeBrazil = newDataframeBrazil.append({"Year": i[0], "Team": i[1], "Total_goals": i[2]},ignore_index=True)

        if(str(i[1]) == "Argentina"):
            newDataframeArgentina = newDataframeArgentina.append({"Year": i[0], "Team": i[1], "Total_goals": i[2]},ignore_index=True)

        if (str(i[1]) == "Italy"):
            newDataframeItaly = newDataframeItaly.append({"Year": i[0], "Team": i[1], "Total_goals": i[2]},
                                                           ignore_index=True)


    #LE PLOT
    colYear = getOneColumn(newDataframeBrazil,0)
    colGoalsBrazil = getOneColumn(newDataframeBrazil,2)
    colGoalsArgentina = getOneColumn(newDataframeArgentina,2)
    colGoaldItaly = getOneColumn(newDataframeItaly,2)

    titleOfHist = "LE NOMBRE DE BUTS MARQUES DURANT LES PHASES DE POULE\n INFLUE-T-IL SUR LE CLASSEMENT FINAL?"
    fig, ax = plt.subplots()
    ax.plot(colYear, colGoalsBrazil, marker="o", color='teal', label='Brazil')
    ax.plot(colYear, colGoalsArgentina, marker="o", color='orange', label='Argentina')
    ax.plot(colYear, colGoaldItaly, marker="o", color='green', label='Italy')
    ax.plot(marker="o",color='red',label='Carre final')
    ax.legend()
    ax.set_xlabel("Années")
    ax.set_ylabel("Nombres")
    plt.title(titleOfHist)
    plt.xticks(np.arange(1950, 2015, 8))
    plt.yticks(np.arange(0, 24, 1))
    # plt.yticks(np.arange(10, 40, 2))
    plt.grid(linewidth=0.25)
    plt.show()









