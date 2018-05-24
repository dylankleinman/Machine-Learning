import nltk 
nltk.download('punkt')
from nltk import word_tokenize
from nltk.corpus import stopwords
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

stop_words = set(stopwords.words("english"))
list = []
file = open('output.txt','w')
with open('train_file_cmps142_hw3', 'r') as fileinput:
   for line in fileinput:
       lines = line.lower()
       file.write(lines)
       token = word_tokenize(line)
       list.append(token)
file.close()

unique_list = []
def unique(list):
	for x in list:
		if x not in unique_list:
			unique_list.append(x)
	print('the unique list length: ')
	print unique_list




unique(list)
print('the regular length is')
print list

# example_sent = ['hello','hello','there','in', 'is']
# print list[0]
# unique(list[0])
# unique(example_sent)
# filtered_word_list = example_sent

# for word in example_sent: # iterate over word_list
#   if word in stopwords.words('english'): 
#     filtered_word_list.remove(word)

# print('the words in example_sent with stopwords taken out:')
# print filtered_word_list