from setuptools import setup, find_packages

VERSION = '0.0.1'

setup (
    name='airkoreaPy',
    version=VERSION,
    packages=find_packages(),
    include_package_data = True,
    description='AirKorea Open API python wrapper'
)
