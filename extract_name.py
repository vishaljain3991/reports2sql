import os
os.chdir('/home/finance/reports2sql')
import re, nltk 
import dates, a_name
import analysts_name
from analysts_name import analysts
from dates import converter
import psycopg2 

def extractor(root):
	u=0
	fo = open(root, 'rb+')
	raw=fo.read()
	locations=nltk.word_tokenize(raw)
	conn = psycopg2.connect(database="finance", user="finance", password="iof2014", host="127.0.0.1", port="5432")
	tokens=root.split('/')
	i=-1
	#print locations
	#print tokens
	count=0
	while(i+1<len(locations)):
		i=i+1
		
			
		string= '/home/finance/data/'+tokens[4]+'/analysts_'+locations[i]+'.txt'
		try:
			g=analysts(string) #here the analysts name alogwith their dept and posotion is returned
			cur = conn.cursor()
			print "INSERT INTO RATINGS1 VALUES ("+tokens[4]+",'"+g[0]+"','"+g[1]+"','"+g[2]+"','"+g[3]+"','"+g[4]+"','"+g[5]+"','"+g[6]+"','"+g[7]+"','"+locations[i]+"');"
			cur.execute("INSERT INTO RATINGS1 VALUES ("+tokens[4]+",'"+g[0]+"','"+g[1]+"','"+g[2]+"','"+g[3]+"','"+g[4]+"','"+g[5]+"','"+g[6]+"','"+g[7]+"','"+locations[i]+"');")
			conn.commit()
			#print g
		except IOError:
			print locations[i]
			print "file not there"
			u=u+1
		except TypeError:
			print locations[i]
			print "Type error"
			u=u+1
		except IndexError:
			print "Index error"
			u=u+1
			
	print tokens[4]
	conn.close()
	return u
"""string='30 Nov 99'
print converter(string)"""

