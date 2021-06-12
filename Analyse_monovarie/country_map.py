from FUNCTIONS import *
from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha2
from geopy.geocoders import Nominatim
import folium
from folium.plugins import MarkerCluster
#from IPython.display import display

geolocator = Nominatim(user_agent="Analyse_monovarie")
def geolocate(country):
    try:
        # Geolocate the center of the country
        loc = geolocator.geocode(country)
        # And return latitude and longitude
        return (loc.latitude, loc.longitude)
    except:
        # Return missing value
        return np.nan


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
    newDataframe = pd.DataFrame(columns=["COUNTRY","Country","Continent","GeoLocate","Latitude","Longitude"])
    for i in range(len(column)):
        c = get_continent(str(column.loc[i]).split("/")[0])
        g = geolocate(str(column.loc[i]).split("/")[0])
        row = pd.Series({"COUNTRY": str(column.loc[i]).split("/")[0], "Country": c[0],"Continent": c[1],"GeoLocate":g,"Latitude":g[0], "Longitude":g[1]},name=6)
        newDataframe = newDataframe.append(row)




    print(newDataframe)



    # empty map
    world_map = folium.Map(tiles="cartodbpositron")
    marker_cluster = MarkerCluster().add_to(world_map)
    # for each coordinate, create circlemarker of user percent
    for i in range(len(newDataframe)):
        lat = newDataframe.iloc[i]['Latitude']
        long = newDataframe.iloc[i]['Longitude']
        radius = 5

        folium.CircleMarker(location=[lat, long], radius=radius,  fill=True).add_to(marker_cluster)
    # show the map
    print("okei start")
    world_map
    print("oky stop")