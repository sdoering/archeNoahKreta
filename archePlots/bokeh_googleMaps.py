#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This piece of software is provided "as is". Meaning I do not guarantee any of this working. 
It was produced by me - Sven Döring.
"""


import sys
import requests as r
import pandas
from bokeh.io import output_file, show
from bokeh.models import (GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool,
                              BoxSelectTool)
import geopandas as gpd
from bokeh.io import output_file, show
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure
from bokeh.sampledata.sample_geojson import geojson

__all__ = ["archeNoahPlots"]
__version__ = "0.0.1"
__author__ = "Sven Doering"

ID_FUNC = lambda doc: "{}{}{}".format(doc["timestamp"], doc["site"], doc["page"])


class Kreta(object):

    """
    Building a class to make querying the GA pagespeed API easier for humans
    """
    pass

def google():

    print("Working")
    # sys.exit(0)

    coords = (35.383, 24.606)
    coords_2 = (35.22, 24.36)

    map_options = GMapOptions(lat=coords_2[0], lng=-coords_2[1], map_type="roadmap", zoom=5)

    plot = GMapPlot(x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options)
    plot.title.text = "Looking for the map"

    # For GMaps to function, Google requires you obtain and enable an API key:
    #
    #     https://developers.google.com/maps/documentation/javascript/get-api-key
    #
    # Replace the value below with your personal API key:
    plot.api_key = "AIzaSyBbO8RFHc9EC1DKSkUCrT3LiwSVD0lwFBk"

    source = ColumnDataSource(data=dict(lat=[coords[0]], lon=[coords[1]], ))

    circle = Circle(x="lon", y="lat", size=55, fill_color="red", fill_alpha=0.8, line_color=None)
    # plot.add_glyph(source, circle)

    plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
    output_file("gmap_plot.html")
    show(plot)

def geojson():
    pass

if __name__ == "__main__":

    google()