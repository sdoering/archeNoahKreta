# Documentation 

## MISC

This tool will be named **bentham**. Referring to [Jeremy Bentham](https://de.wikipedia.org/wiki/Jeremy_Bentham) inventor of the [Panopticon](https://de.wikipedia.org/wiki/Panopticon) referred to by  [Michel Foucault](https://de.wikipedia.org/wiki/Michel_Foucault#.C3.9Cberwachen_und_Strafen). 

## Existing examples of Digital Checkup presentations
* Occhio
* Red Bull Mediahouse
* SWC
* IWC

## Learnings 
* manually preparing the data, creating the graphs and making them look good is the biggest time sink
* Making the presentation look good comes in second

## Dimensions of Report

### SEO
* Redirects (crawling)
* Visibilits (sistrix)
* Title & Description
* Code to Content 
* Code Quality (duplicate h1 and such)
* Documents Indexed
* Content length

### SOCIAL

* Facebook Mentions
* Facebook Likes
* Facebook Fanpage performance 
* Facebook Links
* Twitter Mentions 
* Twitter Links
* Google+ 
* LinkedIn
* Instagram
* Sentiment & Media Mentions (2nd phase)

### TECHNICAL PERFORMANCE

* Time to first byte
* Use persistent connection
* Use GZIP compression
* Use CDN for static assets
* Use browser caching
* Use SVGs for where possible
* Mobile & Desktop Performance

### ANALYTICS IMPLEMENTATION

* Code Version
* Tools
* Tagmanagement
* Interaction Tracking
* Video Tracking
* Goals
* Filters (internal traffic) 
* Attribution

## Used Services

* sistrix
* Google Pagespeed
* ySlow (tbd)
* GT Metrics (tbd)
* webpagetest.org (tbd)

## Digital Checkup

### Introduction
The code is being maintained by Sven Döring (sven.doering@sinnerschrader.com). It is source controlled via git. API credentials are to be found in _config/credentials/apiCredentials.json_.

_bantham_ is being developed in Python 3.5. 

#### Necessary python libs 

* [pandas](http://pandas.pydata.org/pandas-docs/stable/)
* [Requests](http://docs.python-requests.org/en/master/)
* [plotly (offline)](https://plot.ly/python/)
* [beautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* MAYBE: [Tablib](http://docs.python-tablib.org/en/latest/tutorial/)
* MAYBE: something for data storage (records for sql. Or something for elastic-search or such stuff)

#### Style
* [pep8](http://pep8.org/)




