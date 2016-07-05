from .enrichment import ChartMogulEnrichmentClient
from .metrics import ChartMogulMetricsClient


class ChartMogulClient:
    """Metrics API Wrapper Class"""

    def __init__(self, account_token=None, secret_key=None,
                 base_url='https://api.chartmogul.com/v1/'):
        self.metrics = ChartMogulMetricsClient(account_token, secret_key, base_url)
        self.enrichment = ChartMogulEnrichmentClient(account_token, secret_key, base_url)
