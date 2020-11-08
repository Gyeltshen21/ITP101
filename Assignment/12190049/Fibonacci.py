#This is for recursion
def fibonacci(n): 
	if n<=1:
		return n
	else:
		return (fibonacci(n-1)+fibonacci(n-2))
#Taking numbers from users
a=int(input("Enter any numbers:"))
if a<=0:#Checking validate of the input number
	print("Dispalying the positive integers")
else:
	print("Fibonacci sequence")
	for i in range(a):
		print(fibonacci(i))
#This is for iterative
def fibonacci(n):
	a=1
	b=0
	for i in range(0,n):
		a,b=b,a+b
		print(a)
n=int(input("Enter any number:"))
print ("Sequence fibonacci")
fibonacci(n)

