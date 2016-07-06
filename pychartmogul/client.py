from .enrichment import ChartMogulEnrichmentClient
from .metrics import ChartMogulMetricsClient


class ChartMogulClient:
    """API Wrapper Class"""

    def __init__(self, account_token=None, secret_key=None,
                 base_uri='https://api.chartmogul.com/', version=1):
        # Append API version to URI
        base_uri = base_uri + 'v' + str(version) + '/'

        # Define metrics sub-client
        self.metrics = ChartMogulMetricsClient(account_token,
                                               secret_key, base_uri)
        # Define enrichment sub-client
        self.enrichment = ChartMogulEnrichmentClient(account_token,
                                                     secret_key, base_uri)
