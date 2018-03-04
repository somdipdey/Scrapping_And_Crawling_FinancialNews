import json
from watson_developer_cloud import ToneAnalyzerV3


''' This module let's a user analyse the tone of a financial news article.
	The tones can be categorised into Anger, Sadness, Joy, Disgust, 
	Fear, Analytical, Tentative and Confident.
'''

# Use this method to analyze the tone and download the data in JSON format
def tone_analyzer(text):
	tone_analyzer = ToneAnalyzerV3(
	  version='2017-09-21',
	  username='YOUR Username',
	  password='YOUR Password'
	)

	tone = tone_analyzer.tone(tone_input=text,content_type="text/plain")

	output = json.dumps(tone, indent=2)
	return output


# Write the analysed tone in JSON to a file
def tone_analyzer_to_json(text):
	output = tone_analyzer(text)
	with open("output.json","w") as f:
		f.write(output)

# Fetch document tone in JSON format
def fetch_document_tone_in_json(text):
	output = tone_analyzer(text)
	document = json.loads(output)
	return document["document_tone"]["tones"]

# For Joy
def fetch_document_tone_for_joy(text):
	tones = fetch_document_tone_in_json(text)
	for index in range(0,len(tones)):
		if(tones[index]["tone_id"]=='joy'):
			return (tones[index]["score"] * 100)

# For sadness
def fetch_document_tone_for_sadness(text):
	tones = fetch_document_tone_in_json(text)
	for index in range(0,len(tones)):
		if(tones[index]["tone_id"]=='sadness'):
			return (tones[index]["score"] * 100)

# For anger
def fetch_document_tone_for_anger(text):
	tones = fetch_document_tone_in_json(text)
	for index in range(0,len(tones)):
		if(tones[index]["tone_id"]=='anger'):
			return (tones[index]["score"] * 100)

# For disgust
def fetch_document_tone_for_disgust(text):
	tones = fetch_document_tone_in_json(text)
	for index in range(0,len(tones)):
		if(tones[index]["tone_id"]=='disgust'):
			return (tones[index]["score"] * 100)

# For fear
def fetch_document_tone_for_fear(text):
	tones = fetch_document_tone_in_json(text)
	for index in range(0,len(tones)):
		if(tones[index]["tone_id"]=='fear'):
			return (tones[index]["score"] * 100)

# For analytical
def fetch_document_tone_for_analytical(text):
	tones = fetch_document_tone_in_json(text)
	for index in range(0,len(tones)):
		if(tones[index]["tone_id"]=='analytical'):
			return (tones[index]["score"] * 100)

# For tentative
def fetch_document_tone_for_tentative(text):
	tones = fetch_document_tone_in_json(text)
	for index in range(0,len(tones)):
		if(tones[index]["tone_id"]=='tentative'):
			return (tones[index]["score"] * 100)


# For confident
def fetch_document_tone_for_confident(text):
	tones = fetch_document_tone_in_json(text)
	for index in range(0,len(tones)):
		if(tones[index]["tone_id"]=='confident'):
			return (tones[index]["score"] * 100)

# Fetch sentences tone in JSON
def fetch_sentences_tone_in_json(text):
	output = tone_analyzer(text)
	document = json.loads(output)
	return document["sentences_tone"]

