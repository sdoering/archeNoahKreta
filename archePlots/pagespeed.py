#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This piece of software is provided "as is". Meaning I do not guarantee any of this working. 
It was produced by me - Sven Döring - during my time at SinnerSchrader working for the Data Team
"""

import datetime
import sys

from apiclient import discovery

from bentham.utils import ConfigUtil
from bentham.utils import EsWriter

__all__ = ["PagespeedClient"]
__version__ = "0.0.1"
__author__ = "Sven Doering"
__credits__ = "Martin Holtschneider"

ID_FUNC = lambda doc: "{}{}{}".format(doc["timestamp"], doc["site"], doc["page"])


class PagespeedClient:
    """
    Building a class to make querying the GA pagespeed API easier for humans
    """

    def __init__(self, api_config: dict, site_config: dict):
        self.__client = self.__create_client(api_config)
        self._locale = site_config["pagespeed_locale"]

    @staticmethod
    def __create_client(config: dict):
        service = discovery.build(config['service'], config['version'], developerKey=config['key'])
        return service.pagespeedapi()

    def __get_raw_result(self, url: str, strategy: str):
        request = self.__client.runpagespeed(
            url=url, screenshot=None, locale=self._locale, rule=None,
            strategy=strategy, filter_third_party_resources=False)
        return request.execute()

    def get_result_doc(self, timestamp: datetime, site_name: str, page_config: dict):
        raw_result = self.__get_raw_result(page_config["url"], page_config["strategy"])

        result = dict()

        # fachlicher Schlüssel, vgl. ID_FUNC
        result["timestamp"] = timestamp.date().isoformat()
        result["site"] = site_name
        result["page"] = page_config["name"]

        result["url"] = raw_result["id"]
        result["score"] = raw_result["score"]
        result["pagestats"] = [{k: v} for k, v in raw_result["pageStats"].items()]
        result["ruleresults"] = [raw_result["formattedResults"]["ruleResults"][i]
                                 for i in raw_result["formattedResults"]["ruleResults"]]
        result["requesttime"] = datetime.datetime.now().isoformat()
        return result


def usage():
    print("USAGE:" + sys.argv[0] + " <SITE>")
    print("...with possible sites " + ", ".join(ConfigUtil.get_site_names()))


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("wrong number of parameters, given: {}, expected: {}".format(len(sys.argv) - 1, 1))
        usage()
        sys.exit(1)

    api_config = ConfigUtil.get_api_config("pagespeed")

    site_name = sys.argv[1]
    try:
        site_config = ConfigUtil.get_site_config(site_name)
    except Exception as ex:
        print("unexpected error: " + str(ex))
        usage()
        sys.exit(1)

    timestamp = datetime.datetime.now()

    # building the query for the Google Pagespeed API and requesting the result
    pagespeed_client = PagespeedClient(api_config, site_config)
    es_writer = EsWriter(site_config["pagespeed_index"], "pagespeed", ID_FUNC)

    for page_config in site_config["pagespeed_pages"]:
        pagespeed_doc = pagespeed_client.get_result_doc(timestamp, site_name, page_config)
        es_writer.upsert([pagespeed_doc])
