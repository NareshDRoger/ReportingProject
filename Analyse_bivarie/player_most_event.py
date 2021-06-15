from FUNCTIONS import *
from matplotlib.pyplot import figure
import math

if __name__ == '__main__':
    filename = '../WorldCupPlayers.csv'
    dataframe = getDataframe(filename)


    h1 = getOneHeader(dataframe,2)
    h2 = getOneHeader(dataframe,6)
    h3 = getOneHeader(dataframe,8)

    df = getThreeColumn(dataframe,h1,h2,h3)
    #print(df)

    print(type(df))

    #pour enlever un warning
    df = df.copy()
    df[h3] = df[h3].replace(np.nan, "nothing")

    newDataframe1 = pd.DataFrame(columns=["TEAMS","PLAYER","EVENT"])#,"LEN_EVENT"])
    for i in range(len(df)):
        if(len(df.iloc[i,2].split()) > 3):
            #print(df.iloc[i, 0] + "  " + df.iloc[i, 1] + "  " + df.iloc[i, 2])
            newDataframe1 = newDataframe1.append({"TEAMS": str(df.iloc[i,0]), "PLAYER": str(df.iloc[i,1]),"EVENT": str(df.iloc[i,2])},ignore_index=True)#, "LEN_EVENT": len(df.iloc[i,2].split())},ignore_index=True)


    newDataframe1.reset_index(drop=True, inplace=True)
    #newDataframe1 = newDataframe1.sort_values(by='TEAMS')
    print(newDataframe1)