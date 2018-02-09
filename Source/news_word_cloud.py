"""
Generating a square wordcloud based on a news story.
This module do utilise packages developed on Word Cloud by
Andreas Mueller, which can be found here: https://github.com/amueller/word_cloud
Article on Word Cloud: http://peekaboo-vision.blogspot.co.uk/2012/11/a-wordcloud-in-python.html
"""

from os import path
from Helper.wordcloud import WordCloud

''' pass the scrapped text from your news
	to the function news_word_cloud()
'''
def news_word_cloud(text,max_font_size=40,background_color="white"):
	# Generate a word cloud image
	wordcloud = WordCloud(background_color=background_color).generate(text)

	# Display the generated image:
	# the matplotlib way:
	import matplotlib.pyplot as plt
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis("off")

	# lower max_font_size
	wordcloud = WordCloud(background_color=background_color,max_font_size=max_font_size).generate(text)
	plt.figure()
	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	plt.show()

def main():
	import financial_news_keyword_crawler as f_crawl
	returned_text = f_crawl.extractHtmlAsParagraph(r'https://www.bloomberg.com/news/articles/2018-01-26/fast-food-joke-about-saudi-prince-backfires-for-lebanon-comedian')
	news_word_cloud(returned_text)

if __name__ == '__main__': main()