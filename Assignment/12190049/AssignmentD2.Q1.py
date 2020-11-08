def selection():
       print("enter any number to perform the operation")
       print("[1] Max of four numbers)")
       print("[2] Add divisible -by-3 number within the range(1 to N)")
       print("[3] Reverse the number")
       print("[4] Compute GCD and LCM")
       d=int(input("Enter any number to perform operation"))
       if d==1:
               print("enter any for number:")
               a=input("enter any number:")
               b=input("enter any number:")
               c=input("enter any number:")
	       d=input("enter any number:")
               if(a>b and a>c and a>d):
			print("maximum is",a)
               elif(b>c and b>d and b>a):
			print("maximum is",b)
               elif(c>d and c>a and c>b):
			print("maximum is",c)
 	       elif(d>a and d>b and d>c):
			print("maximum is",d)
	       else:
			print("invalid")
        elif d==2:
		N=int(input("enter any number:"))
                sum=0
		print("divisible numbers")
		for N in range (1,N)
			if (N%3==0):
			        sum=sum+N
			 	print N
                print ("The sum of divisible by 3 of ",N,"is:  ",sum)
        elif d==3:
	         n=(input("enter any number")
	         for N in range(n,0,-1):
	                print(n)
        elif d==4:
	   def GCD(a,b):
                  if (b==0):
                        return a
                  else:
                        return GCD(b,a%b)
          def LCM(a,b):
                    	return a*b/GCD(a,b)
	  a=input("enter any number")
	  b=input("enter any number")
	  print("GCD is:",GCD(a,b))
	  print("LCM is :",LCM(a,b))
     else:
	  print("inavalid number")
selection()

print("enter 1 for yes")
print("enter 2 for no")
P=int(input("Select any number to continued the operations:"))
if P==1:
	selection()
	P=int(input("Select any number to continued the operations:"))
	if P==1:
		slection()
		P=int(input("Enter any numbers to perform the operations:"))
	elif P==2:
		print("Your calculation is done")
	else:
		print("Checked your calculation")
elif P==2:
		print("Your calculation is done")
else:
		print("Checked your calculation")



