from ssaha_algo import ssahaFind
from bruteforce_algo import bruteFind
import time

fileName = input("Please type the source file name in fna format (eg. example.fna)") # must be in the same directory

source_file = open(fileName, "r")
source_contents = source_file.readlines() # should be a list now

#preprocessing source file
source_contents = source_contents[1:] # deletes all characters before \n
source_file_processed=''.join(line.rstrip() for line in source_contents)
string_list = list(source_file_processed)
for i in range(0, len(string_list)):
    if string_list[i] not in ['A', 'C', 'G', 'T', 'a', 'c', 'g', 't']:
        string_list[i] = 'Z'
    elif string_list[i].isupper() == False:
        string_list[i] = string_list[i].upper()
source_file_processed = ''.join(string_list)



fileName = input("Please type the key file name in txt format (eg. example.txt)") # must be in the same directory

query_file = open(fileName, "r")
query_contents = query_file.readlines() # returns string
query_contents_processed=''.join(line.rstrip() for line in query_contents)

# testing algorithm
start = time.perf_counter()
print(bruteFind(source_file_processed, query_contents_processed)) #call the function
stop = time.perf_counter()
clock = stop-start
print(clock)


print(ssahaFind(source_file_processed, query_contents_processed)) #call the function
