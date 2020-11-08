#Python3 version
#Question 5
def selection():
	print('Select any numbers to perfrom operations from the menu given below')
	print('[1] The result of: sqrt(x**2+y**2+z**2)')
	print('[2] The minimum of the numbers.')
	print ('[3] The factorial of the sum of the numbers i.e (x+y+z)!.')
	n=int(input("Enter any number to perform the operation:"))
	if n==1:
		print("Enter the value of x,y,z")
		x=int(input("Enter the value of x"))
		y=int(input("Enter the value of y"))
		z=int(input("Enter the value of z"))
		import math
		result=math.sqrt(x**2+y**2+z**3)
		print('Result=',result)
	elif n==2:
		print("Enter the value of x,y,z")
		x=int(input("Enter the value of x"))
		y=int(input("Enter the value of y"))
		z=int(input("Enter the value of z"))
		if (x<y and x<z):
			print('Minimum is ',x)
		elif (y<x and y<z):
			print('Minimum is ',y)
		else:
			print('Minimum is ',z)
	elif n==3:
		print("Enter the value of x,y,z")
		x=int(input("Enter the value of x"))
		y=int(input("Enter the value of y"))
		z=int(input("Enter the value of z"))
		result=x+y+z
		for i in range(1,result):
			result=result*i
		print('The factorial of result','is',result)
	else:
		print('Invalid number')
selection()

print('1 for Yes')
print('2 for No')
m=int(input("Enter any number given above to do the operation or to stop the operation:"))
if m==1:
	selection()
	m=int(input("Enter any number given above to do the operation or to stop the operation:"))
	if m==1:
		m=int(input("Enter any number to perform the operation:"))
	elif m==2:
		print('Your operation is done')
	else:
		print('Check your operation')
elif m==2:
	print('Your operation is done')
else:
	print('Check your operation')
	
		

