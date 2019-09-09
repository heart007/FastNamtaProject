def calc ():
	for i in range(1,11):
		print (str(number) + " * " + str(i)+ " = " +str(round(number*i)))
		i=i+1
try:
	number = int(input("Enter the Number : "))
	print("it's a int")
	# calc()
	# continue
except:
	print("it's a string")
	# entry = input("Press Y for continue, or Press N to Exit: ").lower()
	# if (entry == 'y'):
	# 	number = int(input("Enter the Number : "))
	# 	calc() 
	# else:
	# 	exit()



	# while True:	
	# entry = input("Press Y for continue, or Press N to Exit: ").lower()
	# if (entry == 'y'):
	# 	calc() 
	# else:
	# 	exit()


# calc ()		

