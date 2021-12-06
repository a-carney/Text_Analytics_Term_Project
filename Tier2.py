from os import write
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import io
import time
from timer import Timer

t = Timer()
t.start()

# open and read file
temp = open("abstractsTextFile.txt", "r")
data = temp.read()

# remove punctuation
tokenizer = nltk.RegexpTokenizer(r"\w+")
noPunctuation = tokenizer.tokenize(data)

#convert back to string
data = ' '.join(noPunctuation)

# declare stopwords
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(data)

filtered = []

 # remove stop words
for w in word_tokens:
    if w not in stop_words:

        filtered.append(w)
# convert back to string and turn to lowercase
data = ' '.join(filtered)
data = data.lower()

# replace key for comma as delimeter
key = "fhgiencvlaslrkdjcnskhj"
insertComma = ", "
data = data.replace(key, insertComma)

#write data into text
file = open('withDelimeterAbstracts.txt', 'w')
file.write(data)


t.stop()     
