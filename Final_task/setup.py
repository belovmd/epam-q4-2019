import os
import rss_reader
import setuptools

with open(os.path.join(os.path.dirname(__file__), 'README.md'), "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='rss-reader',
    version=rss_reader.__version__,
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['python==3.7', 'feedparser>=5.1.3',
                      'beautifulsoup4>=4.4.1', 'colored==1.4.2',
                      'EbookLib==0.17.1']
)
