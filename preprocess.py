#Dylan Kleinman, Alex Angelidis
#5/26/18
#cs142 Hw3


import nltk 
# nltk.download('punkt')
from nltk import word_tokenize
from nltk.corpus import stopwords
from compiler.ast import flatten
from nltk.stem.porter import PorterStemmer
from collections import Counter
from itertools import chain
from nltk.probability import FreqDist
import sys
import string
import csv
import io

stemmer = PorterStemmer()
reload(sys)
sys.setdefaultencoding('utf-8')

stop_words = set(stopwords.words("english"))

#####list intialize
list = []
token_list = []
distinct_textfile = []
distinct_list_2 = []
rem_stopwords_list = []
filtered_list = []
##########################

stopwords_set =  set(stopwords.words('english'))
file = open('output.txt','w')
numwords_in_textfile = 0
num_words= 0 

with open('train_file_cmps142_hw3', 'r') as fileinput:
	for line in fileinput:
		lines = line.lower()
		file.write(lines)
		token = word_tokenize(lines)
		#list.append(token)
		token_list.append(token)
file.close()

label = [line[0] for line in token_list]
list = [line[1:] for line in token_list]

##count number of words in file
with open('output.txt', 'r') as file:
	for line in file:
		wordslist = line.split()
		for word in wordslist:
			if word not in distinct_textfile:
				distinct_textfile.append(word)
		numwords_in_textfile += len(wordslist)

#print('the number of words in the textfile is:')
#print numwords_in_textfile
#print('the number of distinct words in the textfile is: ')
#print len(distinct_textfile)

##prints out the number of elements in the list, and distinct elements in the list
#print('the length of the list is')
#print len(flatten(list))

flattened_list = flatten(list)
for word in flattened_list:
	if word not in distinct_list_2:
		distinct_list_2.append(word)
		num_words += 1

print ('the number of distinct words in list, answer to problem 2(a)')
print num_words
print ("\n")

####removes stop words from the list and puts in new list
rem_stopwords_list = [[word for word in sub if word not in stopwords_set] for sub in list]
#print('the number of words with stopwords removed is:')
#<<<<<<< HEAD
#print len(flatten(rem_stopwords_list))

# remove punctuation from list
rem_punctuation_list = [[s.rstrip(string.punctuation) for s in nested] for nested in rem_stopwords_list]
#print('the list without punctuation and stopwords is(havent taken out empty elements yet): ')
#print len(flatten(rem_punctuation_list))

#to remove empty elements
for test_count in rem_punctuation_list:
	test_count[:] = [item for item in test_count if item != '']
	
#print('the list without punctuation and stopwords is: ')
#print len(flatten(rem_punctuation_list))

stemmed_list = [[stemmer.stem(word) for word in nested] for nested in rem_punctuation_list] 

print ('The answer to Step 5 (a)')
print stemmed_list[10]
print ("\n")

#print('number in list after stemmed')
#print len(flatten(stemmed_list))

counted_list = []
c = Counter(chain.from_iterable(stemmed_list))
##creates list counted_list filled with all stemmed list elements that contain more than 5 iterations
for k, v in c.items():
    # print(k, v)
    if v<5:
    	counted_list.append(k)

#print('the amount of words that appear less than 5 times')
#print len(flatten(counted_list))
rem_counted_list = [[word for word in sub if word not in counted_list] for sub in stemmed_list]

#print('after removing words that appear less than 5 times')
#print len(flatten(rem_counted_list))

filtered_words = 0
flattened_list2 = flatten(rem_counted_list)
for word in flattened_list2:
	if word not in filtered_list:
		filtered_list.append(word)
		filtered_words += 1
print ('The answer to Step 6 (a)')
print filtered_words
print ("\n")

#convert to csv file
def write(file, final_list, labels, tokens):
    num_tracker = []
    freq = FreqDist([word for sublist in final_list for word in sublist])
    #block of code to get freq of word in instance
    for iter in range(0, len(final_list)):
        row_list = []
        line_freq = FreqDist(final_list[iter])
        for word in freq:
            if word in line_freq:
                row_list.append(u'{}'.format(line_freq[word]))
            else:
                row_list.append(u'0')
        num_tracker.append(row_list)

    write_list = tokens
    tokens = []
    counter = 0
    #code to write to csv file
    with io.open(file, 'w', encoding='utf8') as outfile:
    	headers = freq.keys()
    	header = ','.join(headers) 
    	label_word = ','+"label" + '\n'
    	outfile.write(header+label_word)
    	for num in num_tracker:
    		num_occurances = ','.join(num)
    		end_label = ',0,'+labels[counter] + '\n'
    		counter +=1
    		outfile.write(num_occurances+end_label)

write('HW3_Angelidis_train.csv', rem_counted_list, label, filtered_list)

##############Dylan's code
#def write(file, filtered_list, unfiltered_list, label):
#	write_list = filtered_list
#	tokens = []
#	with io.open(file, 'w', encoding='utf8') as outfile:
#		l = ','.join(write_list) + '\n'
#		outfile.write(l)
#		for w in range(0,len(unfiltered_list)):
#			l = ','.join(write_list) + '\n'
#			outfile.write(l)
############################################

#convert to csv file
#csv_file = open('testing.csv','w')
#for sublist in rem_counted_list:
#	for word in sublist:
#		csv_file.write(word+" ")
#	csv_file.write("\n")	
#csv_file.close()