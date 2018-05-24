import nltk 
nltk.download('punkt')
from nltk import word_tokenize
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

file = open('output.txt','w')
with open('train_file_cmps142_hw3', 'r') as fileinput:
   for line in fileinput:
       lines = line.lower()
       print(word_tokenize(line))
       file.write(lines)

file.close() 

data = "All work and no play makes jack a dull boy, all work and no play"
print(word_tokenize(data))

