import nltk 
nltk.download('punkt')
from nltk import word_tokenize
from nltk.corpus import stopwords
import sys
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
numlines = 0

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


##doesnt work on list elements yet, only lists within the list
unique_list = []
def unique(list):
	for x in list:
		if x not in unique_list:
			unique_list.append(x)
	print('the unique list length: ')
	print len(unique_list)
#############################################
# unique(list)
# print('the regular length is')
# print len(list)

####removes stop words from the list and puts in new list
rem_stopwords_list = [[word for word in sub if word not in stopwords_set] for sub in list]
#print rem_stopwords_list







