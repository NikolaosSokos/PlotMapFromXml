import folium
import pandas
import xml.etree.ElementTree as ET
import plotly
import numpy as np
import pandas as pd
import io
tree = ET.parse('events2.xml')
j = 0
root = tree.getroot()
marker = []
longitudes = [] #longitude
latitudes = [] #langitude
depth = []
time = []
value=[]
for child in root:
    value.append(child.attrib.get('value'))
for child in root:
    time.append(child.attrib.get('localtime'))
for child in root:
    depth.append(child.attrib.get('depth'))
for child in root:
    longitudes.append(child.attrib.get('longitude'))
for child in root:
    latitudes.append(child.attrib.get('latitude'))
longitudes =np.array(longitudes,float)
latitudes =np.array(latitudes,float)
value = np.array(value,float)
depth = np.array(depth,float)
folium_map = folium.Map(location=[38.246639, 21.734573])
def radius_producer(value):
    if float(value)<=2 and float(value)>0:
        return 1100
    if float(value)<=4 and float(value)>2:
        return 2000
    if float(value)<=7 and float(value)>4:
        return 2500
def color_producer(depth):
    if float(depth) <= 5 and float(depth)>0:
        return 'green'
    if float(depth) < 10 and float(depth)>5:
        return 'yellow'
    elif float(depth)>=10 and float(depth)<30:
        return 'orange'
    else:
            return 'red'
for i in longitudes:
    if float(value[j]) < 7:
          (marker.append(folium.Circle(location=(latitudes[j],i) , popup=( 'Value: ' + str(value[j]) +'\n Local Time: '+time[j]+'\n Depth:'+ str(round(depth[j],3))),
                                          fill_color = color_producer(float(depth[j])), color=color_producer(float(depth[j])),radius=radius_producer(value[j]))))
          marker[j].add_to(folium_map)
          j = j+1
    else :
          (marker.append(folium.Marker(location=(latitudes[j],i), icon =folium.Icon(color=color_producer(depth[j]), icon='star', prefix='fa') ,
                                       popup=folium.Popup('Value: ' + str(value[j]) +'\n Local Time: '+str(time[j])+'\n Depth:'+ str(round(depth[j],3))))))
          marker[j].add_to(folium_map)
          j = j+1
folium_map.save("my_map.html")

