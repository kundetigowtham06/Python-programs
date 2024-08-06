#sum and average
l=[]
n=int(input("No.of elements="))
for i in range(n):
	e=int(input("Enter numbers="))
	l.append(e)
print(l)
add=sum(l)
avg=(add)/len(l)
print("sum=",add)
print("avg=",avg)
# second
l=[]
n=int(input("No.of elements="))
for i in range(n):
	e=int(input("Enter numbers="))
	l.append(e)
#method 1
print(l[::-1])
#method 2
l.reverse()
print(l)
#first occurence
l=[]
n=int(input("No.of elements="))
for i in range(n):
	e=int(input("Enter numbers="))
	l.append(e)
m=len(l)-1
t=l[0]
l[0]=l[m]
l[m]=t
print(l)
#method 2
l=[]
n=int(input("No.of elements="))
for i in range(n):
	e=int(input("Enter numbers="))
	l.append(e)
ind1=int(input("enter index 1="))
ind2=int(input("enter index 2="))
t=l[ind1]
l[ind1]=l[ind2]
l[ind2]=t
print(l)

