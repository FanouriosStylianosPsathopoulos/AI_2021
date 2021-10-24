class Stack:
	def __init__(self):
		self.stack=[] #arxikopoihsh
		self.counter=0

	def push(self,item):
		self.stack.append(item)
		self.counter+=1 
		return True

	def print_things(self):
		print (self.stack)
		print (self.counter)

	def Empty(self):
		if not self.stack: #diaforetikos tropos ulopoihshs 8a htan me counter,eipa na dokimasw kati pio pythonic 
			return True
		else:
			return False

	def pop(self):
		if self.Empty()==False: #an exei estw ena stoixeio tote afairese to 
			self.counter-=1 #meiwse kata 1
			return self.stack.pop() #gurna to stoixeio
		else:
			print ("The stack is empty . You cant pop something from empty stack")
			return None #den uparxei kati na guriseis


p1=Stack()
print(p1.counter)