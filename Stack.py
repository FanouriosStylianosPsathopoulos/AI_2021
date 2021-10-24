class Stack:
	def __init__(self):
		self.stack=[] #initialization
		self.counter=0

	def push(self,item):
		self.stack.append(item)
		self.counter+=1 
		return True

	def print_things(self):
		print (self.stack)
		print (self.counter)

	def Empty(self):
		if not self.stack: #more pythonic than counter
			return True
		else:
			return False

	def pop(self):
		if self.Empty()==False: #if not empty pop
			self.counter-=1 #typical
			return self.stack.pop() #return element
		else:
			print ("The stack is empty . You cant pop something from empty stack")
			return None #nothing to return


def Balanced(string_to_see):
	#first validation check
	#there were some examples with whitespaces in piazza so i will strip whitespaces from string
	string_to_see=string_to_see.replace(" ","")

	allowed_char=["(",")","[","]","{","}"]
	for character in string_to_see:
		#print("Character is",character,"ok")
		if character not in allowed_char:
			print("Character ",character," not allowed")
			return None

	print("Validation check was done. Lets examine now if its Balanced.")


	#we will examine if its balanced by putting the right openers in stack every time we meet them 
	#every time we meet a left opener for example ")" we are gonna pop from stack a character
	#if its the same category we know the balance is kept otherwise its not.
	#we are gonna ignore whitespace character
	stack_of_validation=Stack()
	for_adding_to_stack=["(","[","{"]
	for_popping_from_stack=[")","]","}"]

	for character in string_to_see:
		if character in for_adding_to_stack:
			stack_of_validation.push(character)
		elif character in for_popping_from_stack:
			element=stack_of_validation.pop()

			if element==None:
				print("You closed something that wasnt open in first place.")
				print("Not balanced ")
				return False
			else :
				#i will check if its the appropriate closing by checking the substraction of ascii. 
				#For example [ has ascii 91 and ] 93 . ( has 40 and  ) has 41 . { has 123 and } 125
				#so if the substraction is 1 or 2 its valid otherwise its inbalanced
				if (ord(character)-ord(element)!=2 and ord(character)-ord(element)!=1):
					#print("Element out of stack is ",element," and character out of stack is ",character," ",ord(character)-ord(element))
					print("Not balanced , closed wrong symbol.")
					return False

	print("It is balanced")