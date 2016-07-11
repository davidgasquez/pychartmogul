# PyChartMogul

Basic Python wrapper for [ChartMogul API](https://dev.chartmogul.com/docs)

## Installation
You can use `pip` to install PyChartMogul.

```bash
pip install git+https://github.com/davidgasquez/pychartmogul
```

If you prefer, you can clone it and run the setup.py file. Use the following
commands to get a copy from Github and install all dependencies:

```bash
git clone https://github.com/davidgasquez/pychartmogul
cd pychartmogul
python setup.py install
```

## Usage

Although you don't need to know anything about the ChartMogul API to use this
module, you'll need an account token and a secret key to use it.

To use the wrapper:

```python
from pychartmogul.client import ChartMogulClient

account_token = '********************************'
secret_key = '********************************'

client = ChartMogulClient(account_token, secret_key)

client.metrics.get_metric('mrr', '2016-06-01', '2016-06-10')
client.enrichment.list_customers()
```

## Features

- Support for `datetime` instead of `str` dates.
- Response parsing to Pandas DataFrame.

#### Current Metrics

- `mrr`: Retrieves the Monthly Recurring Revenue (MRR), for the specified time period.
- `arr`: Retrieves the Annualized Run Rate (ARR), for the specified time period.
- `arpa`: Retrieves the Average Revenue Per Account (ARPA), for the specified time period.
- `asp`: Retrieves the Average Sale Price (ASP), for the specified time period.
- `customer-count`: Retrieves the number of active customers, for the specified time period.
- `customer-churn-rate`: Retrieves the Customer Churn Rate, for the specified time period.
- `mrr-churn-rate`: Retrieves the Net MRR Churn Rate, for the specified time period.
- `ltv`: Retrieves the Customer Lifetime Value (LTV), for the specified time period.

Is also possible to get a summary for a time-period:

```python
client.metrics.get_summary('2016-06-01', '2016-06-10')
```

## Roadmap

- Custom number of `Timeout` retries.
- Retrieve long periods splitting the initial request.
