#Add
def sum(a,b):
	return a+b
add=sum(16,14)
print("Addition is ",add)
#Mul
def mul(a,b,c):
	return a*b*c
print("Multiplication is",mul(1,2,3))
#Sub
def sub(a,b=4,c=9):
	return a-b-c
print("Subtraction is",sub(24))
#div
def div(a,b):
	return a/b
print("Divison is",int(div(b=2,a=6)))
#program 2
def M_return(a):
	if a%2==0:
		return "even"
	else:
		return "Odd"
n=int(input("Enter number="))
print(M_return(n))
#GCD
def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(a,a%b)
print(gcd(2,4))
#second largest
def s(my_list):
	x=max(my_list)
	my_list.remove(x)
	return max(my_list)
l=[1,2,3,4]
print(s(l))
