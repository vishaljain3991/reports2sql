#==========================
#PLEASE READ THE COMMENTS
#==========================
#Now we refine i.e. clean our database. In this file we open names.txt which contains the names of 
#analysts as mentioned in the analysts_YYYY-MM-YY.txt file and alongside that only first and last names
#of the analysts. This file replaces all the instances of the names of full name of analyst with their 
#first and last names.

import nltk
import os
import psycopg2
fo=open("names.txt", "rb+")
raw=fo.read()
conn = psycopg2.connect(database="finance", user="finance", password="iof2014", host="127.0.0.1", port="5432")
cur=conn.cursor()

#We split the text read from names.txt file using \n delimiter. 
sents=raw.split('\n')

#Each sentence contains the full names of analyst alongwith their first and last names. We form a
#Dictionary where a full name points to first and last name.

index={} #forming a dictionary
for sent in sents:
	if(sent!=''):
		#We split every sentence into full name and "first name and last name" on the basis
		#delimiter '#'
		t=sent.split('#')
		index[t[0]]=t[1]

#All the keys of dictionary we are basically refining our ratings1 table reducing names to just first and last names
print index['Christopher Wimmer, CFA']

#'CFA','CPA','Dr.' are the additional designations that comes with a person name, we separate them out and 
#put it in a separate column called a1_add or a2_add depending on whether the person was 1st or 2nd anlayst
#on the report.

buzz=['CFA','CPA','Dr.']
for t in index.keys():
	tokens=t.split(" ")
	
	#For every full name we determine whether there is anything common between the set of words in token
	#and the set of words in buzz. Generally, a name has only one designation if at all it has it. so 
	#if a name contains a designation the cardinality of intersected set comes out to be greater than or equal
	#to one.
	inter=list(set(tokens)&set(buzz)) #whether there is some intersection or not
	
	
	if (len(inter)>0):
		#Next, we add additional designation in a1_add or a2_add column for full names having additional desingnation
		
		cur.execute("UPDATE RATINGS1 SET A1_ADD='"+inter[0]+"' WHERE A1_NAME='"+t+"';")
		conn.commit()
		
		cur.execute("UPDATE RATINGS1 SET A2_ADD='"+inter[0]+"' WHERE A2_NAME='"+t+"';")
		conn.commit()
		
	
	#Finally we update the a1_name or a2_name column with "full name and last name" 
	cur.execute("UPDATE RATINGS1 SET A1_NAME='"+index[t]+"' WHERE A1_NAME='"+t+"';")
	conn.commit()
	cur.execute("UPDATE RATINGS1 SET A2_NAME='"+index[t]+"' WHERE A2_NAME='"+t+"';")
	conn.commit()
	
	
	
	

