# -*- coding: utf-8 -*-
import sys;
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from wordExpansion import *


def main():
	# Present input parameters.
	client_key = sys.argv[1]
	engine_key = sys.argv[2]
	precision = sys.argv[3]
	query = ' '.join(sys.argv[4:])

	service = build("customsearch", "v1",
			developerKey=client_key)

	# Present top-10 results and mark relevance in each iteration.
	# Call expandWords implemented by Rocchio Algorithm to expand query.
	# Terminate if precision >= target value or precision is zero.
	while True:
		print('Parameters:')
		print('Client key = ' + client_key)
		print('Engine key = ' + engine_key)
		print('Query      = ' + query)
		print('Precision  = ' + precision)
		print('Google Search Results:')
		print('=======================')

		with open('transcript.txt', 'a') as file:
			file.write('Parameters:\n')
			file.write('Client key = ' + client_key + '\n')
			file.write('Engine key = ' + engine_key + '\n')
			file.write('Query      = ' + query + '\n')
			file.write('Precision  = ' + precision + '\n')
			file.write('=======================\n')

		res = service.cse().list(
			q = query,
			cx = engine_key,
		).execute()

		doc = []
		relevant = []
		for i,item in enumerate(res['items']):
			print 'Result '+str(i+1)
			print '['
			print ' URL: '+item['formattedUrl']
			print ' Title: '+BeautifulSoup(item['htmlTitle'], "html.parser").text
			print ' Description: '+BeautifulSoup(item['htmlSnippet'], "html.parser").text
			print ']'
			print ''
			tmp = raw_input('Relevant (Y/N):?')
			while tmp != 'y' and tmp != 'n' and tmp != 'N' and tmp != 'Y':
				print 'Invalid input, please enter again.'
				tmp = raw_input('Relevant (Y/N):?')

			print ''
			with open('transcript.txt', 'a') as file:
				file.write('Result ' + str(i + 1) + '\n')
				file.write('[\n')
				file.write(' URL: ' + item['formattedUrl'].encode('utf-8') + '\n')
				file.write(' Title: ' + BeautifulSoup(item['htmlTitle'], "html.parser").text.encode('utf-8') + '\n')
				file.write(
					' Description: ' + BeautifulSoup(item['htmlSnippet'], "html.parser").text.encode('utf-8') + '\n')
				file.write(']' + '\n')
				file.write('Relevant (Y/N):? ' + tmp.lower() + '\n')
				file.write('\n')

			if tmp.lower() == 'y':
				relevant.append(1)
			else:
				relevant.append(0)
			doc.append(BeautifulSoup(item['htmlSnippet'], "html.parser").text)

			count = 0
			for i in relevant:
				if i == 1: count += 1
			count = count / 10.0

		query = expandWords(doc, relevant, query, count, float(precision))
		if count >= float(precision) or count == 0:
			return 


if __name__ == '__main__':
	main()