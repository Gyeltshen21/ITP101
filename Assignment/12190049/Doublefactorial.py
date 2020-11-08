#This is for recursion
def doublefactorial1(a):
	if a==1:#Odd
		return a
	elif a==2:#Even
		return a
	else:
		return a*doublefactorial1(a-2)
#Taking number of users
n=int(input("Enter any  numbers:"))
if n<0:#Checking weather given number is negative or positive
	print("For negative integers the factorial doesnot exist")
elif n==0:
	print("The factorial for 0 is 1")
else:
	print("The factorial of",n,"is",doublefactorial1(n))
#This is for iterative
def doublefactorial2(a):
	fac=1
	for i in range(a,-1,-2):
		if(i==0 or i==1):
			return fac
		else:
			fac=fac*i
#Taking number of users
n=int(input("Enter any  numbers:"))
if n<0:#Checking weather given number is negative or positive
	print("For negative integers the factorial doesnot exist")
elif n==0:
	print("The factorial for 0 is 1")
else:
	print("The factorial of",n,"is",doublefactorial2(n))


