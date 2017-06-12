#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This piece of software is provided "as is". Meaning I do not guarantee any of this working. 
It was produced by me - Sven Döring.
"""


import sys
import requests as r
import pandas
# import plotly as py


__all__ = ["archeNoahPlots"]
__version__ = "0.0.1"
__author__ = "Sven Doering"

ID_FUNC = lambda doc: "{}{}{}".format(doc["timestamp"], doc["site"], doc["page"])


class Kreta(object):

    """
    Building a class to make querying the GA pagespeed API easier for humans
    """
    pass

def main():

    print("Working")
    sys.exit(0)

if __name__ == "__main__":

    main()