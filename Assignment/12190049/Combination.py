#This is for recursion
n=int(input("Enter any number"))
r=int(input("Enter any number"))
def combination(n):
	if n==1:
		return 1
	else:
		return n*combination(n-1)
a=combination(n)
b=combination(r)
d=combination(n-r)
e=a/(b*d);
print(e)

#This is for iterative
def combination(n,r):
	if(r>n-r):
	   r=n-r
	d=1
	for i in range(r):
		d=d*(n-i)
		d=d/(i+1)
	return d
n=int(input("Enter any number"))
r=int(input("Enter any number"))
d=combination(n,r)
print(d)


