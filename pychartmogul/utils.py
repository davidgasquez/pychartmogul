"""Utils functions

This module provides utility functions that are used within pychartmogul
that are also useful for external consumption.
"""

from pandas.io.json import json_normalize

DOLLAR_COLUMNS = [
    'mrr',
    'mrr-churn',
    'mrr-contraction',
    'mrr-expansion',
    'mrr-new-business',
    'mrr-reactivation',
    'arr',
    'asp',
    'arpa',
    'ltv'
]


def convert_to_dollars(data):
    if data.name in DOLLAR_COLUMNS:
        data /= 100
    return data


def response_to_dataframe(data, in_dollars=False):
    """Transform a request response into a dataframe with some custom
    transformations.
    """
    # Get the entries
    columns = sorted(data['entries'][0].keys())
    result = json_normalize(data['entries'], meta=columns)

    # Set date as index
    if 'date' in result.columns:
        result.set_index('date', inplace=True)

    # Convert to dollars numeric columns(ChartMogul gives the metrics in cents)
    if in_dollars:
        result.apply(convert_to_dollars)

    return result
