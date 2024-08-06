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
