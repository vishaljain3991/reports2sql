#==========================
#PLEASE READ THE COMMENTS
#==========================
#In this file we fetch the names of the analysts and create a names.txt. This file contains the full names of the
#analyst alongwith the first and last names of the analyst 
import psycopg2
import re
conn = psycopg2.connect(database="finance", user="finance", password="iof2014", host="127.0.0.1", port="5432")
print "Opened database successfully"

cur = conn.cursor()
fo=open("names.txt", "wb+")
cur.execute("SELECT * FROM RATINGS1")
rows = cur.fetchall()
l=[]
#lis=['a']
for row in rows:
	#print "Analyst 1 Name: ", row[2]
	#print "Analyst 2 Name: ", row[6], "\n"
	
   	group=[row[2],row[6]]
   	
   	l=l+group
   	
   	
a=set(l)
uni=list(a)
#print uni
#print len(uni)
for t in uni:
	#Some of the names had unicode character \xc2\xa0, so we replaced the character with a blank and
	#processed the names.
	if(re.search(r'.*\xc2\xa0.*', t)):
		t=t.replace("\xc2\xa0", " ") #replacing \xc2\xa0 with blank using str.replace method
		#print t
		
	#We split the names and basically included the first and the last token.
	tokens=t.split(" ")
	print [t,tokens[0]+' '+tokens[-1]]
	fo.write(t+' /'+tokens[0]+' '+tokens[-1]+'\n')
   
