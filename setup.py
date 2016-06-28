from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pychartmogul',
    version='0.1',
    description='Chartmogul Metrics API wrapper',
    author='David Gasquez',
    author_email='davidgasquez@gmail.com',
    url='https://github.com/davidgasquez/pychartmogul',
    license=license,
    packages=find_packages()
)
