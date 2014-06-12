import os
import re, nltk, psycopg2 
import dates, a_name
import extract_name
from extract_name import extractor
from a_name import analysts
from dates import converter

d=0
fo = open("/home/finance/reports2sql/r_fil_date.txt", "rb+")
raw=fo.read()
locs=nltk.word_tokenize(raw)
#print locs
"""string='a'
for t in locs:
	tokens=t.split('/')
	string=string+' '+tokens[4]"""
	
for t in locs:
	d=d+extractor(t)

#print d
#conn.close()
"""tok=nltk.word_tokenize(string)
tok=tok[1:]
#print tok[0]
print tok[tok.index('413000')+1]"""
