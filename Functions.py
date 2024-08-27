#Addition Function
def sum(a,b):
	return a+b
add=sum(16,14)
print("Addition is ",add)
#Positional Parameters
def mul(a,b,c):
	return a*b*c
print("Multiplication is",mul(1,2,3))
#Default parameters
def sub(a,b=4,c=9):
	return a-b-c
print("Subtraction is",sub(24))
#Keyword parameters
def div(a,b):
	return a/b
print("Divison is",int(div(b=2,a=6)))
#variable length
def Branch(*b):
	print("Branches in vitb are",b)
	for i in b:
		print(i)
print(Branch("Cse","Ece","It"))
