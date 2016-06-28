"""Python ChartMogul Metrics API Wrapper

This file implements a simple wrapper around the ChartMogul metrics API.
"""

import requests
from .utils import response_to_dataframe


class ChartMogulMetrics:
    """Metrics API Wrapper Class"""

    def __init__(self, account_token=None, secret_key=None):
        self.account_token = account_token
        self.secret_key = secret_key
        self.auth = (account_token, secret_key)

    def get_metric(self, metric, start_date, end_date,
                   interval=None, geo=None, plans=None):
        payload = {
            'start-date': start_date,
            'end-date': end_date,
            'interval': interval,
            'geo': geo,
            'plans': plans
        }

        endpoint = 'https://api.chartmogul.com/v1/metrics/' + metric
        response = requests.get(endpoint, auth=self.auth, params=payload)
        convert = metric in ['mrr', 'arr', 'asp', 'arpa', 'ltv']
        data = response_to_dataframe(response, convert_to_dollars=convert)
        return data

    def get_summary(self, start_date, end_date,
                    interval=None, geo=None, plans=None):
        payload = {
            'start-date': start_date,
            'end-date': end_date,
            'interval': interval,
            'geo': geo,
            'plans': plans
        }

        endpoint = 'https://api.chartmogul.com/v1/metrics/all'
        response = requests.get(endpoint, auth=self.auth, params=payload)
        data = response_to_dataframe(response)

        # TODO: Transform columns to $

        return data
