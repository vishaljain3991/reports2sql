import os
import re, nltk, psycopg2 

fo = open("/home/finance/reports2sql/r_fil_date.txt", "wb+")
root = '/home/finance/data'
#print os.walk(root, topdown=False)
for path, subdirs, files in os.walk(root, topdown=False):
    for name in files:
        w=os.path.join(path, name)
        if((re.search(r'^.*dates$', w))):
        	print w
        	fo.write(w+" ")
        #print path[21:]
    #for name in subdirs:
        #print(os.path.join(path, name))
        
fo.close()


