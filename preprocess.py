file = open('testfile.txt','w')
with open('train_file_cmps142_hw3', 'r') as fileinput:
   for line in fileinput:
       lines = line.lower()
       file.write(lines)
file.close() 

