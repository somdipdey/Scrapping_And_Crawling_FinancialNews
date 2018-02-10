# Scrapping And Crawling Financial News

#### Build for Linux and OSX:
[![Build Status](https://travis-ci.org/somdipdey/Scrapping_And_Crawling_FinancialNews_For_Keywords.svg?branch=master)](https://travis-ci.org/somdipdey/Scrapping_And_Crawling_FinancialNews_For_Keywords)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://github.com/somdipdey/Scrapping_And_Crawling_FinancialNews_For_Keywords/blob/master/LICENSE)

An umbrella project, comprising of several different modules, to scrap and crawl financial news for useful/relevant information.

## Installation

Install the following packages before you can start using them::

		>> pip install lxml
		>> pip install requests
		>> pip install pandas
		>> pip install quandl
		>> pip install matplotlib
		>> pip install numpy>=1.6.1
		>> pip install pillow

Else:

		>> pip install -r requirements.txt

#### To install this package manually:
Download the package from https://github.com/somdipdey/Scrapping_And_Crawling_FinancialNews_For_Keywords.git

then:

		>> python setup.py install

## Usage

#### Using Word Cloud to visualise the news article (Module: news_word_cloud)

###### Example:

The news article on "Fast-Food Joke About Saudi Prince Backfires for Lebanon Comedian" available at https://www.bloomberg.com/news/articles/2018-01-26/fast-food-joke-about-saudi-prince-backfires-for-lebanon-comedian  can be visualised as follows:

![Word Cloud on Bloomberg Article](https://user-images.githubusercontent.com/8515608/36053428-9aee79f8-0de9-11e8-9b80-770f82d16c3c.png)

#### Using Word Cloud to visualise the news article with specific keywords appearing in specific colors (Module: news_word_cloud.news_word_cloud_by_color)

###### Example:

The news article on "Fast-Food Joke About Saudi Prince Backfires for Lebanon Comedian" available at https://www.bloomberg.com/news/articles/2018-01-26/fast-food-joke-about-saudi-prince-backfires-for-lebanon-comedian  can be visualised as follows:

![Word Cloud on Bloomberg Article with only two tone colors](https://user-images.githubusercontent.com/8515608/36055502-ca7edfea-0df4-11e8-851c-d75cd1db8cf3.png)


#### Using Keyword Crawler to extract/check if the news article contains the keyword(s) (Module: financial_news_keyword_crawler)

###### Example:

The news article on "Fast-Food Joke About Saudi Prince Backfires for Lebanon Comedian" available at https://www.bloomberg.com/news/articles/2018-01-26/fast-food-joke-about-saudi-prince-backfires-for-lebanon-comedian is searched for keyword "national" and the result is as follows:

		Paragraph number:  1 
		False 

		Paragraph number:  2 
		False 

		Paragraph number:  3 
		False 

		Paragraph number:  4 
		False 

		Paragraph number:  5 
		False 

		Paragraph number:  6 
		False 

		Paragraph number:  7 
		False 

		Paragraph number:  8 
		False 

		Paragraph number:  9 
		False 

		Paragraph number:  10 
		False 

		Paragraph number:  11 
		False 

		Paragraph number:  12 
		False 

		Paragraph number:  13 
		False 

		Paragraph number:  14 
		False 

		Paragraph number:  15 
		True 

		Paragraph number:  16 
		False 