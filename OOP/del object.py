class A:
	def __init__(self,b):
		self.b=b
	def display(self):
		print(self.b)
obj=A("Hello")
print(obj)
del obj
