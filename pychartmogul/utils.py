"""Utils functions

This module provides utility functions that are used within pychartmogul
that are also useful for external consumption.
"""

from pandas.io.json import json_normalize


def response_to_dataframe(response, convert_to_dollars=False):
    """Transform a request response into a dataframe with some custom
    transformations.
    """
    # Get the entries
    columns = sorted(response.json()['entries'][0].keys())
    data = response.json()
    result = json_normalize(data['entries'], meta=columns)

    # Set date as index
    if 'date' in result.columns:
        result.set_index('date', inplace=True)

    # Convert to dollars numeric columns(ChartMogul gives the metrics in cents)
    if convert_to_dollars:
        columns = result.select_dtypes(include=['int64', 'float64']).columns
        result[columns] /= 100

    return result
