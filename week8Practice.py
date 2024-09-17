#Factorial
'''def fact(n):
	if n==0 or n==1:
		return 1
	else:
		return n*fact(n-1)
num=int(input("Enter number ="))
print("Factorial of",num,"is",fact(num))'''
#Fibonacci
'''def fib(n):
	if n<=1:
		return n
	else:
		return(fib(n-1)+fib(n-2))
x=int(input("Enter Number ="))
for i in range(x):
	print(fib(i))'''
#Gcd
'''
def Gcd(a,b):
	if b==0:
		return a
	else:
		return Gcd(a,a%b)
a=int(input())
b=int(input())
print(Gcd(a,b))
'''
#Math Functions
#Square Root
'''
import math
n=int(input("Enter Number="))
print(math.sqrt(4))
'''
#power,ceil,floor
'''
import math
n=int(input("Enter Number="))
l=math.pow(n,2)
print(l)
print(math.ceil(2.4))
print(math.floor(2.4))
'''
#Lambda
square=lambda x: x*x
n=int(input("Enter number="))
print(square(n))
#Second
l=[1,2,3,4]
square=list(map(lambda x: x*x,l))
print(square)
#program-7
check=lambda x:x%2
n=int(input("Enter number="))
if check(n)==0:
	print("Even")
else:
	print("Odd")
#Program-4
d={1:22,
2:33,
3:44,
4:55
}
key=int(input("Enter a key to find="))
m=0
for x in d:
	if key==d[x]:
		m=m+1
		break
	
if m!=0:
	print("Exists")
else:
	print("Doesn't Exists")
#Program-5
d={1:2,
2:3,
3:4,
4:5
}
d[5]=6
print("After adding new key-value pair")
print(d)
#program-6
d={1:2,
2:3,
3:4,
4:5
}
sum=0
for x in d:
	sum=sum+d[x]
print("Sum of all items",sum)
	
