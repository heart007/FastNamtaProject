def calc ():
	number = int(input("Enter the Number : "))
	for i in range(1,11):
		print (str(number) + " * " + str(i)+ " = " +str(round(number*i)))
		i=i+1
calc()
while True:		
	entry = input("Press Y for continue, or Press N to Exit: ").lower()
	if (entry == 'y'):
		calc()
		continue
	else:
		exit()