# Iterate through sentences to detect tones with more than defined% probability
def fetch_each_tone_sentences_for_probability(text, probability):
	sentences_tone=fetch_sentences_tone_in_json(text)
	return sentences_tone
	sadness_list=[]
	joy_list=[]
	disgust_list=[]
	fear_list=[]
	anger_list=[]
	analytical_list=[]
	tentative_list=[]
	confident_list=[]
	for index in range(0,len(sentences_tone)):
		emotion_foreach=sentences_tone[index]["tones"]
		for i in range(0,len(emotion_foreach)):
			if (emotion_foreach[i]["tone_id"]=='sadness'):
				if(emotion_foreach[i]["score"]*100 >= probability):
					sadness_list.insert(0,sentences_tone[index]["text"])
			if (emotion_foreach[i]["tone_id"]=='joy'):
				if(emotion_foreach[i]["score"]*100 >= probability):
					joy_list.insert(0,sentences_tone[index]["text"])
			if (emotion_foreach[i]["tone_id"]=='disgust'):
				if(emotion_foreach[i]["score"]*100 >= probability):
					disgust_list.insert(0,sentences_tone[index]["text"])
			if (emotion_foreach[i]["tone_id"]=='fear'):
				if(emotion_foreach[i]["score"]*100 >= probability):
					fear_list.insert(0,sentences_tone[index]["text"])
			if (emotion_foreach[i]["tone_id"]=='anger'):
				if(emotion_foreach[i]["score"]*100 >= probability):
					anger_list.insert(0,sentences_tone[index]["text"])
			if (emotion_foreach[i]["tone_id"]=='analytical'):
				if(emotion_foreach[i]["score"]*100 >= probability):
					analytical_list.insert(0,sentences_tone[index]["text"])
			if (emotion_foreach[i]["tone_id"]=='tentative'):
				if(emotion_foreach[i]["score"]*100 >= probability):
					tentative_list.insert(0,sentences_tone[index]["text"])
			if (emotion_foreach[i]["tone_id"]=='confident'):
				if(emotion_foreach[i]["score"]*100 >= probability):
					confident_list.insert(0,sentences_tone[index]["text"])
	return [sadness_list,joy_list,disgust_list,fear_list,anger_list,analytical_list,tentative_list,confident_list]




# Fetch general document tone
def fetch_document_tone(text):
	try:
		if(fetch_document_tone_for_joy(text) is not None):
			print('Joy: ' + str(fetch_document_tone_for_joy(text)) + ' %')
		if(fetch_document_tone_for_sadness(text) is not None):
			print('Sadness: ' + str(fetch_document_tone_for_sadness(text)) + ' %')
		if(fetch_document_tone_for_disgust(text) is not None):
			print('Disgust: ' + str(fetch_document_tone_for_disgust(text)) + ' %')
		if(fetch_document_tone_for_fear(text) is not None):
			print('Fear: ' + str(fetch_document_tone_for_fear(text)) + ' %')
		if(fetch_document_tone_for_anger(text) is not None):
			print('Anger: ' + str(fetch_document_tone_for_anger(text)) + ' %')
		if(fetch_document_tone_for_analytical(text) is not None):
			print('Analytical: ' + str(fetch_document_tone_for_analytical(text)) + ' %')
		if(fetch_document_tone_for_tentative(text) is not None):
			print('Tentative: ' + str(fetch_document_tone_for_tentative(text)) + ' %')
		if(fetch_document_tone_for_confident(text) is not None):
			print('Confident: ' + str(fetch_document_tone_for_confident(text)) + ' %')
	except:
		print('Some exception occurred!')

''' All the method are re-written with efficiency below
'''

# Write the analysed tone in JSON to a file
def tone_analyzer_to_json2(analysed_tone):
	with open("output.json","w") as f:
		f.write(analysed_tone)

# Fetch document tone in JSON format
def fetch_document_tone_in_json2(analysed_tone):
	document = json.loads(analysed_tone)
	return document["document_tone"]["tones"]

# For Joy
def fetch_document_tone_for_joy2(document_tones):
	for index in range(0,len(document_tones)):
		if(document_tones[index]["tone_id"]=='joy'):
			return (document_tones[index]["score"] * 100)

# For sadness
def fetch_document_tone_for_sadness2(document_tones):
	for index in range(0,len(document_tones)):
		if(document_tones[index]["tone_id"]=='sadness'):
			return (document_tones[index]["score"] * 100)

