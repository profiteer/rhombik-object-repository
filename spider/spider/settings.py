# -*- coding: utf-8 -*-

# Scrapy settings for spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os
import sys
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
sys.path.append(PROJECT_PATH+"/../../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Settings.settings")

BOT_NAME = 'spider'

SPIDER_MODULES = ['spider.spiders']
NEWSPIDER_MODULE = 'spider.spiders'

ITEM_PIPELINES = {
    'spider.pipelines.saveProject': 500,
    'spider.pipelines.saveThing': 550
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'rhombik-object-repository public spider #please configure with your own name.'
