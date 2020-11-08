def store():
	global x
	x=[]#storing the list
	for i in range(5):
		Name=str(input("Enter your Name:" ))#Getting string from user
		print("Name:",Name)
		y=x.append(Name)#Adding the string in the list
	print(x)
store()

def search():
	z=str(input("Enter any name to search from the list: "))#Getting string from user
	if z in x:#Checking weather enter user string is there or not
		print("Found")
	else:
		print("Not Found")
search()

def delete():
	Name=str(input("Enter a name to remove from the list: "))
	n=x.remove(Name)
	print(x)
delete()

def update():
	print("The lists of Name you have entered are:")
	print(x)
	try:
		for i in range(0,x) :
			a=int(input("Enter any index to display the name: "))
			print("Old Name: ",a[i])
			b=str(input("Enter any new name to update the list: "))
			print("New Name: ",b)
			c=x.append([b])
		print(x)
	except(IndexBoundOutOfRange):
		print ("index error")
update()

