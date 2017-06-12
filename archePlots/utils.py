import json
from datetime import date, timedelta
from typing import Callable, Iterable

from elasticsearch import Elasticsearch
from elasticsearch import helpers as es_helpers

DYNAMIC_MAPPING_DEFINITION = """
{
  "mappings": {
    "_default_": {
      "_all": { "enabled": false },
      "dynamic_templates": [
        { "strings": {
          "match": "*",
          "match_mapping_type": "string",
          "mapping": {
            "type": "string",
            "index": "not_analyzed"
          }
        }}
      ]
    }
  }
}
"""

ANALYTICS_TOOLS = {"piwik.js": "Piwik",
         "analytics.js": "Google Analytics",
         "collect?cid": "Google Analytics",
         "ga-lite.min.js": "Google Analytics",
         "/dc.js": "Google Analytics (Doubleclick Integration",
         "ga.js": "Google Analytics",
         "gtm.js": "Google Tagmanager",
         "sitemeter.com": "Sitemeter",
         "chartbeat.com": "Chartbeat",
         "adex.js": "Adex",
         "newrelic.com": "New Relic",
         "coremetrics": "Core Metrics",
         "cnt_js.php?": "eTracker",
         "stats.wp.com": "Wordpress Stats",
         "alexametrics.com": "Alexa Ranking",
         "fastclick.net": "Fastclick",
         "brightcove.com": "Brightcove Video Stats",
         "nuggad.net/rc?nuggn=": "NuggAd",
         "webtrends.js": "Webtrends",
         "kissmetrics.com": "Kiss Metrics",
         "elqcfg.js": "Eloqua",
         "/e.js": "eTracker",
         "s_code.js": "Adobe Analytics",
         "b/ss/": "Adobe Analytics",
         "AppMeasurement.js": "Adobe Analytics",
         "s-code-contents-": "Adobe Analytics",
         "satelliteLib-": "Adobe DTM",
         "agfnielsen.js": "Nielsen",
         "iam.js": "IVW",
         "webtrekk_v3.js": "Webtrekk V3",
         "webtrekk_v2.js": "Webtrekk V2",
         "webtrekk_v1.js": "Webtrekk V1",
         "webtrekk_v4.js": "Webtrekk V4",
         "si-s.nuggad.net": "Nuggad",
         "optimizely.com/js/": "Optimizely",
         "mmcore.js": "Maxymiser",
         "visualwebsiteoptimizer.com/j.php": "VWO",
         "fbevents.js": "Facebook",
         "uz_til.js?cuid=": "UserZoom",
         "w.usabilla.com": "Usabilla",
         "adition.com/js/srp.js": "Adition",
         "google.com/pagead/ga-audiences": "DoubleClick",
         "doubleclick.net/r/collect?": "DoubleClick",
         "conversion_async.js": "Google Adservice",
         "siteintercept.qualtrics.com": "Qualtrics",
         "inqChatLaunch302.js": "TouchCommerce Chat",
         "tags.tiqcdn.com/utag": "Tealium Tagmanager",
         "webtrekkHub/logic.js": "Webtrekk",
         "xiti.com/hit.xiti": "AT Internet",
         "pingdom.net/prum": "Pingdom",
         "vrs.js": "Visual Revenue",
         "tracker.js": "TrackJS",
         "evergage.com": "Evergage",
         "ads/ga-audiences": "Google Audiences",
         "siteintercept.qualtrics.com/WRSiteInterceptEngine/Targeting.php": "Qualtrics",
         "crazyegg.com": "Crazy Egg",
         "pagefair.com": "Page Fair",
         "tman.cgi?": "TagMan",
         "bf-ad.net": "Burda",
         "cdn.optimizely.com/js/": "Optimizely",
         "bidr.io": "Beeswax",
         "static.hotjar.com": "Hotjar",
         "livechatinc.com/tracking.js": "LiveChat",
         "engange.commander": "Tag Commander",
         "cdn.smart-digital-solutions.com/NetPromoterScore/Live/nps": "Smart Digital - NPS",
         "cdn.smart-digital-solutions.com/SmartSignals/": "Smart Digital - Smart Signals Tagmanager",
         "piksel.com": "piksel",
         "ebOneTag.js": "Sizmek VersaTag",
         "scorecardresearch.com": "ComScore",
         "static.parsely.com/p.js": "Parse.ly"
         }



class EsWriter:
    """
    Class to handle upserts to a specific Elasticsearch index and type.
    """

    def __init__(self, index_name: str, type_name: str, to_doc_id: Callable[[dict], str]):
        self.__es = Elasticsearch()
        self.__index_name = index_name
        self.__type_name = type_name
        self.__to_doc_id = to_doc_id

        # Index anlegen - falls er schon existiert, erhalten wir einen
        # 400er-Response-Code, den wir ignorieren
        self.__es.indices.create(
            index=self.__index_name, ignore=400, body=DYNAMIC_MAPPING_DEFINITION)

    def upsert_single(self, document: dict):
        self.upsert([document])

    def upsert(self, documents: object) -> object:
        es_actions = map(lambda doc: self.__to_action(doc), documents)
        es_helpers.bulk(self.__es, es_actions)

    def __to_action(self, document: dict) -> dict:
        return {
            "_index": self.__index_name,
            "_type": self.__type_name,
            "_id": self.__to_doc_id(document),
            "_source": document,
            "doc_as_upsert": True
        }


class DateUtil:
    """
    Collection of functions dealing with date and time.
    """

    @staticmethod
    def create_list_of_mondays(year):
        """
        generate all days that are Mondays in the given year as sistrix calculates visibility index and other 
        metrics on any given monday
        """

        jan1 = date(year, 1, 1)

        # find first Monday (which could be this day)
        monday = jan1 + timedelta(days=(7 - jan1.weekday()) % 7)

        while True:
            if monday.year != year:
                break
            if monday >= date.today():
                break
            yield monday
            monday += timedelta(days=7)


class ConfigUtil:
    """
    Collection of functions dealing with different configurations.
    """

    @staticmethod
    def get_api_config(api_name: str) -> dict:
        with open("../config/apiConfig.json") as conf_file:
            api_config = json.load(conf_file)
        if api_name in api_config:
            return api_config[api_name]
        raise Exception("no api config for " + api_name)

    @staticmethod
    def get_site_config(site_name: str) -> dict:
        with open("../config/siteConfig.json") as conf_file:
            site_config = json.load(conf_file)
        if site_name in site_config:
            return site_config[site_name]
        raise Exception("no site config for " + site_name)

    @staticmethod
    def get_site_names():
        with open("../config/siteConfig.json") as conf_file:
            site_config = json.load(conf_file)
        return site_config.keys()
