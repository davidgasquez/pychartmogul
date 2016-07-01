"""Python ChartMogul Metrics API Wrapper

This file implements a simple wrapper around the ChartMogul metrics API.
"""

import requests
from datetime import date

AVALIABLE_METRICS = [
    'mrr',
    'arr',
    'arpa',
    'asp',
    'customer-count',
    'customer-churn-rate',
    'mrr-churn-rate',
    'ltv'
]


class ChartMogulMetricsClient:
    """Metrics API Wrapper Class"""

    def __init__(self, account_token=None, secret_key=None,
                 base_url='https://api.chartmogul.com/v1/'):
        self.auth = (account_token, secret_key)
        self.base_url = base_url

    def _check_metric(self, metric):
        if metric not in AVALIABLE_METRICS:
            raise ValueError("Metric not available")

    def _check_dates(self, start_date, end_date):
        """Transform datetimes into properly formatted dates."""
        if isinstance(start_date, date):
            start_date = start_date.strftime('%Y-%m-%d')

        if isinstance(end_date, date):
            end_date = end_date.strftime('%Y-%m-%d')

        return start_date, end_date

    def get_metric(self, metric, start_date, end_date=date.today(),
                   interval=None, geo=None, plans=None):
        start_date, end_date = self._check_dates(start_date, end_date)

        payload = {
            'start-date': start_date,
            'end-date': end_date,
            'interval': interval,
            'geo': geo,
            'plans': plans
        }

        self._check_metric(metric)
        endpoint = self.base_url + 'metrics/' + metric
        response = requests.get(endpoint, auth=self.auth, params=payload)
        response.raise_for_status()

        return response.json()

    def get_summary(self, start_date, end_date=date.today(),
                    interval=None, geo=None, plans=None):
        start_date, end_date = self._check_dates(start_date, end_date)

        payload = {
            'start-date': start_date,
            'end-date': end_date,
            'interval': interval,
            'geo': geo,
            'plans': plans
        }

        endpoint = self.base_url + 'metrics/' + 'all'
        response = requests.get(endpoint, auth=self.auth, params=payload)
        response.raise_for_status()

        return response.json()
