import sys
from random import randint

class invalid_operator:
	def __init__(self, message_):
		self.message=message_
	def get_message(self):
		return self.message
		

class GraphungeParser:
	def __init__(self,FileName):
		self.dict={}
		self.Stack=[]
		self.Graph={}
		self.pcd=0
		self.string_mode=False
		self.seen_sharp=False
		self.dict_of_operators={'+':self.addition , '-':self.subtraction , '*':self.multiply , '/':self.divide , '%':self.module , '!':self.not_operator , '`':self.bigger , '^':self.caret_operator , 'v':self.v_operator , '_':self.underline ,'\"':self.quote_operator ,':':self.colon_operator , '\\':self.backslash_operator , '$':self.dollar_operator , '.':self.dot_operator ,',':self.comma_operator , '#':self.sharp_operator , 'g':self.g_operator ,'p':self.p_operator , 'l':self.l_operator , '&':self.ampersand_operator , '~':self.tilde_operator}
		file=open(FileName,"r")
		counter=0
		for line in file:
			elements_of_line=line.split()
			#print elements_of_line
			try:
				self.dict[counter]=int(elements_of_line[0])
			except ValueError:
				self.dict[counter]=elements_of_line[0]
			elements_of_line=elements_of_line[1:]
			int_elements=[int(x) for x in elements_of_line]
			self.Graph[counter]=int_elements
			counter+=1
		print self.Graph
		print self.dict
		file.close()
		print "closing successfuly!"
	def addition(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				if len(self.Stack) < 2:
					print "Stack is empty!"
					return
				first=self.Stack.pop()
				second=self.Stack.pop()
				result = first+second
				self.Stack.append(result)
				print self.Stack
			else:
				self.seen_sharp=False
		else:
			self.Stack.append(ord('+'))

	def subtraction(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				if len(self.Stack) < 2:
					print "Stack is empty!"
					return
				first=self.Stack.pop()
				second=self.Stack.pop()
				result = first-second
				self.Stack.append(result)
				print self.Stack
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('-'))
	def underline(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				if len(self.Stack) < 1:
					print "Stack is empty!"
					return
				last=self.Stack.pop()
				if last == 0:
					self.pcd=self.pcd-1
				else:
					self.pcd=self.pcd+1
				print self.pcd
				#return pcd_a
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('_'))
		#return self.pcd
	def multiply(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				if len(self.Stack) < 2:
					print "Stack is empty!"
					return
				first=self.Stack.pop()
				second=self.Stack.pop()
				result = first*second
				self.Stack.append(result)
				print self.Stack
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('*'))

	def divide(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				if len(self.Stack) < 2:
					print "Stack is empty!"
					return
				first=self.Stack.pop()
				second=self.Stack.pop()
				result = first/second
				self.Stack.append(result)
				print self.Stack
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('/'))

	def module(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				if len(self.Stack) < 2:
					print "Stack is empty!"
					return
				first=self.Stack.pop()
				second=self.Stack.pop()
				result = first%second
				self.Stack.append(result)
				print self.Stack
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('%'))
		
	def not_operator(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				if len(self.Stack) < 1:
					print "Stack is empty!"
					return
				x=self.Stack.pop()
				if x == 0:
					self.Stack.append(1)
				else:
					self.Stack.append(0)
				print self.Stack
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('!'))
	def bigger(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				if len(self.Stack) < 2:
					print "Stack is empty!"
					return
				first=self.Stack.pop()
				second=self.Stack.pop()
				result = int(first>second)
				self.Stack.append(result)
				print self.Stack
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('`'))

	def colon_operator(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				if len(self.Stack) < 1:
					print "Stack is empty!"
					return
				result=self.Stack.pop()
				self.Stack.append(result)
				self.Stack.append(result)
				print self.Stack
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord(':'))
	def backslash_operator(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				size=len(self.Stack)
				if size >= 2:
					self.Stack[size-1] , self.Stack[size-2] = self.Stack[size-2] , self.Stack[size-1]
					print self.Stack
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('\\'))
	def dollar_operator(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				if len(self.Stack) < 1:
					print "Stack is empty!"
					return
				self.Stack.pop()
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('$'))
	def dot_operator(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				if len(self.Stack) < 1:
					print "Stack is empty!"
					return
				print self.Stack.pop()
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('.'))
	def comma_operator(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				if len(self.Stack) < 1:
					print "Stack is empty!"
					return
				print chr(self.Stack.pop())
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord(','))
	def ampersand_operator(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				try:
					user_input=int(raw_input("Enter a number : "))
					self.Stack.append(user_input)
				except ValueError:
					print "your input is not a number!"
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('&'))
	def tilde_operator(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				input_number=raw_input("Enter a number : ")
				if len(input_number) > 1:
					print "you have more than one character and i push first parameter!"
					self.Stack.append(ord(input_number[0]))
				else:
					self.Stack.append(ord(input_number))
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('~'))

	def g_operator(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				if len(self.Stack) < 1:
					print "Stack is empty!"
					return
				x=self.Stack.pop()
				if x in self.dict.keys():
					temp=str(self.dict[x])
					self.Stack.append(ord(temp))	
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('g'))
	def caret_operator(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				self.pcd=self.pcd+1				
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('^'))
	def v_operator(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				self.pcd=self.pcd-1				
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('v'))

	def question_mark(self,vertex):
		if self.string_mode == False:
			if self.seen_sharp == False:
				print len(self.Graph[vertex])
				self.pcd = randint(0,len(self.Graph[vertex])-1)				
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('?'))
	def l_operator(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				if len(self.Stack) < 2:
					print "Stack is empty!"
					return
				x=self.Stack.pop()
				y=self.Stack.pop()
				if x in self.Graph.keys():
					self.Graph[x].append(y)
				print self.Graph					
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('l'))
	def p_operator(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				if len(self.Stack) < 2:
					print "Stack is empty!"
					return
				first = self.Stack.pop()
				second = self.Stack.pop()
				if first in self.dict.keys():
					self.dict[first]=chr(second)
				print self.dict						
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('p'))
	def sharp_operator(self):
		if self.string_mode == False:
			if self.seen_sharp == False:
				self.seen_sharp = True						
			else:
				self.seen_sharp=False

		else:
			self.Stack.append(ord('#'))

	def quote_operator(self):
			if self.seen_sharp == False:
				if self.string_mode == True:
					self.string_mode = False
				else:
					self.string_mode = True						
			else:
				self.seen_sharp=False		
	def do_operator(self, operator ,vertex):
	
		if operator in self.dict_of_operators:
			self.dict_of_operators[operator]()
		elif operator == '?':
			self.question_mark(vertex)
		else:
			raise invalid_operator(operator+" is not a valid operator in Graphunge program!")

	def function(self,a):
		if isinstance(a,str):
			return 0
		return 1
	def parse_file(self):
		y=0
		x=0
		while self.dict[x] != '@':
			#print self.function(self.dict[x])
			if self.function(self.dict[x]) == 1:
				if self.dict[x] >= 0 and self.dict[x] <= 9:
					self.Stack.append(self.dict[x])
				else:
					print self.dict[x] , " is not a valid number in node of graph!"
					break
			else:
				try:
					self.do_operator(self.dict[x] , x)
				except invalid_operator as error:
					print error.get_message()
					break
			#print "pcd :: "
			#print self.pcd
			if self.pcd != 0 and len(self.Graph[x]) != 0:
				y=self.pcd%len(self.Graph[x])
			else:
				y=0
			#print x
			if x not in self.Graph.keys():
				break

			if len(self.Graph[x]) == 0:
				break
			#print y
			x=self.Graph[x][y]
			#print x
			print self.Stack

		print self.Stack
if len(sys.argv) < 2:
	print "correct way of interpret the GraphungeParser.py is python GraphungeParser.py program.gr!"
else:
	print str(sys.argv[1])
	g=GraphungeParser(str(sys.argv[1]))
	g.parse_file()
	print g.Stack
