import re
import io
from setuptools import setup
from setuptools.extension import Extension

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    io.open('crawl_finance/__init__.py', encoding='utf_8').read()
    ).group(1)

setup(
    author="Somdip Dey",
    author_email="somdip007-at-gmail.com",
    name='crawl_finance',
    version=__version__,
    url='https://github.com/somdipdey/Scrapping_And_Crawling_FinancialNews_For_Keywords',
    description='Financial News crawler and scrapper for useful data',
    license='MIT',
    install_requires=['matplotlib', 'numpy>=1.6.1', 'pillow', 'pandas', 'quandl', 'lxml', 'requests'],
    ext_modules=[Extension("Helper.query_integral_image",
                           ["crawl_finance/Helper/query_integral_image.c"])],
    scripts=['crawl_finance/Helper/wordcloud_cli.py'],
    packages=['crawl_finance'],
    package_data={'Source/Helper': ['DroidSansMono.ttf']}
)
