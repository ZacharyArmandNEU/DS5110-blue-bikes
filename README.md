# DS5110-blue-bikes
Final project for DS5110-Summer 1 2023. Examining Blue Bikes data

### Colab Juypiter Notebook
https://colab.research.google.com/drive/1qFO4eZAgffWXNrwQcNAzyvLOTz7wEEtY?usp=sharing


### Database file (download local copy to work with here):
[https://drive.google.com/file/d/13gERspTDxvXuUNTtXXVTk3Ie9ucDx2eU/view?usp=drive_link
](https://drive.google.com/file/d/13gERspTDxvXuUNTtXXVTk3Ie9ucDx2eU/view?usp=sharing)


### Sources

Sources: https://www.bluebikes.com/system-data

data from 2017-2022, maybe just 2017 and 2022 


blue bike station in boston, common blue bike trips,  network of stations, 

sea level(different rises) - https://data.boston.gov/dataset/36inch-sea-level-rise-high-tide

which station are flooded -- impact on blue bike stations? how many daily trips are lost? etc. 

vision zero data- crashes, heat map of crashes?, 


???? crashes and blue bike network? 


maybe bike lanes?


https://www.bluebikes.com/blog/the-data-challenge-entries


BlueBlue Projects:
https://storymaps.arcgis.com/stories/0f5fc6ed107d4c0491d24051eed77ff9
https://data.boston.gov/dataset/vision-zero-crash-records


CODE FROM CLASS:
# Plot a map of boston

import geopandas as gpd
import contextily as ctx

bos = gpd.read_file("boston.geojson")
bos = bos.to_crs(epsg=3857)
ax = bos.plot(figsize=(10, 10), alpha=0.15, edgecolor='k')
ctx.add_basemap(ax)


# Other Boston Attributes
#trees = gpd.read_file("trees.shp").to_crs(epsg=3857)
hosp = gpd.read_file("hospitals.geojson").to_crs(epsg=3857)
coll = gpd.read_file("colleges.geojson").to_crs(epsg=3857)
wifi = gpd.read_file("wifi.geojson").to_crs(epsg=3857)
bikes = gpd.read_file("bikes.geojson").to_crs(epsg=3857)
#sts = gpd.read_file("/Users/rachlin/Downloads/streets.geojson").to_crs(epsg=3857)

#trees.plot(color='green', markersize=1, ax=ax)
hosp.plot(color='pink', markersize=10, ax=ax)
coll.plot(color='purple', markersize=10, ax=ax)
wifi.plot(color='white', markersize=10, ax=ax)
bikes.plot(color='green', markersize=1, ax=ax)
#sts.plot(color='green', markersize=1, ax=ax)
