from pandas.io.json import json_normalize


def response_to_dataframe(response, convert_to_dollars=False):
    columns = sorted(response.json()['entries'][0].keys())
    data = response.json()
    result = json_normalize(data['entries'], meta=columns)

    if 'date' in result.columns:
        result.set_index('date', inplace=True)

    if convert_to_dollars:
        columns = result.select_dtypes(include=['int64', 'float64']).columns
        result[columns] /= 100

    return result
