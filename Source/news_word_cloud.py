"""
Generating a square wordcloud based on a news story.
"""

from os import path
from Helper.wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.
text = 'Damn boy!  yoyo'

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()