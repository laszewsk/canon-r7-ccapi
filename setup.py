from setuptools import setup
from setuptools import find_packages
from ccapi.version import __version__

print (__version__)

setup(
    name='canon-r7-ccapi',
    version=__version__,
    install_requires=[
        'cloudmesh-common',
        'eel',
        'humanize',
        'streamlit',
        'watchdog',
        'ipywidgets',
        'requests',
    ],
    packages=find_packages(
        where='ccapi',  # '.' by default
        include=['ccapi'],  # ['*'] by default
        exclude=['examples'],  # empty by default
    ),
)