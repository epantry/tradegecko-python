import os

from endpoints import Company, Address, Variant, Product, Order

import logging
logger = logging.getLogger(__name__)


class TradeGeckoRestClient(object):

    def __init__(self, access_token=None):
        self.access_token = access_token or os.environ.get("TRADEGECKO_ACCESS_TOKEN", None)
        self.base_uri = os.environ.get("TRADEGECKO_API_URI", 'https://api.tradegecko.com/')

        if not access_token:
            raise Exception("No TG access token. Pass into client constructor or set env var TRADEGECKO_ACCESS_TOKEN")

        # Endpoints
        self.company = Company(self.base_uri, self.access_token)
        self.address = Address(self.base_uri, self.access_token)
        self.variant = Variant(self.base_uri, self.access_token)
        self.product = Product(self.base_uri, self.access_token)
        self.order = Order(self.base_uri, self.access_token)