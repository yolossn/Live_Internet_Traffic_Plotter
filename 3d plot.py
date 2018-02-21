import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot,plot
from plotly.graph_objs import *
init_notebook_mode()

izip = zip

df_flight_paths =open("loc.txt")


flight_paths = []

scl = ['rgb(213,62,79)','rgb(244,109,67)','rgb(253,174,97)',\
       'rgb(254,224,139)','rgb(255,255,191)','rgb(230,245,152)',\
       'rgb(171,221,164)','rgb(102,194,165)','rgb(50,136,189)']

def pairwise(iterable):
    a = iter(iterable)
    return izip(a, a)

i=0
flight_paths.append(
        dict(
            type = 'scattergeo',
            locationmode = 'USA-states',
            lon = [114.1333,77.0],
            lat = [22.5333,22.0],
            mode = 'lines',
            line = dict(
                width = 1,
                color = 'red',
            ),
            opacity =1,
        )
    )
for i in df_flight_paths:
    if i=='\n':
        continue
    line=i
    #print(line)
    line=line.lstrip('[')
    line=line.rstrip(']\n')
    print(line)
    x1,y1,x2,y2= line.split(',')
    x1,y1,x2,y2=float(x1.strip(' ')),float(y1.strip(' ')),float(x2.strip(' ')),float(y2.strip(' '))
    flight_paths.append(
        dict(
            type = 'scattergeo',
            locationmode = 'IN',
            lon = [x1,x2],
            lat = [y1,y2],
            mode = 'lines',
            line = dict(
                width = 1,
                color = 'red',
            ),
            opacity =1,
        )
    )  

layout = dict(
        title = 'Contour lines over globe<br>(Click and drag to rotate)',
        showlegend = False,         
        geo = dict(
            showland = True,
            showlakes = True,
            showcountries = True,
            showocean = True,
            countrywidth = 0.5,
            landcolor = 'rgb(230, 145, 56)',
            lakecolor = 'rgb(0, 255, 255)',
            oceancolor = 'rgb(0, 255, 255)',
            projection = dict( 
                type = 'orthographic',
                rotation = dict(
                    lon = 77,
                    lat = 22,
                    roll = 0
                )            
            ),
            lonaxis = dict( 
                showgrid = True,
                gridcolor = 'rgb(102, 102, 102)',
                gridwidth = 0.5
            ),
            lataxis = dict( 
                showgrid = True,
                gridcolor = 'rgb(102, 102, 102)',
                gridwidth = 0.5
            )
        )
    )
    
print(flight_paths)
fig = dict( data=flight_paths, layout=layout )
plot( fig, validate=False, filename='d3-globe' )