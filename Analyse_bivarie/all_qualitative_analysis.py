from Analyse_bivarie.FUNCTIONS import *

if __name__ == '__main__':

    filename = '../WorldCupMatches.csv'
    dataframe = getDataframe(filename)

    print("Is there a link between Stage and Goals?")

    dataframe2 = pd.DataFrame();
    dataframe2['Goals'] = (dataframe["Home Team Goals"] + dataframe["Away Team Goals"])
    dataframe2['Stage'] = dataframe["Stage"]

    print(dataframe2)

    var1 = dataframe2.columns.get_loc("Goals")
    var2 = dataframe2.columns.get_loc("Stage")

    t = contegenceTable(dataframe2,var1,var2)
    print(t)
    t.to_excel("goals_by_stage.xlsx")
    print()

    print("Is there a link between Stage and Goals?")

    dataframe2 = pd.DataFrame();
    dataframe2['Goals'] = (dataframe["Home Team Goals"] + dataframe["Away Team Goals"])
    dataframe2['Year'] = dataframe["Year"]

    print(dataframe2)

    var1 = dataframe2.columns.get_loc("Goals")
    var2 = dataframe2.columns.get_loc("Year")

    t = contegenceTable(dataframe2, var1, var2)
    print(t)
    t.to_excel("goals_by_year.xlsx")
    print()

    print("Is there a link between Hour of the day and Goals?")

    dataframe2 = pd.DataFrame();
    dataframe2['Goals'] = (dataframe["Home Team Goals"] + dataframe["Away Team Goals"])
    dataframe2['Hour'] = dataframe["Datetime"].str[-6:-1]
    print(dataframe2['Hour'])

    print(dataframe2)

    var1 = dataframe2.columns.get_loc("Goals")
    var2 = dataframe2.columns.get_loc("Hour")

    t = contegenceTable(dataframe2, var1, var2)
    print(t)
    t.to_excel("goals_by_hour_of_the_day.xlsx")
    print()