import os
import re, nltk 
import dates, a_name
import extract_name
from extract_name import extractor
from a_name import analysts
from dates import converter
fo = open("/home/finance/r_fil_loc.txt", "rb+")
raw=fo.read()
locs=nltk.word_tokenize(raw)
#print locs
string='a'
for t in locs:
	tokens=t.split('/')
	string=string+' '+tokens[4]
	
tok=nltk.word_tokenize(string)
tok=tok[1:]
#print tok[0]
print tok.index('761840')

print tok[tok.index('372050')+1]
