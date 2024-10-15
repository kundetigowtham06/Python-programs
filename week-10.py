class Hello:
	branch='CSE'
	def details(self,roll,name):
		self.r=roll
		self.n=name
	def display(self):
		print(self.r)
		print(self.n)
class Bye(Hello):
	def __init__(self):
		print("Hello world")
	
o=Bye()
o.details(12,'ram')
o.display()
#multiple Inheritance
class Hello:
	branch='CSE'
	def details(self,roll,name):
		self.r=roll
		self.n=name
	def display(self):
		print(self.r)
		print(self.n)
class Bye:
	def __init__(self):
		print("Hello world")
class Child(Hello,Bye):
	def Name(self):
		print("Hello Python")
o=Child()
o.details(12,'ram')
o.display()
o.Name()
