
def Get_marks():
	global a,b,c,d,e,f,g,h,i,j 
	print("Enter CA of all modules")
	a=input("Programming language (ITP101)")
	b=input("Java (ITP102)")
	c=input("Operating system (ITF101)")
	d=input("Dzongkha")
	e=input("Maths")	
	print("Enter all exam marks of the each modules")
	f=input("Programming language (ITP101)")
	g=input("Java (ITP102)")
	h=input("Operating system (ITF101)")
	i=input("Dzongkha")
	j=input("Maths")	
Get_marks()
def calculate():
	global m,n,o,p,q
	m=a+f
	n=b+g
	o=c+h
	p=d+i
	q=e+j
	global Average
	Average=(m+n+o+p+q)/5		
	
calculate()

def Display():
	print("The CA and exam marks of each module")
	print("CA of ITP101 is:",a,"and exam marks is:",f)
	print("CA of ITP102 is:",b,"and exam marks is:",g)
        print("CA of ITF101 is:",c,"and exam marks is:",h)
	print("CA of Dzongkha is:",d,"and exam marks is:",i)
	print("CA of Maths is:",e,"and exam marks is:",j)
	
	print("The total marks of each module")
	print("ITP101:",m)
	print("ITP102:",n)
	print("ITF101:",o)
	print("Dzongkha:",p)
	print("Maths:",q)
	print("Average:",Average)
	
	if (m<n and m<o and m<p and m<q):
		print("Lowest is ITP101:",m)
	elif (n<m and n<o and n<p and n<q):
		print("Lowest is ITP102:",n)
	elif (o<n and o<m and o<p and o<q):  
		print("Lowest is ITF101:",o)
	elif (p<m and p<n and p<o and p<q):
		print("Lowest is Dzongkha:",p)
	else:
		print("Lowest is Maths:",q)
		

	print("The status of performance")
	if(100<Average>80):
		print("Outstanding performance")
	elif(70<Average>79.9):
		print("Very good performance")
	elif(60<Average>69.9):
		print("Good performance")
	elif(50<Average>59.9):
		print("Satisfactory performance")
	elif(Average<49.9):
		print("Fail")
	else:
		print("Invalid")
Display()
		
		

