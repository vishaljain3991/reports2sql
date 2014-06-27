#==========================
#PLEASE READ THE COMMENTS
#==========================
#This file serves as an auxilliary file for the executor.py file. In this file we have 
#defined a single function extractor that takes the location of the dates file of a company
#id as input and extracts the relevant features from the analysts_YYYY-MM-YY.txt 
#file of the company for all te dates mentioned in the dates file.

#We import analysts function from analysts_name.py file. This function helps us extract the
#relevant features from analysts_YYYY-MM-YY.txt file.

#We also import psycopg2 package becuase in this filwe we are interacting with the database

#f_not.txt is a file that contains the company id along with the date on which their respective
#analysts file was not found.
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
	bo=open('f_not.txt', 'ab+')
	fo = open(root, 'rb+')
	raw=fo.read()
	
	#IN the next statement we tokenize the file that has been read to extract the dates on which
	#the reports were published.
	locations=nltk.word_tokenize(raw)
	
	#Next, we connect with the database and create an object.
	conn = psycopg2.connect(database="finance", user="finance", password="iof2014", host="127.0.0.1", port="5432")
	
	#In the following operation, we split the root string to extract the company id. In this token[4] 
	#happens to be the company id
	tokens=root.split('/')
	i=-1
	count=0
	#NOw we execute the loop to go through every date on which the report was published and extract relevant 
	#information from the analysts_YYYY-MM-YY.txt file. 
	while(i+1<len(locations)):
		i=i+1
		
		#We create a string here so that the actual location of analysts_YYYY-MM-YY.txt can be given to
		#the analysts function.
		string= '/home/finance/data/'+tokens[4]+'/analysts_'+locations[i]+'.txt'
		
		#Exception handling has been done to catch the exceptions when analysts_YYYY-MM-YY.txt is not found 
		#or there is some TypeError or IndexError.
		try:
			g=analysts(string) #here the analysts name alogwith their dept and posotion is returned
			cur = conn.cursor()
			print "INSERT INTO RATINGS2 VALUES ("+tokens[4]+",'"+g[0]+"','"+g[1]+"','"+g[2]+"','"+g[3]+"','"+g[4]+"','"+g[5]+"','"+g[6]+"','"+g[7]+"','"+locations[i]+"');"
			
			#In the next statement, we execute our sql command and insert the relevant info into the 
			#the database ratings1.
			cur.execute("INSERT INTO RATINGS2 VALUES ("+tokens[4]+",'"+g[0]+"','"+g[1]+"','"+g[2]+"','"+g[3]+"','"+g[4]+"','"+g[5]+"','"+g[6]+"','"+g[7]+"','"+locations[i]+"');")
			
			#Next, we commit the transaction that we performed previously.
			conn.commit()
			
		#Below are the exceptions that can be handled. 
		except IOError:
			print locations[i]
			print "file not there"
			u=u+1
			bo.write(tokens[4]+'\t'+locations[i]+'\n')
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

