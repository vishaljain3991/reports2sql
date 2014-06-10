import os
import re, nltk, psycopg2 
import dates, a_name
from a_name import analysts
from dates import converter

conn = psycopg2.connect(database="finance", user="finance", password="iof2014", host="127.0.0.1", port="5432")

"""fo = open("/home/finance/r_fil_loc.txt", "wb+")
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
        
fo.close()"""

"""fo = open("/home/finance/r_fil_loc.txt", "rb+")
raw=fo.read()
locations=nltk.word_tokenize(raw)
print locations
print len(locations)"""

fo = open("/home/finance/ratings.txt", "rb+")
raw=fo.read()
locations=nltk.word_tokenize(raw)
print locations
#print len(locations)

"""for t in locations:
	if (t=='On' or t=='Upgrade'):
		if 
	#elif (t.isalpha()):
		#print t"""
i=-1
count=0
while(i+1<len(locations)):
	i=i+1
	if(locations[i]=='On'):
		#print locations[i-4]+locations[i-3]+locations[i-2]+locations[i-1]
		if (locations[i-3]=='P'):
			w=locations[i-7]+" "+locations[i-6]+" "+locations[i-5][2:]
		elif(locations[i-1]=="''"):
			w=locations[i-6]+" "+locations[i-5]+" "+locations[i-4][2:]
		else:
			w=locations[i-4]+" "+locations[i-3]+" "+locations[i-2][2:]
			
		string= '/home/finance/a_data/600008820/analysts_'+converter(w)+'.txt'
		try:
			analysts(string)
		except IOError:
			print "file not there"
		
		i=i+4
		if i<len(locations):
			#print locations[i]
			count=count+1
		
	elif(locations[i]=='Upgrade'):
		#print locations[i-4]+locations[i-3]+locations[i-2]+locations[i-1]
		count=count+1
		if (locations[i-3]=='P'):
			w=locations[i-7]+" "+locations[i-6]+" "+locations[i-5][2:]
		elif(locations[i-1]=="''"):
			w=locations[i-6]+" "+locations[i-5]+" "+locations[i-4][2:]
		else:
			w=locations[i-4]+" "+locations[i-3]+" "+locations[i-2][2:]
			
		string= '/home/finance/a_data/600008820/analysts_'+converter(w)+'.txt'
		try:
			analysts(string)
		except IOError:
			print "file not there"
		#print converter(w)
		#print locations[i-1]
	elif(locations[i]=='Downgrade'):
		#print locations[i-1]
		#print locations[i-4]+locations[i-3]+locations[i-2]+locations[i-1]
		if (locations[i-3]=='P'):
			w=locations[i-7]+" "+locations[i-6]+" "+locations[i-5][2:]
		elif(locations[i-1]=="''"):
			w=locations[i-6]+" "+locations[i-5]+" "+locations[i-4][2:]
		else:
			w=locations[i-4]+" "+locations[i-3]+" "+locations[i-2][2:]
			
		string= '/home/finance/a_data/600008820/analysts_'+converter(w)+'.txt'
		try:
			analysts(string)
		except IOError:
			print "file not there"
		#print converter(w)
		count=count+1

print count
"""string='30 Nov 99'
print converter(string)"""

