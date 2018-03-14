n = float(input("Enter the 5th power of a double digit integer : "))
k = n % 10

if (n>(10**5) and n<(20**5)):
	val = 10 + k
elif(n>(20**5) and n<(30**5)):
	val = 20 + k
elif(n>(30**5) and n<(40**5)):
	val = 30 + k
elif(n>(40**5) and n<(50**5)):
	val = 40 + k
elif(n>(50**5) and n<(60**5)):
	val = 50 + k
elif(n>(60**5) and n<(70**5)):
	val = 60 + k
elif(n>(70**5) and n<(80**5)):
	val = 70 + k
elif(n>(80**5) and n<(90**5)):
	val = 80 + k
elif(n>(90**5) and n<(100**5)):
	val = 90 + k

print ("\nFifth root  is " ,+ val)

