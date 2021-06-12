from FUNCTIONS import *
from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha2
import pygal



def get_continent(col):
    try:
        cn_a2_code =  country_name_to_country_alpha2(col)
    except:
        cn_a2_code = 'Unknown'
    try:
        cn_continent = country_alpha2_to_continent_code(cn_a2_code)
    except:
        cn_continent = 'Unknown'


    return (cn_a2_code, cn_continent)



if __name__ == '__main__':

    filename = '../WorldCups.csv'
    dataframe = getDataframe(filename)
    WICH_COLUMN = 1
    column = getOneColumn(dataframe,WICH_COLUMN)



    #NETTOYER LES DONNE (Korea/Japan)
    newDataframe = pd.DataFrame(columns=["COUNTRY","Country","Continent"])
    for i in range(len(column)):
        c = get_continent(str(column.loc[i]).split("/")[0])
        #g = geolocate(str(column.loc[i]).split("/")[0])
        row = pd.Series({"COUNTRY": str(column.loc[i]).split("/")[0], "Country": c[0],"Continent": c[1]},name=3)
        newDataframe = newDataframe.append(row)




    print(newDataframe)
    c = getOneColumn(newDataframe,1)
    l1 = list(c)
    l2 = []
    for i in l1:
        l2.append(i.lower())

    print(l2)

    # create a world map
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = "PAYS D'ACCUEIL DE TOUTES LES COUPES DU MONDE"
    worldmap_chart.add("Pays",l2)
    worldmap_chart.render()
    worldmap_chart.render_to_file('map.svg')

