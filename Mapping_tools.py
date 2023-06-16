"""
DS 5110 Final Project
Tools that can be used to make maps in python
"""


import geopandas as gpd
from shapely.geometry import Point



def spatially_join(polygon, dataframe, groupbyfield):
    """
    Spatially joins a dataframe to a shapefile, spatially using "contain" function
    :param polygon: Shapefile to join to, represented by a geopandas object
    :param dataframe: Dataframe to join to geometry
    :param groupbyfield: What field to group data by
    :return: geodf, a geodataframe complete with crime data
    """

    # Spatially join the points to the polygons using contain function (points in polygon)
    joined = gpd.sjoin(polygon, dataframe, how='left', op='contains')
    # Dissolve to number of points per polygon
    counts = joined.groupby(groupbyfield).size()
    # Merge counts with original polygon GeoDataFrame
    geodf = polygon.merge(counts.rename("Count"),  # create a new column "Crime_incidents"
                                     left_on=groupbyfield,
                                     right_index=True,
                                     how='left')
    return geodf



def create_geodataframe(df, lat_field, long_field):
    """
    Creates a geodataframe from a pandas df with lat/long data
    :param df: pandas dataframe to convert
    :param lat_field: name of column that includes latitude points
    :param long_field: name of column that includes longitude points
    :return: geodf, a pandas geodataframe with geometry
    """
    
    
    # Convert  dataframe into a series of point objects
    points = [Point(xy) for xy in zip(df[long_field], df[lat_field])]
    # Convert that point layer into a geodataframe object
    geodf = gpd.GeoDataFrame(df, crs="EPSG:4326", geometry=points)
    
    return geodf
    