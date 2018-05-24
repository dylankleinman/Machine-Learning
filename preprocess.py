import nltk 
from nltk import word_tokenize
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


list = []
file = open('output.txt','w')
with open('train_file_cmps142_hw3', 'r') as fileinput:
   for line in fileinput:
       lines = line.lower()
       file.write(lines)
       token = word_tokenize(lines)
       list.append(token)
file.close()

def unique(list):
	unique_list = []
	for x in list:
		if x not in unique_list:
			unique_list.append(x)
	print('the unique list length: ')
	print unique_list[0]
	print len(unique_list)

unique(list[0])
print('the regular length is')
print len(list)
<<<<<<< HEAD

# example_sent = ['hello','hello','there','in', 'is']
# filtered_word_list = example_sent

# for word in example_sent: # iterate over word_list
#   if word in stopwords.words('english'): 
#     filtered_word_list.remove(word)

# print('the words in example_sent with stopwords taken out:')
# print filtered_word_list

=======
>>>>>>> parent of 074cf9f... started step 3, unfinished
