#==========================
#PLEASE READ THE COMMENTS
#==========================
#Upon execution of this python file you form a database named ratings1
#in which there are information stored about each report i.e. names of
#analysts, their positions, their departments etc.

#We import extractor function from extract_name.py file. The extractor
#function helps us in extracting important features from the report as
#mentioned in the first para.

import os
import re, nltk, psycopg2 
import dates, a_name
import extract_name
from extract_name import extractor


d=0

#In the next statement we open r_fil_date.txt file. It contains the 
#info about the location of the dates file of various company ids for 
#e.g. /home/finance/data/600045616/dates happens to be the dates file
#of the company with company id 600045616
fo = open("/home/finance/reports2sql/r_fil_date.txt", "rb+")
raw=fo.read()

#We use nltk.work_tokenize to break our raw data into tokens where each
#token is a location of dates file of a company id.
locs=nltk.word_tokenize(raw)

#We loop here to go through every date file. THen from corresponding 
#date file we extract the dates on which reports were published. From
#the reports we extract the relevant features and put it into our 
#database ratings1	
for t in locs:
	d=d+extractor(t)


