import os
import re, nltk, psycopg2 
import dates, a_name
import extract_name
from extract_name import extractor


d=0
fo = open("/home/finance/reports2sql/r_fil_date.txt", "rb+")
raw=fo.read()
locs=nltk.word_tokenize(raw)
	
for t in locs:
	d=d+extractor(t)