# For anger
def fetch_document_tone_for_anger2(document_tones):
	for index in range(0,len(document_tones)):
		if(document_tones[index]["tone_id"]=='anger'):
			return (document_tones[index]["score"] * 100)

# For disgust
def fetch_document_tone_for_disgust2(document_tones):
	for index in range(0,len(document_tones)):
		if(document_tones[index]["tone_id"]=='disgust'):
			return (document_tones[index]["score"] * 100)

# For fear
def fetch_document_tone_for_fear2(document_tones):
	for index in range(0,len(document_tones)):
		if(document_tones[index]["tone_id"]=='fear'):
			return (document_tones[index]["score"] * 100)

# For analytical
def fetch_document_tone_for_analytical2(document_tones):
	for index in range(0,len(document_tones)):
		if(document_tones[index]["tone_id"]=='analytical'):
			return (document_tones[index]["score"] * 100)

# For tentative
def fetch_document_tone_for_tentative2(document_tones):
	for index in range(0,len(document_tones)):
		if(document_tones[index]["tone_id"]=='tentative'):
			return (document_tones[index]["score"] * 100)


# For confident
def fetch_document_tone_for_confident2(document_tones):
	for index in range(0,len(document_tones)):
		if(document_tones[index]["tone_id"]=='confident'):
			return (document_tones[index]["score"] * 100)

# Fetch sentences tone in JSON
def fetch_sentences_tone_in_json2(analysed_tone):
	document = json.loads(analysed_tone)
	return document["sentences_tone"]

# Fetch general document tone
def fetch_document_tone2(document_tones):
	fetched_joy=fetch_document_tone_for_joy2(document_tones)
	fetched_sadness=fetch_document_tone_for_sadness2(document_tones)
	fetched_disgust=fetch_document_tone_for_disgust2(document_tones)
	fetched_fear=fetch_document_tone_for_fear2(document_tones)
	fetched_anger=fetch_document_tone_for_anger2(document_tones)
	fetched_analytical=fetch_document_tone_for_analytical2(document_tones)
	fetched_tentative=fetch_document_tone_for_tentative2(document_tones)
	fetched_confident=fetch_document_tone_for_confident2(document_tones)

	try:
		if(fetched_joy is not None):
			print('Joy: ' + str(fetched_joy) + ' %')
		if(fetched_sadness is not None):
			print('Sadness: ' + str(fetched_sadness) + ' %')
		if(fetched_disgust is not None):
			print('Disgust: ' + str(fetched_disgust) + ' %')
		if(fetched_fear is not None):
			print('Fear: ' + str(fetched_fear) + ' %')
		if(fetched_anger is not None):
			print('Anger: ' + str(fetched_anger) + ' %')
		if(fetched_analytical is not None):
			print('Analytical: ' + str(fetched_analytical) + ' %')
		if(fetched_tentative is not None):
			print('Tentative: ' + str(fetched_tentative) + ' %')
		if(fetched_confident is not None):
			print('Confident: ' + str(fetched_confident) + ' %')
	except:
		print('Exception occured while fetching different tones')


# Main method
def main():
	import financial_news_keyword_crawler as f_crawl
	returned_text = f_crawl.extractHtmlAsParagraph(r'https://www.bloomberg.com/news/articles/2018-01-26/fast-food-joke-about-saudi-prince-backfires-for-lebanon-comedian')
	
	#print(fetch_document_tone_in_json(returned_text))
	#analysed_tone = tone_analyzer(returned_text)
	#document_tones = fetch_document_tone_in_json2(analysed_tone)
	#fetch_document_tone2(document_tones)
	#print(fetch_sentences_tone_in_json2(analysed_tone))
	returned = fetch_each_tone_sentences_for_probability(returned_text,40.0)
	print(returned[0])
	print(returned[1])
	print(returned[2])
	print(returned[3])
	print(returned[4])
	print(returned[5])
	print(returned[6])


if __name__== '__main__': main()