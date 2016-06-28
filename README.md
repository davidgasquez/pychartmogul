# PyChartMogul
Python wrapper for [ChartMogul API](https://dev.chartmogul.com/docs)

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
from pychartmogul.metrics import ChartMogulMetrics

account_token = '********************************'
secret_key = '********************************'

wrapper = ChartMogulMetrics(account_token, secret_key)
```
