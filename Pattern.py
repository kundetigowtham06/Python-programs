n=int(input("No.of rows="))
for i in range(1,n+1):
	for j in range(1,i+1):
		print("* ",end=" ")
	print("")
#number pattern
n=int(input("No.of rows="))
for i in range(1,n+1):
	for j in range(1,i+1):
		print(j,end=" ")
	print("")
#alphabet pattern
n=int(input("No.of rows="))
m=65
for i in range(1,n+1):
	for j in range(1,i+1):
		print(chr(m),end=" ")
	m+=1
	print("")
