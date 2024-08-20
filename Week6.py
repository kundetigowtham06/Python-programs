'''s=input("Enter String= ")
print(s[::-1])'''
#method 2
'''s=input("Enter string= ")
rev=""
for i in s:
	rev=i+rev
print("Reverse=",rev)'''
#palindrome
'''s=input("Enter string= ")
rev=""
for i in s:
	rev=i+rev
if s==rev:
	print("Palindrome")
else:
	print("Not a Palindrome")'''
#length of string
'''s=input("Enter string= ")
count=0
for i in s:
	count+=1
print("Length=",count)'''
#number of vowels
'''s=input("Enter string= ")
c,v=0,0
for i in s:
	if i in "aeiouAEIOU":
		v+=1
	else:
		c+=1
print("No of vowels=",v)
print("No of consonants=",c)'''
#even length
s=input("Enter String").split(" ")
for i in s:
	if len(i)%2==0:
		print(i)


