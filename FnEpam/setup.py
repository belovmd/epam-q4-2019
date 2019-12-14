from setuptools import find_packages
from setuptools import setup

setup(
    name='news-parser',
    version='4.0.0',
    packages=find_packages(),
    author='Vadim Rashkevich',
    author_email='vadimrashkevich@yandex.ru',
    url='https://github.com/Solborm',
    python_requires='>=3.7',
    install_requires=['feedparser', 'ebooklib', 'lxml'],
    entry_points={
        "console_scripts": [
            "news-parser = RssReaderr.menu:main",
        ]
    }
)
