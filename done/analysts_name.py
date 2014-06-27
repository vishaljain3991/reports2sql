#==========================
#PLEASE READ THE COMMENTS
#==========================
#This is one of the most important file of the lot. In the file analysts function
#is defined. With this function we extract analyst names, their designation,
#departments and positions.
 
import os
import re, nltk 

def analysts(string):
	bo=open("/home/finance/reports2sql/types.txt","ab+")
	
	foo=open(string)
	raw=foo.read()
	
	#Next, we split analysts_YYYY-MM-YY.txt into multiple lines by using \n delimiter
	sents=raw.split('\n' );
	
	#We also tokenize the file into words
	words=nltk.word_tokenize(raw); 
	foo.close()
	
	#sents1 contains all the places in which Moody's have offices.
	sents1=['Boston', 'Buenos Aires', 'Chicago', 'Dallas', 'Mexico City', 'New York', 'Sao Paulo', 'San Francisco', 'Toronto', 'Dubai', 'Frankfurt', 'Johannesburg', 'Limassol', 'London', 'Madrid', 'Milan', 'Moscow', 'Paris', 'Warsaw', 'Beijing', 'Hong Kong', 'Seoul', 'Shanghai', 'Singapore', 'Sydney', 'Tokyo', 'India', 'Giza', 'Tel Aviv', 'Montreal', 'Toronto', 'South San Francisco', 'West Chester', 'Edinburgh', 'Grenoble', 'Port Louis', 'Saint Cloud', 'Melbourne', 'Shenzhen', 'New', 'Hong','Jersey City', 'DIFC', 'DIFC - Dubai','Frankfurt am Main']
	
	i=0
	
	#Firstly we count the no. of times a place has been a token in sents 
	for t in sents:
		 if(t in sents1):
		 	i=i+1
	#Secondly we count the number of tokens which have JOURNALISTS mentioned.
	g=0	 	
	for t in sents:
		if(re.search('.*JOURNALISTS.*', t)): 
			g=g+1
	#Now comes the most important part of the code. Here we decide which methodology
	#to choose for extraxting the features depending on the value of i and g
	
	#if i=2 and j is free to have any value
	#so analysts_YYYY-MM-YY.txt file looks somewhat like this as in the example shown
	#below
	#--------------------------------
	#	New York
	#	Michael Levesque
	#	Senior Vice President
	#	Corporate Finance Group
	#	Moody's Investors Service
	#	JOURNALISTS: 212-553-0376
	#	SUBSCRIBERS: 212-553-1653

	#	New York
	#	Lenny J. Ajzenman
	#	Senior Vice President
	#	Corporate Finance Group
	#	Moody's Investors Service
	#	JOURNALISTS: 212-553-0376
	#	SUBSCRIBERS: 212-553-1653

	#	Moody's Investors Service
	#	250 Greenwich Street
	#	New York, NY 10007
	#	U.S.A.
	#	JOURNALISTS: 212-553-0376
	#	SUBSCRIBERS: 212-553-1653
	#--------------------------------
	
	if (i==2):
		count=0
		k=0
		while(k<len(sents)):
			#Next we search whether any of the tokens is in sents1. If we find such 
			#token, we immediately know that the succeding sentences are name of the 
			#analyst, his designation and department.
			if(sents[k] in sents1):
			
				count=count+1
				if(count%2==1):
					#a contains information for the first analyst.
					a=[sents[k], sents[k+1], sents[k+2],sents[k+3]]
				else:
					#b contains information for the second analyst.
					b=[sents[k], sents[k+1], sents[k+2],sents[k+3]]
					
					#We concatenate a and b to form t that contains 
					#info about both the analyst.
					t=a+b
					
					#In the next while loop, actually find those
					#entries in t that have apostrophe and remove it. 
					#This is done to ensure that the entries with
					#apostrophe are actually entered in the database.
					#If we try to enter the data, POSTGRES throws an
					#error. I could not find an alternate way to avoid 
					#error.
					j=0
					while(j<len(t)):
						if("'" in t[j]):
							t[j]=t[j][:t[j].index("'")]+t[j][t[j].index("'")+1:]
							print t[j]
					
						j=j+1

						
			
					foo.close()
					return t
		
			k=k+1
			
	#When i=0 (Ignore g=3). 
	#For e.g. analysts_YYYY-MM-YY.txt file looks somewhat like these
	#------------------------------------------------
	#	Michael Levesque, CFA			
	#	Senior Vice President
	#	Corporate Finance Group
	#	Moody's Investors Service, Inc.
	#	250 Greenwich Street
	#	New York, NY 10007
	#	U.S.A.
	#	JOURNALISTS: 212-553-0376
	#	SUBSCRIBERS: 212-553-1653

	#	Peter H. Abdill, CFA
	#	MD - Corporate Finance
	#	Corporate Finance Group
	#	JOURNALISTS: 212-553-0376
	#	SUBSCRIBERS: 212-553-1653

	#	Releasing Office:
	#	Moody's Investors Service, Inc.
	#	250 Greenwich Street
	#	New York, NY 10007
	#	U.S.A.
	#	JOURNALISTS: 212-553-0376
	#	SUBSCRIBERS: 212-553-1653
	#--------------------------------------------------
	#	Michael J. Mulvaney
	#	Managing Director
	#	Corporate Finance Group
	#
	#	Charles X. Tan
	#	Vice President - Senior Analyst
	#	Corporate Finance Group
	#--------------------------------------------------
	elif(i==0 or g==3):
		k=0
		pi=0	#place index if 1 that means a place found
		while(k<len(words)):
			#We determine whether any of the words that we obtained by tokenization
			#is a location.
			if (words[k] in sents1):
				pi=pi+1
				#If a word happens to be 'New', then the place is most probably New York
		 		if(words[k]=='New'):
		 			words[k]='New York'
		 		#If a word happens to be 'Hong', then the place is most probably Hong Kong
		 		if(words[k]=='Hong'):
		 			words[k]='Hong Kong'
		 		
		 		#place variable stores the location that was found	 	
		 		place=words[k]
		 		
			k=k+1
		
		l=0
		count=0
		
		#if we still find no word that happens to be one og the locations then the default location
		#of the analyst is New York (this is our assumption)
		if (pi==0):    
			place='New York'
		
		#a stores the relevant features of first analyst	
		a=[place,sents[0],sents[1],sents[2]]
		
		while(l<len(sents)):
			if(sents[l]=='' and count<1):
				count=count+1
				if (pi==0):
					b=['New York', sents[l+1], sents[l+2],sents[l+3]]
				else:
					b=[place, sents[l+1], sents[l+2],sents[l+3]]
				t=a+b
				
				j=0
				
				
				while(j<len(t)):
					if("'" in t[j]):
						t[j]=t[j][:t[j].index("'")]+t[j][t[j].index("'")+1:]
						print t[j]
					
					j=j+1
				foo.close()
				return t
			l=l+1
			
			
	#When i=1 and initial sentence is a location in sents1
	#For e.g. analysts_YYYY-MM-YY.txt file looks somewhat like this
	#---------------------------------
	#	New York
	#	Pamela Stumpp
	#	Managing Director
	#	Corporate Finance Group
	#	Moody's Investors Service
	#	JOURNALISTS: 212-553-0376
	#	SUBSCRIBERS: 212-553-1653
	#
	#	Thomas S. Coleman
	#	Senior Vice President
	#	Corporate Finance Group	
	#----------------------------------	
	elif(i==1 and (sents[0] in sents1)):
		a=[sents[0],sents[1],sents[2],sents[3]]
		k=0
		while(k<len(sents)):
			if(sents[k] in sents1):
				
				b=[sents[k], sents[k+1], sents[k+2],sents[k+3]]
				t=a+b
				
				j=0
				while(j<len(t)):
					if("'" in t[j]):
						t[j]=t[j][:t[j].index("'")]+t[j][t[j].index("'")+1:]
						print t[j]
					
					j=j+1

						
			
				foo.close()
				return t
		
			k=k+1
			
	#When i=1 and initial sentence is not a location in sents1
	#For e.g. analysts_YYYY-MM-YY.txt file looks somewhat like this
	#-----------------------------------
	#	Mark Gray
	#	Managing Director
	#	Corporate Finance Group
	#
	#	New York
	#	David Neuhaus
	#	VP - Senior Credit Officer
	#	Corporate Finance Group
	#	Moody's Investors Service
	#	JOURNALISTS: 212-553-0376
	#	SUBSCRIBERS: 212-553-1653
	#-----------------------------------
	elif(i==1 and (sents[0] not in sents1)):
		k=0
		print 'yes'
		while(k<len(sents)):
			if(sents[k] in sents1):
				b=[sents[k], sents[k+1], sents[k+2],sents[k+3]]
				a=[sents[k],sents[0],sents[1],sents[2]]
				t=a+b
				
				j=0
				while(j<len(t)):
					if("'" in t[j]):
						t[j]=t[j][:t[j].index("'")]+t[j][t[j].index("'")+1:]
						print t[j]
					
					j=j+1

						
			
				foo.close()
				return t
		
			k=k+1
	
	print t
	foo.close()
	bo.close()
