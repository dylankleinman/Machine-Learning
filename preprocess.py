import nltk 
# nltk.download('punkt')
from nltk import word_tokenize
from nltk.corpus import stopwords
from compiler.ast import flatten
from nltk.stem.porter import PorterStemmer
import sys
import string
stemmer = PorterStemmer()
reload(sys)
sys.setdefaultencoding('utf-8')

stop_words = set(stopwords.words("english"))
list = []
distinct_list = []
distinct_list_2 = []
rem_stopwords_list = []
stopwords_set =  set(stopwords.words('english'))
file = open('output.txt','w')
distinct_file = open('output_distinct.txt','w')
numwords = 0
num_words= 0 

with open('train_file_cmps142_hw3', 'r') as fileinput:
	for line in fileinput:
		lines = line.lower()
		file.write(lines)
		token = word_tokenize(lines)
		list.append(token)
file.close()

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


print('the length of the list is')
print len(flatten(list))

flattened_list = flatten(list)
for word in flattened_list:
	if word not in distinct_list_2:
		distinct_list_2.append(word)
		num_words += 1

print ('the number of distinct words in list:')
print num_words

####removes stop words from the list and puts in new list
rem_stopwords_list = [[word for word in sub if word not in stopwords_set] for sub in list]
print('the number of words with stopwords removed is:')
print len(flatten(rem_stopwords_list))

# remove punctuation from list
rem_punctuation_list = [[s.rstrip(string.punctuation) for s in nested] for nested in rem_stopwords_list]
print('the list without punctuation and stopwords is(havent taken out empty elements yet): ')
print len(flatten(rem_punctuation_list))

#to remove empty elements
for test_count in rem_punctuation_list:
	test_count[:] = [item for item in test_count if item != '']
	
print('the list without punctuation and stopwords is: ')
print len(flatten(rem_punctuation_list))

words = [["game","gaming","gamed","games"],["game","gaming","gamed","games"]]
for list in words:
	for word in words:
		print word






