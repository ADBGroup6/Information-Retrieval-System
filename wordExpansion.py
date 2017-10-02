from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from operator import add,sub

with open("stopwords.txt", "r") as f:
    stop = f.read().splitlines() 
alpha = 1
beta = 0.75
gamma = 0.15
def expandWords (doc, relevant, query, prec, target_prec):
	query_list = query.split(" ")
	for word in query_list:
		if word in stop:
			stop.remove(word)
	num = len(query_list)
	R = sum(relevant)
	NR = len(relevant) - R

	# Vectorize results using tf-idf term weighting.
	# Initialize query vector and update it based on relevant and irrelevant doc.
	vectorizer = CountVectorizer(stop_words = stop)
	corpus = doc
	X = vectorizer.fit_transform(corpus)
	res = TfidfTransformer(smooth_idf=False).fit_transform(X).toarray()

	q0 =[0]*len(vectorizer.get_feature_names())
	for word in query:
		if word in vectorizer.get_feature_names():
			q0[vectorizer.get_feature_names().index(word)] = alpha
	for i,row in enumerate(res):
		if relevant[i] == 1:
			temp = row
			temp *= beta / R
			q0 = map(add, q0, temp)
		elif relevant[i] == 0:
			temp = row
			temp *= gamma /NR
			q0 = map(sub, q0, temp)
	q0 = map(lambda  x : max(x, 0), q0)

	# Add newly derived query words and reorder words in new query.
	# Present the feedback summary according to precision rate in this iteration.
	index = sorted(range(len(q0)),key=lambda i: q0[i])[-num-2:]
	new_query = []
	augmented_word = []
	for i in index:
		new_query.append(vectorizer.get_feature_names()[i])
	query_score = {}
	for word in query_list:
		query_score[word] = q0[vectorizer.get_feature_names().index(word)]
	ptr = -1
	for key, value in sorted(query_score.iteritems(), key=lambda (k,v): (v,k), reverse = True):
		if key not in new_query:
			new_query[ptr] = key
			ptr -= 1

	for word in new_query:
		if word not in query_list:
			augmented_word.append(word)

	with open('transcript.txt', 'a') as file:
		print('=======================')
		print('FEEDBACK SUMMARY: ')
		print('Query: ' + query)
		print('Precision: ' + str(prec))
		file.write('=======================\n')
		file.write('FEEDBACK SUMMARY: \n')
		file.write('Query: ' + query + '\n')
		file.write('Precision: '+str(prec)+'\n')

		if prec < target_prec:
			print('Still below the desired precision of '+str(target_prec))
			file.write('Still below the desired precision of '+str(target_prec)+'\n')
			if prec == 0:
				print('Below desired precision, but can no longer augment the query')
				file.write('Below desired precision, but can no longer augment the query'+'\n')
			else:
				print('Indexing results ....')
				print('Augmenting by: '+' '.join(augmented_word))
				file.wirte('Indexing results ....\n')
				file.write('Augmenting by: '+' '.join(augmented_word)+'\n')
		else:
			print('Desired precision reached, done!')
			file.write('Desired precision reached, done!\n')
		print('=======================')
		file.write('=======================\n')

	return ' '.join(new_query)

