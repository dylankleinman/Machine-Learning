import nltk 
nltk.download('punkt')
from nltk import word_tokenize
from nltk.corpus import stopwords
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

stop_words = set(stopwords.words("english"))
list = []
rem_stopwords_list = []
stopwords_set =  set(stopwords.words('english'))
file = open('output.txt','w')
with open('train_file_cmps142_hw3', 'r') as fileinput:
   for line in fileinput:
       lines = line.lower()
       file.write(lines)
       token = word_tokenize(lines)
       list.append(token)

unique_list = []
def unique(list):
	for x in list:
		if x not in unique_list:
			unique_list.append(x)
	print('the unique list length: ')
	print len(unique_list)


unique(list)
print('the regular length is')
print len(list)

rem_stopwords_list = [[word for word in sub if word not in stopwords_set] for sub in list]
print rem_stopwords_list


# example_sent = ['hello','hello','there','in', 'is', 'dylan'],['hello','hello','there','in', 'is','alex'],['hello','hello','there','in', 'is']
# unique(example_sent)
# print ('this is the unfiltered example_sent: ')
# print example_sent

# example_sent = [[word for word in sub if word not in stopwords_set] for sub in example_sent]
# print example_sent



file.close()






