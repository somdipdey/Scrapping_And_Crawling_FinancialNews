import pandas as pd
import quandl as qd

API_KEY = 'Wy67QBC68SUjfSCFhXph'
qd.ApiConfig.api_key = API_KEY

''' Get financial market data from Quandl
based on Quandl code'''
def getData(code):
	dataFrame = qd.get(code)
	return dataFrame

''' Get financial market data from Quandl
based on Quandl code within specific time range'''
def getDataWithinDates(code, startDate, endDate):
	dataFrame = qd.get(code, start_date=startDate, end_date=endDate)
	return dataFrame

''' Get financial market data for n number
of rows from Quandl
based on Quandl code'''
def getData_NRows(code , nRows):
	dataFrame = qd.get(code, rows=nRows)
	return dataFrame

''' Get financial market data for n number
of rows from Quandl
based on Quandl code within specific time range'''
def getDataWithinDates_NRows(code, startDate, endDate, nRows):
	dataFrame = qd.get(code, start_date=startDate, end_date=endDate, rows=nRows)
	return dataFrame

def main():
	# Testing getData() function
	df = getData('WIKI/AAPL')
	print(df.head())

	# Testing getDataWithinDates_NRows() function
	df = getDataWithinDates_NRows('WIKI/AAPL', '1980-12-12', '1980-12-17', 5)
	print(df.head())

if __name__ == '__main__': main()