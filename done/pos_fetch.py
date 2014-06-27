#==========================
#PLEASE READ THE COMMENTS
#==========================
#In this file we refined the dsignation columns of analysts i.e. a1_pos and a2_pos. So for e.g.
#if a designation was Sr. Vice Pres. we changed it to Senior Vice President. This was done to 
#maintain coherence in our database. Additionally if some designation was SVP- Sr. Credit Officer
#we added Senior Vice President to the a1_pos or a2_pos column and added Senior Credit Officer to 
#the a1_aux or a2_aux column.

import psycopg2
import re
conn = psycopg2.connect(database="finance", user="finance", password="iof2014", host="127.0.0.1", port="5432")
print "Opened database successfully"

cur = conn.cursor()
fo=open("names.txt", "wb+")

#We select all positions occuring in our database
cur.execute("SELECT DISTINCT A1_POS FROM RATINGS1 UNION SELECT DISTINCT A2_POS FROM RATINGS1")
rows = cur.fetchall()

#lis=['a']
j=0
k=0
for row1 in rows:
	#row1 is a tuple which is immutable. So we convert the tuple to a list.
	row=list(row1)
	if('Sr.' in row[0]):
		row[0]=row[0].replace("Sr.","Senior")
		
	elif('Sr' in row[0]):
		row[0]=row[0].replace("Sr", "Senior")
		
	#print row[0]
	j=j+1
	
	#Firstly we search for the regex S.*V.*P.* to determine whether designation is Senior Vice President
	#Then we search for the regex S.*V.*P.*-.* to determine whether there is an additional designation.
	
	if(re.search("^S.*V.*P.*", row[0])):
		
		if(re.search("S.*V.*P.*-.*", row[0])):
			
			#We search for '-' and break after that to get the additional designation
			
			i=row[0].index('-')
			i=i+1
			
			while(row[0][i]==' ' and i<len(row[0])):
				i=i+1
			#We then update a1_aux column with additional designation
			cur.execute("UPDATE RATINGS1 SET A1_AUX='"+row[0][i:]+"' WHERE A1_POS='"+row[0]+"';")
			conn.commit()
			cur.execute("UPDATE RATINGS1 SET A2_AUX='"+row[0][i:]+"' WHERE A2_POS='"+row[0]+"';")
			conn.commit()
		else:
			#print row[0]
			print 'yes'
		#Next we update the a1_pos column. For e.g. if a designation was Sr. Vice Pres. we change it to 
		#Senior Vice President
		cur.execute("UPDATE RATINGS1 SET A1_POS='"+"Senior Vice President"+"' WHERE A1_POS='"+row[0]+"';")
		conn.commit()
		cur.execute("UPDATE RATINGS1 SET A2_POS='"+"Senior Vice President"+"' WHERE A2_POS='"+row[0]+"';")
		conn.commit()
		k=k+1
		
	#As usually we search for Assistant Vice President and the procedures are same as above.
	elif(re.search("^A.*V.*P.*", row[0])):
		if(re.search("A.*V.*P.*-.*", row[0])):
			#print row[0]
			i=row[0].index('-')
			i=i+1
			#print row[0]
			while(row[0][i]==' ' and i<len(row[0])):
				i=i+1
			#print row[0][i:]
			cur.execute("UPDATE RATINGS1 SET A1_AUX='"+row[0][i:]+"' WHERE A1_POS='"+row[0]+"';")
			conn.commit()
			cur.execute("UPDATE RATINGS1 SET A2_AUX='"+row[0][i:]+"' WHERE A2_POS='"+row[0]+"';")
			conn.commit()
		else:
			#print row[0]
			print 'yes'
		cur.execute("UPDATE RATINGS1 SET A1_POS='"+"Assistant Vice President"+"' WHERE A1_POS='"+row[0]+"';")
		conn.commit()
		cur.execute("UPDATE RATINGS1 SET A2_POS='"+"Assistant Vice President"+"' WHERE A2_POS='"+row[0]+"';")
		conn.commit()
		k=k+1
	
	#As usually we search for Vice President and the procedures are same as above.
	elif(re.search("^V.*P.*", row[0])):
		if(re.search("V.*P.*-.*", row[0])):
			#print row[0]
			i=row[0].index('-')
			i=i+1
			#print row[0]
			while(row[0][i]==' ' and i<len(row[0])):
				i=i+1
			#print row[0][i:]
			cur.execute("UPDATE RATINGS1 SET A1_AUX='"+row[0][i:]+"' WHERE A1_POS='"+row[0]+"';")
			conn.commit()
			cur.execute("UPDATE RATINGS1 SET A2_AUX='"+row[0][i:]+"' WHERE A2_POS='"+row[0]+"';")
			conn.commit()
		else:
			#print row[0]
			print 'yes'
		cur.execute("UPDATE RATINGS1 SET A1_POS='"+"Vice President"+"' WHERE A1_POS='"+row[0]+"';")
		conn.commit()
		cur.execute("UPDATE RATINGS1 SET A2_POS='"+"Vice President"+"' WHERE A2_POS='"+row[0]+"';")
		conn.commit()
		k=k+1
		
	#As usually we search for Managing Director and the procedures are same as above.
	elif(re.search("M.*D.*", row[0])):
		if('-' in row[0]):
			#print row[0]
			i=row[0].index('-')
			i=i+1
			#print row[0]
			while(row[0][i]==' ' and i<len(row[0])):
				i=i+1
			#print row[0][i:]
			cur.execute("UPDATE RATINGS1 SET A1_AUX='"+row[0][i:]+"' WHERE A1_POS='"+row[0]+"';")
			conn.commit()
			cur.execute("UPDATE RATINGS1 SET A2_AUX='"+row[0][i:]+"' WHERE A2_POS='"+row[0]+"';")
			conn.commit()
		else:
			#print row[0]
			print 'yes'
		k=k+1
		cur.execute("UPDATE RATINGS1 SET A1_POS='"+"Managing Director"+"' WHERE A1_POS='"+row[0]+"';")
		conn.commit()
		cur.execute("UPDATE RATINGS1 SET A2_POS='"+"Managing Director"+"' WHERE A2_POS='"+row[0]+"';")
		conn.commit()
			
	else:
		#print row[0]
		k=k+1
	#if(re.search(".*-.*", row[0])):
		#print "Position: ", row[0]
	#print "Analyst 2 Name: ", row[6], "\n"
	#print "Position: ", row[0]

print j
print k
	
   	
