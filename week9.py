f=open("hello.txt",'w')
f.write("Hello")
f=open("hello.txt",'a')
f.write("Gotam")
f=open("hello.txt",'r')
print(f.read())
f.close()
f1=open("example.txt",'r')
print(f1.tell()) 
#Binary
f2=open("gotam.bin",'wb')
f2.write(b'\x00\x01')
f2=open("gotam.bin",'rb')
print(f2.read())
#csv
import csv
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
