"""
Generating a square wordcloud based on a news story.
This module do utilise packages developed on Word Cloud by
Andreas Mueller, which can be found here: https://github.com/amueller/word_cloud
Article on Word Cloud: http://peekaboo-vision.blogspot.co.uk/2012/11/a-wordcloud-in-python.html

Before utilisng this module, please install the required packages.
use the setup.py in the root directory to install these dependecies.
"""

from os import path
from Helper.wordcloud import (WordCloud, get_single_color_func)
# the matplotlib way:
import matplotlib.pyplot as plt

''' pass the scrapped text from your news
	to the function news_word_cloud()
'''
def news_word_cloud(text,max_font_size=60,background_color="white"):
	# Display the generated image:

	# Generate a word cloud image &
	# set lower max_font_size
	wordcloud = WordCloud(background_color=background_color,max_font_size=max_font_size).generate(text.lower())
	plt.figure()
	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	plt.show()

def news_word_cloud_by_color(text,words_of_color,max_font_size=60,background_color="white"):
	# Display the generated image:
	default_color = 'black'

	# Generate a word cloud image &
	# set lower max_font_size
	wordcloud = WordCloud(background_color=background_color,max_font_size=max_font_size).generate(text.lower())
	grouped_color_func = GroupedColorFunc(words_of_color, default_color)
	# Apply our color function
	wordcloud.recolor(color_func=grouped_color_func)
	plt.figure()
	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	plt.show()

class GroupedColorFunc(object):
    """Create a color function object which assigns DIFFERENT SHADES of
       specified colors to certain words based on the color to words mapping.
       Uses wordcloud.get_single_color_func
       Parameters
       ----------
       color_to_words : dict(str -> list(str))
         A dictionary that maps a color to the list of words.
       default_color : str
         Color that will be assigned to a word that's not a member
         of any value from color_to_words.
    """

    def __init__(self, color_to_words, default_color):
        self.color_func_to_words = [
            (get_single_color_func(color), set(words))
            for (color, words) in color_to_words.items()]

        self.default_color_func = get_single_color_func(default_color)

    def get_color_func(self, word):
        """Returns a single_color_func associated with the word"""
        try:
            color_func = next(
                color_func for (color_func, words) in self.color_func_to_words
                if word in words)
        except StopIteration:
            color_func = self.default_color_func

        return color_func

    def __call__(self, word, **kwargs):
        return self.get_color_func(word)(word, **kwargs)

class SimpleGroupedColorFunc(object):
    """Create a color function object which assigns EXACT colors
       to certain words based on the color to words mapping
       Parameters
       ----------
       color_to_words : dict(str -> list(str))
         A dictionary that maps a color to the list of words.
       default_color : str
         Color that will be assigned to a word that's not a member
         of any value from color_to_words.
    """

    def __init__(self, color_to_words, default_color):
        self.word_to_color = {word: color
                              for (color, words) in color_to_words.items()
                              for word in words}

        self.default_color = default_color

    def __call__(self, word, **kwargs):
        return self.word_to_color.get(word, self.default_color)

def main():
	import financial_news_keyword_crawler as f_crawl
	returned_text = f_crawl.extractHtmlAsParagraph(r'https://www.bloomberg.com/news/articles/2018-01-26/fast-food-joke-about-saudi-prince-backfires-for-lebanon-comedian')
	# Create a simple word cloud based on random colors
	news_word_cloud(returned_text)

	# Create word cloud based on your preferred colors
	words_of_color = {
    # words below will be colored with a green single color function
    'green': ['information', 'people', 'saudi arabia'],
    # will be colored with a red single color function
    'red': ['one', 'bloomberg', 'fast', 'connecting', 'year']
	}
	news_word_cloud_by_color(returned_text, words_of_color)

if __name__ == '__main__': main()