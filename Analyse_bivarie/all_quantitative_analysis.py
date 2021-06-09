# from FUNCTIONS import *

from FUNCTIONS import *

if __name__ == '__main__':

    filename = '../WorldCupMatches.csv'
    dataframe = getDataframe(filename)

    print("Is there a link between Home Teams Goals and the Attendance?")

    var1 = dataframe.columns.get_loc("Home Team Goals")
    var2 = dataframe.columns.get_loc("Attendance")

    t = correlationTable(dataframe,var1,var2)
    print(t)
    print()

    print("Is there a link between Away Teams Goals and the Attendance?")

    var1 = dataframe.columns.get_loc("Away Team Goals")
    var2 = dataframe.columns.get_loc("Attendance")

    t = correlationTable(dataframe, var1, var2)
    print(t)
    print()

    print("Is there a link between Number of goals in a match and Attendance?")

    dataframe2 = pd.DataFrame();
    dataframe2['Goals'] = dataframe["Home Team Goals"] + dataframe["Away Team Goals"]
    dataframe2['Attendance'] = dataframe["Attendance"]

    print(dataframe2)

    var1 = dataframe2.columns.get_loc("Goals")
    var2 = dataframe2.columns.get_loc("Attendance")

    t = correlationTable(dataframe2, var1, var2)
    print(t)
    print()

    print("Is there a link between Home Team Goals and Away Team Goals?")

    var1 = dataframe.columns.get_loc("Home Team Goals")
    var2 = dataframe.columns.get_loc("Away Team Goals")

    t = correlationTable(dataframe,var1,var2)
    print(t)
    print()

    print("Is there a link between First Half Goals and Second Half Goals?")

    dataframe2 = pd.DataFrame();
    dataframe2['First Half Goals'] = dataframe["Half-time Home Goals"] + dataframe["Half-time Away Goals"]
    dataframe2['Second Half Goals'] = (dataframe["Home Team Goals"] + dataframe["Away Team Goals"]) - dataframe2['First Half Goals']

    print(dataframe2)

    var1 = dataframe2.columns.get_loc("First Half Goals")
    var2 = dataframe2.columns.get_loc("Second Half Goals")

    t = correlationTable(dataframe2, var1, var2)
    print(t)
    print()