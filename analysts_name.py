import os
import re, nltk 

def analysts(string):
	bo=open("/home/finance/reports2sql/types.txt","ab+")
	#print 'yes'
	foo=open(string)
	raw=foo.read()
	sents=raw.split('\n' );
	words=nltk.word_tokenize(raw); #for splitting multiple lines
	foo.close()
	#foo=open(string1)
	#print words
	#raw=foo.read()
#print raw
#tokens=nltk.sent_tokenize(raw)
	#sents1=raw.split('\n' );
	sents1=['Boston', 'Buenos Aires', 'Chicago', 'Dallas', 'Mexico City', 'New York', 'Sao Paulo', 'San Francisco', 'Toronto', 'Dubai', 'Frankfurt', 'Johannesburg', 'Limassol', 'London', 'Madrid', 'Milan', 'Moscow', 'Paris', 'Warsaw', 'Beijing', 'Hong Kong', 'Seoul', 'Shanghai', 'Singapore', 'Sydney', 'Tokyo', 'India', 'Giza', 'Tel Aviv', 'Montreal', 'Toronto', 'South San Francisco', 'West Chester', 'Edinburgh', 'Grenoble', 'Port Louis', 'Saint Cloud', 'Melbourne', 'Shenzhen', 'New', 'Hong','Jersey City', 'DIFC', 'DIFC - Dubai','Frankfurt am Main']
	i=0
	for t in sents:
		 if(t in sents1):
		 	i=i+1
	g=0	 	
	for t in sents:
		if(re.search('.*JOURNALISTS.*', t)): 
			g=g+1
	if (i==2):
		#bo.write('------------------------------------\n'+raw+'\n'+str(i)+' '+str(j)+'\n------------------------------------\n')
		count=0
		k=0
		while(k<len(sents)):
			if(sents[k] in sents1):
			#print sents[i]
			#print i
				count=count+1
				if(count%2==1):
					a=[sents[k], sents[k+1], sents[k+2],sents[k+3]]
				else:
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
	elif(i==0 or g==3):
		k=0
		pi=0	#place index if 1 that means a place found
		while(k<len(words)):
			if (words[k] in sents1):
				pi=pi+1
		 		if(words[k]=='New'):
		 			words[k]='New York'
		 		if(words[k]=='Hong'):
		 			words[k]='Hong Kong'
		 			 	
		 		place=words[k]
		 		
			k=k+1
		
		l=0
		count=0
		
		if (pi==0):    #defalut location is New York
			place='New York'
			
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
			
			
			
	elif(i==1 and (sents[0] in sents1)):
		a=[sents[0],sents[1],sents[2],sents[3]]
		k=0
		while(k<len(sents)):
			if(sents[k] in sents1):
				#print sents[i]
				#print i
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
	elif(i==1 and (sents[0] not in sents1)):
		k=0
		print 'yes'
		while(k<len(sents)):
			if(sents[k] in sents1):
				#print sents[i]
				#print i
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
