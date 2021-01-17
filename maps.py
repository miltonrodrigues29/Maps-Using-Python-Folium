import folium
import pandas
data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
map=folium.Map(location=[38, -99.09],zoom_start=6,tiles="stamen Terrain")
fgp=folium.FeatureGroup(name="population")
def getColor(elev):
    if elev <1000 :
        return "green"
    elif elev >= 1000 and elev <= 3000:
        return "orange"
    else:
        return "red"
fgv = folium.FeatureGroup(name="Volcanoes")
for lt,ln,el in zip (lat ,lon, elev) :
    color1=getColor(el)
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el) + " m" ,fill_color=color1,color='grey', fill_op=0.7))

fgp.add_child(folium.GeoJson(data=(open('world.json','r',encoding= 'utf-8-sig').read()), 
style_function=lambda x: { 'fillColor':'green' if x['properties']['POP2005'] < 1000000 
 else 'orange' if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map3.html")
