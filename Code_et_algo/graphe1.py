from FUNCTIONS import *


if __name__ == '__main__':
    filename = '../WorldCups.csv'
    dataframe = getDataframe(filename)


    colYear = getOneColumn(dataframe,0)
    colWinner = getOneColumn(dataframe,2)
    colSecond = getOneColumn(dataframe,3)
    colThird = getOneColumn(dataframe,4)
    colFourth = getOneColumn(dataframe,5)


    fig, ax = plt.subplots(figsize=(40,30))


    column_labels = list(colYear)
    print(column_labels)

    data = []

    ltemp1 = []
    for x in colWinner:
        ltemp1.append(str(x))
    data.append(ltemp1)
    ltemp2 = []
    for x in colSecond:
        ltemp2.append(str(x))
    data.append(ltemp2)
    ltemp3 = []
    for x in colThird:
        ltemp3.append(str(x))
    data.append(ltemp3)
    ltemp4 = []
    for x in colFourth:
        ltemp4.append(str(x))
    data.append(ltemp4)



    df = pd.DataFrame(data, columns=column_labels)
    df.to_excel("podium.xlsx")
    plt.title('EVOLUTION DU PODIUM DES COUPES DU MONDE')
    print(df)
    #ax.axis('tight')
    from matplotlib.pyplot import figure

    ax.axis('off')
    ax.table(cellText=df.values,colLabels=df.columns,rowLabels=["WINNER","RUNNERS-UP","THIRD","FOURTH"],loc="center")
    plt.show()
