import nltk 
# nltk.download('punkt')
from nltk import word_tokenize
from nltk.corpus import stopwords
import sys
import string

reload(sys)
sys.setdefaultencoding('utf-8')

stop_words = set(stopwords.words("english"))
list = []
distinct_list = []
rem_stopwords_list = []
stopwords_set =  set(stopwords.words('english'))
file = open('output.txt','w')
distinct_file = open('output_distinct.txt','w')
numwords = 0

with open('train_file_cmps142_hw3', 'r') as fileinput:
	for line in fileinput:
		lines = line.lower()
		file.write(lines)
		token = word_tokenize(lines)
		list.append(token)
file.close()
print len(list)

##count number of words in file
with open('output.txt', 'r') as file:
	for line in file:
		wordslist = line.split()
		for word in wordslist:
			if word not in distinct_list:
				distinct_list.append(word)
		numwords += len(wordslist)


print('the number of words in the textfile is:')
print numwords
print('the number of distinct words in the textfile is: ')
print len(distinct_list)

####removes stop words from the list and puts in new list
rem_stopwords_list = [[word for word in sub if word not in stopwords_set] for sub in list]
print('the number of words with stopwords removed is:')
print len(rem_stopwords_list)


rem_punctuation_list = [[s.rstrip(string.punctuation) for s in nested] for nested in rem_stopwords_list]
print('the list without punctuation and stopwords is(havent taken out empty elements yet): ')
print rem_punctuation_list







