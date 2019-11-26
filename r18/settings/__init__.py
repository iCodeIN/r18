"""
The basic settings for this spider
"""
from typing import Dict

BOT_NAME = "r18"

SPIDER_MODULES = ["r18.spiders"]
NEWSPIDER_MODULE = "r18.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

SPIDER_MIDDLEWARES: Dict[str, int] = {}

DOWNLOADER_MIDDLEWARES: Dict[str, int] = {}

EXTENSIONS: Dict[str, int] = {}

ITEM_PIPELINES: Dict[str, int] = {}
