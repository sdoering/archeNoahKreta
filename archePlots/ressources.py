from subprocess import check_output
import json
import itertools
import re
import datetime, time

from pprint import pprint

URL = "https://mcdonalds.de"


TOOLS = {"piwik.js": "Piwik",
         "analytics.js": "Google Analytics",
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
         "b/ss/" : "Adobe Analytics",
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
         "siteintercept.qualtrics.com" : "Qualtrics",
         "inqChatLaunch302.js" : "TouchCommerce Chat",
         "tags.tiqcdn.com/utag" : "Tealium Tagmanager",
         "webtrekkHub/logic.js" : "Webtrekk",
         "xiti.com/hit.xiti" : "AT Internet",
         "pingdom.net/prum" : "Pingdom",
         "vrs.js" : "Visual Revenue",
         "tracker.js" : "TrackJS",
         "evergage.com" : "Evergage",
         "ads/ga-audiences" : "Google Audiences",
         "siteintercept.qualtrics.com/WRSiteInterceptEngine/Targeting.php" : "Qualtrics",
         "crazyegg.com" : "Crazy Egg",
         "pagefair.com" : "Page Fair",
         "tman.cgi?" : "TagMan",
         "bf-ad.net" : "Burda",
         "cdn.optimizely.com/js/" : "Optimizely",
         "bidr.io" : "Beeswax",
         "static.hotjar.com" : "Hotjar",
         "livechatinc.com/tracking.js" : "LiveChat",
         "engange.commander" : "Tag Commander",
         "cdn.smart-digital-solutions.com/NetPromoterScore/Live/nps" : "Smart Digital - NPS",
         "cdn.smart-digital-solutions.com/SmartSignals/" : "Smart Digital - Smart Signals Tagmanager",
         "piksel.com" : "piksel",
         "ebOneTag.js" : "Sizmek VersaTag",
         "scorecardresearch.com" : "ComScore",
         "static.parsely.com/p.js" : "Parse.ly"
         }


class AnalyticsToolCheck(object):
    """
    class for identifying used Analytics & Tracking tools on a given website and returning this as an
    iterable object (dict) for storage in ElasticSearch including id based on current date and domain.
    """

    def __init__(self, url: str, tools: dict):
        self._url = url
        self._result = {}
        self.__tool_list = tools

    def __ressources(self):
        """ Invisible method returning an iterable """
        result = check_output(["phantomjs", "--ssl-protocol=any", \
                               "--web-security=false", "getRessources.js", self._url])
        return json.loads(result.decode("utf-8"))

    def ressources(self):
        """ Public facing API to return self """
        result = check_output(["phantomjs", "--ssl-protocol=any", \
                               "--web-security=false", "getRessources.js", self._url])
        self._result["ressourceList"] = json.loads(result.decode("utf-8"))
        return self

    def page_timing(self):
        """ Public facing API to return self """
        result = check_output(["phantomjs", "--ssl-protocol=any", \
                               "--web-security=false", "getLoadTime.js", self._url])
        self._result["pageTiming"] = json.loads(result.decode("utf-8"))
        return self

    def analytics_tools(self):
        """ Public facing API to return self """
        self._result["analyticsTools"] = [{self.__tool_list[tool]: url} for (tool, url) in \
                  itertools.product(self.__tool_list, self.__ressources()) if tool in url]
        return self

    def build(self) -> dict:
        """ Public facing API to return result if chained with previous methods """
        domain = self._url.split(":")[-1]
        self._result["timestamp"] = datetime.datetime.isoformat(datetime.datetime.now())
        self._result["id"] = re.sub(r'\W+', '', "{}{}".format(time.strftime("%Y%m%d"), domain))
        self._result["number_of_external_ressources"] = len(self._result["ressourceList"])

        return self._result


def main():

    toolCheck = AnalyticsToolCheck(URL, TOOLS)
    tools_doc = toolCheck.analytics_tools() \
        .ressources() \
        .page_timing() \
        .build()
    pprint(tools_doc)

if __name__ == "__main__":
    main()