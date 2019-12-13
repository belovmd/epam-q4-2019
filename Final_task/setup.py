from setuptools import setup, find_packages
from os.path import join, dirname
import rss_reader

with open(join(dirname(__file__), 'README.md'), "r") as fh:
    long_description = fh.read()

setup(
    name='rss-reader',
    version=rss_reader.__version__,
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['python==3.7', 'feedparser>=5.1.3',
                      'beautifulsoup4>=4.4.1', 'colored==1.4.2',
                      'EbookLib==0.17.1']
)
