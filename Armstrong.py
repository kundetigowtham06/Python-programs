n=int(input())
sum=0
t=n
l=n
i=0
while n!=0:
	remainder=n%10
	i=i+1
	n //=10
while l!=0:
	rem=l%10
	sum=sum+(rem**i)
	l //=10
if t==sum:
	print("Armstrong number")
else :
	print(" It is not a armstrong number")
