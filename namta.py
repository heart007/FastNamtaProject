def calc ():
	try:
		number = int(input("Enter the Number : "))
		for i in range(1,11): 
			print(str(number) + " * " + str(i)+ " = " +str(round(number*i)))
			i=i+1
	except:
		print("Enter Numeric Value Only...!!!")
	
calc()
while True:		
	entry = input("Press Y or Yes for continue: ").lower()
	if (entry == 'y' or entry == 'yes'):
		calc()
		continue
	else:
		exit()
