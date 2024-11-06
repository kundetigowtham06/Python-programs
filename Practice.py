                                             Set 1
 1. Write a program to convert Fahrenheit to Celsius.
#TO CONVERT FAHRENHEIT TO CELSIUS
f=int(input("ENTER THE FAHRENHEIT VALUE="))
celsius=((5/9)*(f-32))
print("celsius=",celsius)
 2. Write a program to swap two numbers without using a temporary variable.
a=int(input("Enter a:"))
b=int(input("Enter b:"))
a=a+b
b=a-b
a=a-b
print("a=",a)
print("b=",b)
 3. Write a program to check whether a given key exists in a dictionary or not.
dict1={
1:"Hello",
2:"World",
3:"python",
4:"java",
5:"Gowtham"
}
key=int(input())
if key in dict1.keys():
	print("Key is found")
else :
	print("Key is not found")
                                                          SET 2
 1. Write a Program to check whether the given alphabet is a vowel or consonant.
a=input("Enter alphabet:")
v=['a','e','i','o','u','A','E','I','O','U']
if a in v:
    print("It is a vowel")
else:
    print("It is a consonant")
 2. Write a program to find the position of minimum and maximum elements of a list.
l=[]
n=int(input("Enter the number of elements: "))
print("Enter elements=")
for i in range(n):
    e=int(input())
    l.append(e)
print("maximum position",l.index(max(l)))
print("minimum position",l.index(min(l)))
 3. Write a program to find the factorial of a given number using recursion.
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter number="))
print(fact(n))


                                              SET 3


 1. Write a program to find the Sum and Average of the list.

l=[]
n=int(input("No.of elements="))
for i in range(n):
	e=int(input("Enter numbers="))
	l.append(e)
add=sum(l)
avg=(add)/len(l)
print("sum=",add)
print("avg=",avg)


 2. Write a program to create and read a Text File.

f=open("Hello.txt",'w')
f.write("Hello world!")
f=open("Hello.txt",'r')
print(f.read())
f.close()


 3. Write a program to print the Fibonacci sequence using recursion.

def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
n=int(input("enter number="))
for i in range(n):
    print(fib(i),end=' ')
                                                               SET 4


 1. Write a Program to check whether the given Year is a Leap Year or not.

year=int(input("Enter year="))
if year%400==0 or year%4==0 or year%100!=0:
    print("Year is a leap year")
else:
    print("Year is not a leap year")

2. Write a program to concatenate two lists index-wise

l1=["M","na","i","Abhi"]
l2=["y","me","s","ram"]
m=len(l1)
l=[]
for i in range(m):
	l.append(l1[i]+l2[i])
print(l)

 3. Write a program to find the GCD of two numbers using recursion
def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(a,a%b)
a=int(input("Enter number1="))
b=int(input("Enter number2="))
print(gcd(a,b))


                                                   SET 5
 1. Write a program to Determine the Grade Based on Marks

a=int(input("Enter marks:"))
if a>=90 and a<100:
	print("Grade A")
elif a>=80 and a<90:
	print("Grade B")
elif a>=70 and a<80:
	print("Grade C")
elif a>=60 and a<70:
	print("Grade D")
elif a>=50 and a<60:
	print("Grade E")
else :
	print("Failed")

 2. Demonstrate the use of i) Logical Operators and v) Bitwise Operators with
 examples
i)Logical Operators

print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(not True)

ii)Bitwise Operators
x=int(input())
y=int(input())
print(x&y)
print(x|y)
print(x^y)
print(~x)
print(x>>y)
print(x<<y) 

 3. Write a program to create and read a CSV file.

d=[['s.no','name','roll'],
[1,'gotam',7],
[2,'hello',9]
]
with open('king.csv','w',newline='') as f:
	m=csv.writer(f)
	m.writerows(d)
with open('king.csv','r') as f:
	read=csv.reader(f)
	for i in read:
		print(i)

                                                          SET 10
 1. Write a Python program to interchange first and last elements in a list.

                                           
