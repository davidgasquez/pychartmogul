from .enrichment import ChartMogulEnrichmentClient
from .metrics import ChartMogulMetricsClient


class ChartMogulClient:
    """API Wrapper Class"""

    def __init__(self, account_token=None, secret_key=None,
                 base_uri='https://api.chartmogul.com/', version=1):
        base_uri = base_uri + 'v' + str(version) + '/'
        self.metrics = ChartMogulMetricsClient(account_token, secret_key, base_uri)
        self.enrichment = ChartMogulEnrichmentClient(account_token, secret_key, base_uri)
