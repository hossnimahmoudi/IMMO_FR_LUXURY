# -*- coding: utf-8 -*-

# Scrapy settings for luxury project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'luxury'

SPIDER_MODULES = ['luxury.spiders']
NEWSPIDER_MODULE = 'luxury.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'luxury (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
FEED_EXPORT_FIELDS=["ANNONCE_LINK", "FROM_SITE",    "ID_CLIENT",    "ANNONCE_DATE", "ACHAT_LOC",    "SOLD", "MAISON_APT",   "CATEGORIE",    "NEUF_IND", "NOM",  "ADRESSE",  "CP",   "VILLE",    "QUARTIER", "DEPARTEMENT",  "REGION",   "PROVINCE", "ANNONCE_TEXT", "ETAGE",    "NB_ETAGE", "LATITUDE", "LONGITUDE",    "M2_TOTALE",    "SURFACE_TERRAIN",  "NB_GARAGE",    "PHOTO",    "PIECE",    "NB_CHAMBRE",   "PISCINE",  "PRIX", "PRIX_M2",  "URL_PROMO",    "STOCK_NEUF",   "PAYS_AD",  "PRO_IND",  "SELLER_TYPE",  "MINI_SITE_URL",    "MINI_SITE_ID", "AGENCE_NOM",   "AGENCE_ADRESSE",   "AGENCE_CP",    "AGENCE_VILLE", "AGENCE_DEPARTEMENT",   "EMAIL",    "WEBSITE",  "AGENCE_TEL",   "AGENCE_TEL_2", "AGENCE_TEL_3", "AGENCE_TEL_4", "AGENCE_FAX",   "AGENCE_CONTACT",   "PAYS_DEALER",  "FLUX", "SIREN"]


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'luxury.middlewares.LuxurySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'luxury.middlewares.LuxuryDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'luxury.pipelines.LuxuryPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_IGNORE_MISSING = False(True)
#HTTPCACHE_IGNORE_HTTP_CODES = []


HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
import time, os
datee = time.strftime("%Y_%m")
pathc = '/home/a.bouyahya/CacheWares/LUXURY/' + datee
if not os.path.exists(pathc):
    os.makedirs(pathc)
HTTPCACHE_DIR = pathc
HTTPCACHE_IGNORE_HTTP_CODES = [500, 503, 504, 400, 408, 404, 413]  # Do not save 404 page...
HTTPCACHE_IGNORE_MISSING = False
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

import time, os
path = "/home/a.bouyahya/LogsWares/LUXURY/" + datee
if not os.path.exists(path):
    os.makedirs(path)
now = time.strftime("%Y%m%d_%Hh-%Mmin-%Ss")
LOG_FILE = "%s/%s_%s.log" % (path, 'Luxury', now)
###
LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'
LOG_STDOUT = True
