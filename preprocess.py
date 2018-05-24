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
       token = word_tokenize(line)
       list.append(token)
file.close()

def unique(list):
	unique_list = []
	for x in list:
		if x not in unique_list:
			unique_list.append(x)
	print('the unique list length: ')
	print len(unique_list)

unique(list)
print('the regular length is')
print len(list)
