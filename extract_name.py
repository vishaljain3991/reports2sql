import os
import re, nltk 
import dates, a_name
from a_name import analysts
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
	count=0
	while(i+1<len(locations)):
		i=i+1
		if(locations[i]=='On'):
			#print locations[i-4]+locations[i-3]+locations[i-2]+locations[i-1]
			if (locations[i-3]=='P'):
				w=locations[i-7]+" "+locations[i-6]+" "+locations[i-5][2:]
				c=locations[i-1].lower()
			elif(locations[i-1]=="''"):
				w=locations[i-6]+" "+locations[i-5]+" "+locations[i-4][2:]
				c=locations[i-2].lower()
			else:
				w=locations[i-4]+" "+locations[i-3]+" "+locations[i-2][2:]
				c=locations[i-1].lower()
			string= '/home/finance/data/'+tokens[4]+'/analysts_'+converter(w)+'.txt'
			try:
				g=analysts(string) #here the analysts name alogwith their dept and posotion is returned
				cur = conn.cursor()
				#print 'INSERT INTO RATINGS VALUES ('+tokens[4]+',"'+g[0]+'","'+g[1]+'","'+g[2]+'","'+g[3]+'","'+g[4]+'","'+g[5]+'","'+converter(w)+'","'+c+'","'+locations[i+4]+'";)'
				#cur.execute('INSERT INTO RATINGS VALUES ('+tokens[4]+',"'+g[0]+'","'+g[1]+'","'+g[2]+'","'+g[3]+'","'+g[4]+'","'+g[5]+'","'+converter(w)+'","'+c+'","'+locations[i+4]+'");')
				#print "INSERT INTO RATINGS VALUES ("+tokens[4]+",'"+g[0]+"','"+g[1]+"','"+g[2]+"','"+g[3]+"','"+g[4]+"','"+g[5]+"','"+converter(w)+"','"+c+"','"+locations[i+4]+"')";
				cur.execute("INSERT INTO RATINGS VALUES ("+tokens[4]+",'"+g[0]+"','"+g[1]+"','"+g[2]+"','"+g[3]+"','"+g[4]+"','"+g[5]+"','"+converter(w)+"','"+c+"','"+locations[i+4]+"');")
				conn.commit()
				#print g
			except IOError:
				print "file not there"
				u=u+1
			except TypeError:
				print "Type error"
				u=u+1
		
			i=i+4
			if i<len(locations):
			#print locations[i]
				count=count+1
		
		elif(locations[i]=='Upgrade'):
		#print locations[i-4]+locations[i-3]+locations[i-2]+locations[i-1]
			count=count+1
			if (locations[i-3]=='P'):
				w=locations[i-7]+" "+locations[i-6]+" "+locations[i-5][2:]
				c=locations[i-1].lower()
			elif(locations[i-1]=="''"):
				w=locations[i-6]+" "+locations[i-5]+" "+locations[i-4][2:]
				c=locations[i-2].lower()
			else:
				w=locations[i-4]+" "+locations[i-3]+" "+locations[i-2][2:]
				c=locations[i-1].lower()
			string= '/home/finance/data/'+tokens[4]+'/analysts_'+converter(w)+'.txt'
			try:
				g=analysts(string)
				cur = conn.cursor()
				#print 'INSERT INTO RATINGS VALUES ('+tokens[4]+',"'+g[0]+'","'+g[1]+'","'+g[2]+'","'+g[3]+'","'+g[4]+'","'+g[5]+'","'+converter(w)+'","'+c+'","'+'Upgrade'+'";)'
				#cur.execute('INSERT INTO RATINGS VALUES ('+tokens[4]+',"'+g[0]+'","'+g[1]+'","'+g[2]+'","'+g[3]+'","'+g[4]+'","'+g[5]+'","'+converter(w)+'","'+c+'","'+'Upgrade'+'");')

				#"INSERT INTO RATINGS VALUES ("+tokens[4]+",'"+g[0]+"','"+g[1]+"','"+g[2]+"','"+g[3]+"','"+g[4]+"','"+g[5]+"','"+w+"','"+c+"','"+locations[i+4]+"')";
				cur.execute("INSERT INTO RATINGS VALUES ("+tokens[4]+",'"+g[0]+"','"+g[1]+"','"+g[2]+"','"+g[3]+"','"+g[4]+"','"+g[5]+"','"+converter(w)+"','"+c+"','"+"Upgrade"+"');")
				conn.commit()
				#print g
			except IOError:
				print "file not there"
				u=u+1
			except TypeError:
				print "Type error"
				u=u+1
			#print converter(w)
			#print locations[i-1]
		elif(locations[i]=='Downgrade'):
			#print locations[i-1]
			#print locations[i-4]+locations[i-3]+locations[i-2]+locations[i-1]
			if (locations[i-3]=='P'):
				w=locations[i-7]+" "+locations[i-6]+" "+locations[i-5][2:]
				c=locations[i-1].lower()
			elif(locations[i-1]=="''"):
				w=locations[i-6]+" "+locations[i-5]+" "+locations[i-4][2:]
				c=locations[i-2].lower()
			else:
				w=locations[i-4]+" "+locations[i-3]+" "+locations[i-2][2:]
				c=locations[i-1].lower()
			string= '/home/finance/data/'+tokens[4]+'/analysts_'+converter(w)+'.txt'
			try:
				g=analysts(string)
				cur = conn.cursor()
				#print 'INSERT INTO RATINGS VALUES ('+tokens[4]+',"'+g[0]+'","'+g[1]+'","'+g[2]+'","'+g[3]+'","'+g[4]+'","'+g[5]+'","'+converter(w)+'","'+c+'","'+'Downgrade'+'";)'
				#cur.execute('INSERT INTO RATINGS VALUES ('+tokens[4]+',"'+g[0]+'","'+g[1]+'","'+g[2]+'","'+g[3]+'","'+g[4]+'","'+g[5]+'","'+converter(w)+'","'+c+'","'+'Downgrade'+'");')

				#"INSERT INTO RATINGS VALUES ("+tokens[4]+",'"+g[0]+"','"+g[1]+"','"+g[2]+"','"+g[3]+"','"+g[4]+"','"+g[5]+"','"+w+"','"+c+"','"+locations[i+4]+"')";
				cur.execute("INSERT INTO RATINGS VALUES ("+tokens[4]+",'"+g[0]+"','"+g[1]+"','"+g[2]+"','"+g[3]+"','"+g[4]+"','"+g[5]+"','"+converter(w)+"','"+c+"','"+"Downgrade"+"');")
				
				conn.commit()
				#print g
			except IOError:
				print "file not there"
				u=u+1
			except TypeError:
				print "Type error"
				u=u+1
		#print converter(w)
			count=count+1

	#print count
	print tokens[4]
	conn.close()
	return u
"""string='30 Nov 99'
print converter(string)"""

