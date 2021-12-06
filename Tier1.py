from urllib.request import HTTPDigestAuthHandler
import Bio
from Bio import Entrez
from Bio import Medline
from io import StringIO
import time


# All three tiers use the following timer class
# For reference, the timer algorithm can be found at https://realpython.com/python-timer/#a-python-timer-class

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")


t = Timer()
t.start()

# Entrez model needs email
Entrez.email = 'alexwcarney@gmail.com'

# Create a list of topics to search
topicsToSearch = ['acute rheumatic arthritis', 'disease, lyme', 
                    'abnormalities, cardiovascular', 'knee osteoarthritis']

# Create an empty list for abstracts to be placed in
abstracts = []
# track number of abstracts found
count = 0
# key will be used later as delimeter (cannot use punctuation as it will be removed)
key = "fhgiencvlaslrkdjcnskhj"

# the following use Entrez esearch and efetch to obtain data
# Data is then passed a string through Medline using parse
for x in topicsToSearch:
    handle = Entrez.esearch(db='pubmed', term=x, 
                            api_key='7cabd17b5994f28369af9e7983b1526e8108',
                            mindate='2010', retmode='xml', retmax=20000)    
    record = Entrez.read(handle)    
    ids = record['IdList']
    ids = ",".join(ids)
    fetch = Entrez.efetch(db='pubmed', id=ids, retmode='text', rettype='medline', 
                                api_key='7cabd17b5994f28369af9e7983b1526e8108')    
    results = Medline.parse(StringIO(fetch.read()))



    # each result is added to abstract list with delimeter and search term
    for item in results:
        try:
            abstracts.append(item['AB'] + " " + key + " " + x)
            count += 1
        except:
            pass

# written into text file   
output = open("abstractsTextFile.txt", "w")

for item in abstracts:
    output.write(item + "\n\n\n\n" + key)

print("Total number of articles found:")
print(count)
t.stop()






    