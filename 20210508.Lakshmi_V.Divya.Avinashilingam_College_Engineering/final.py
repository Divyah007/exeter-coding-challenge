import time
import csv
import string 
# time start
start_time = time.time()
# dictionary a mapping from english to french
lookup = {}
with open("french_dictionary.csv") as fp:
  dict_reader = csv.DictReader(fp)
  lookup = {row["A"]:row["B"] for row in dict_reader} 
# "Printing the csv file 
#for old_value,new_value in lookup.items():
#  print(f'{old_value:>6} -> {new_value:<3}')
# Writing french Words to the file
french_words = open("french_words.txt","w")
french_words.write(str(list(lookup.values())))
french_words.close()
counts={}
# replace algorithm 
sp = open("t8.shakespeare.txt","r")
op = open("output_file.txt","w")
for line in sp:
  for word in line.split():
    word=word.lower()
    if len(word) > 1 and word[-1] in string.punctuation:
      op.write(lookup.get(word[:-1],word))
      #op.write(word[-1]+" ")
      counts[word[-1]] = counts.get(word[-1],0) +1
    else:
      op.write(lookup.get(word,word))
      op.write(" ")
      counts[word] = counts.get(word,0) +1
  op.write("\n")
end_time = time.time()
# closing files
sp.close()
op.close()
# writing counts to the file
cp = open("counts.txt","w")
allwords= {}
for word in sorted(counts):
  if counts[word] >1 and word in lookup:
    allwords[word] = counts[word]
cp.write(str(allwords))
cp.close()
# Printing Total time taken 
print("TOTAL TIME",end_time-start_time)