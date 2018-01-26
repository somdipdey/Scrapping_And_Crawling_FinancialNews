''' You need to install lxml and requests packages in your
	python develpment environment.
	To install lxml>> pip install lxml
	To install requests>> pip install requests'''

# Function to extract and scrap a webpage by paragraphs
def extractHtml(url):
	from lxml import html
	import requests
	# Read the page content in bytes
	# and form the XPath tree structure
	page = requests.get(url)
	tree = html.fromstring(page.content)
	# Get the stub of the news article
	# More about XPath from https://www.w3schools.com/xml/xpath_syntax.asp
	articleStub = tree.xpath('//p/text()')
	return articleStub

# Function to check if the keyword (case insensetive) exists
def findKeywordCaseInsensetive(inputString, keyword):
	# Import regex
	import re
	if re.search(keyword, inputString, re.IGNORECASE):
		return True
	else:
		return False

# Function to check if the keyword (case sensetive) exists
def findKeywordCaseSensetive(inputString, keyword):
	if inputString.find(keyword) != -1:
		return True
	else:
		return False

# main function of the python script. Duh!
def main():
	# Put the following in try/catch exception handling to manage exceptions properly
	try:
		returnedValue = extractHtml(r'https://www.bloomberg.com/news/articles/2018-01-26/fast-food-joke-about-saudi-prince-backfires-for-lebanon-comedian')
	except:
		print('An error occured while parsing the provided url')
		return

	# If parsing the url was correct then start writing out the content
	print ('Article Content: ')

	# Print out the contents in seperated paragraphs
	paraNum = 1
	for stub in returnedValue:
		print(paraNum)
		print(stub, '\n')
		paraNum += 1
	
	# Check if the keyword exists in each paragraph
	paraNum = 1
	for stub in returnedValue:
		print('Paragraph number: ', paraNum, '\n')
		print(findKeywordCaseInsensetive(stub, 'national'), '\n')
		paraNum += 1
	
if __name__ == '__main__': main()