import os
import re, nltk, psycopg2 
import dates, a_name
from a_name import analysts
from dates import converter

conn = psycopg2.connect(database="finance", user="finance", password="iof2014", host="127.0.0.1", port="5432")

fo = open("/home/finance/r_fil_loc.txt", "wb+")
root = '/home/finance/data'
#print os.walk(root, topdown=False)
for path, subdirs, files in os.walk(root, topdown=False):
    for name in files:
        w=os.path.join(path, name)
        if((re.search(r'^.*ratings.txt$', w))):
        	print w
        	fo.write(w+" ")
        #print path[21:]
    #for name in subdirs:
        #print(os.path.join(path, name))
        
fo.close()


