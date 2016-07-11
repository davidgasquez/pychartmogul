"""Python ChartMogul Enrichment API Wrapper

This file implements a simple wrapper around the ChartMogul enrichment API.
"""

import requests


class ChartMogulEnrichmentClient:
    """Enrichment API Wrapper Class"""

    def __init__(self, account_token=None, secret_key=None,
                 base_url='https://api.chartmogul.com/v1/'):
        self.auth = (account_token, secret_key)
        self.base_url = base_url

    def list_customers(self, page=1, per_page=200):

        payload = {
            'page': page,
            'per_page': per_page
        }

        endpoint = self.base_url + 'customers'

        try:
            response = requests.get(endpoint, auth=self.auth, params=payload)
        except requests.exceptions.HTTPError:
            response = requests.get(endpoint, auth=self.auth, params=payload)

        response.raise_for_status()

        return response.json()

    def get_customer(self, uuid):

        endpoint = self.base_url + 'customers/' + uuid

        try:
            response = requests.get(endpoint, auth=self.auth)
        except requests.exceptions.HTTPError:
            response = requests.get(endpoint, auth=self.auth)

        response.raise_for_status()

        return response.json()
