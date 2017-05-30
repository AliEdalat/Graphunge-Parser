import sys
from random import randint

file=open("program.gr","r")
counter=0
graph={}
stack=[]
dict ={}
for line in file:
	elements_of_line=line.split()
	print elements_of_line
	try:
		dict[counter]=int(elements_of_line[0])
	except ValueError:
		dict[counter]=elements_of_line[0]
	elements_of_line=elements_of_line[1:]
	int_elements=[int(x) for x in elements_of_line]
	graph[counter]=int_elements
	counter+=1
print graph
print dict




#graph = {0: [1],1: [2],2: [3],3: [4] , 4:[5] , 5:[6,7] , 7:[8,9]}

#stack=[]

#dict={0:[2] , 1:[4] , 2:['+'] , 3:[9] , 4:['-'] ,5:['_'] , 6:[':'] , 7:[1] ,8:[2] , 9:['@'] }

pcp=0
x=0
def function(a):
	
		if a == '+':
			return 0
		if a == '-':
			return 0
		if a == '_':
			return 0
		if a == '@':
			return 0
		if a == ':':
			return 0
		if isinstance(a,str):
			return 0

		return 1

def remove_list(stack_l1):
	for i in stack_l1:
		del i
def do_operator(stack_l , operator , vertex,pcp_a):
	if operator == '+':
		size=len(stack_l)
		result=stack_l[size-1]+stack_l[size-2]
		#print result
		stack_l.remove(stack_l[size-1])
		size=len(stack_l)
		print stack_l
		stack_l.remove(stack_l[size-1])
		print stack_l
		stack_l.append(result)
		print stack_l
		return pcp_a
	if operator == '-':
		size=len(stack_l)
		result=stack_l[size-1]-stack_l[size-2]
		#print result
		stack_l.remove(stack_l[size-1])
		print stack_l
		size=len(stack_l)
		stack_l.remove(stack_l[size-1])
		print stack_l
		stack_l.append(result)
		print stack_l
		return pcp_a
	if operator == '_':
		size=len(stack_l)
		if stack_l[size-1] == 0:
			pcp_a=pcp_a-1
		else:
			pcp_a=pcp_a+1
		#print pcp_a
		del stack_l[size-1]
		return pcp_a
	if operator == '*':
		size=len(stack_l)
		result=stack_l[size-1]*stack_l[size-2]
		#print result
		stack_l.remove(stack_l[size-1])
		size=len(stack_l)
		print stack_l
		stack_l.remove(stack_l[size-1])
		print stack_l
		stack_l.append(result)
		print stack_l
		return pcp_a
	if operator == '/':
		size=len(stack_l)
		result=stack_l[size-1]/stack_l[size-2]
		#print result
		stack_l.remove(stack_l[size-1])
		size=len(stack_l)
		print stack_l
		stack_l.remove(stack_l[size-1])
		print stack_l
		stack_l.append(result)
		print stack_l
		return pcp_a
	if operator == '%':
		size=len(stack_l)
		result=stack_l[size-1]%stack_l[size-2]
		#print result
		stack_l.remove(stack_l[size-1])
		size=len(stack_l)
		print stack_l
		stack_l.remove(stack_l[size-1])
		print stack_l
		stack_l.append(result)
		print stack_l
		return pcp_a
	if operator == '!':
		size=len(stack_l)
		if stack_l[size-1] == 0:
			stack_l.remove(stack_l[size-1])
			stack_l.append(1)
		else:
			stack_l.remove(stack_l[size-1])
			stack_l.append(0)
		print stack_l
		return pcp_a
	if operator == '`':
		size=len(stack_l)
		result=int(stack_l[size-1] > stack_l[size-2])
		#print result
		stack_l.remove(stack_l[size-1])
		size=len(stack_l)
		print stack_l
		stack_l.remove(stack_l[size-1])
		print stack_l
		stack_l.append(result)
		print stack_l
		return pcp_a
	if operator == ':':
		size=len(stack_l)
		result=stack_l[size-1]
		#print result
		stack_l.remove(stack_l[size-1])
		stack_l.append(result)
		stack_l.append(result)
		print stack_l
		return pcp_a
	if operator == '\\':
		size=len(stack_l)
		stack_l[size-1] , stack_l[size-2] = stack_l[size-2] , stack_l[size-1]
		print stack_l
		return pcp_a
	if operator == '$':
		stack_l.pop()
		return pcp_a
	if operator == '.':
		print stack_l.pop()
		return pcp_a
	if operator == ',':
		result=str(stack_l.pop())
		print result
		return pcp_a
	if operator == '&':
		
		try:
			user_input=int(raw_input("Enter a number : "))
			stack_l.append(user_input)
		except ValueError:
			print "your input is not a number!"
		return pcp_a
	if operator == '~':
		stack_l.append(ord(raw_input()))
		return pcp_a
	if operator == 'g':
		x=stack_l.pop()
		if x in dict.keys():
			temp=str(dict[x])
			stack_l.append(ord(temp))
		return pcp_a
	if operator == '^':
		pcp_a=pcp_a+1
		return pcp_a
	if operator == 'v':
		pcp_a=pcp_a-1
		return pcp_a
	if operator == '?':
		print len(graph[vertex])
		return randint(0,len(graph[vertex])-1)
	if operator == 'l':
		x=stack_l.pop()
		y=stack_l.pop()
		if x in graph.keys():
			graph[x].append(y)
		print graph
		return pcp_a
	if operator == 'p':
		first = stack_l.pop()
		second = stack_l.pop()
		if first in dict.keys():
			dict[first]=chr(second)
		print dict
		return pcp_a



#for x in graph:
y=0
while dict[x] != '@':
	
	
	print function(dict[x])
	if function(dict[x]) == 1:
		stack.append(dict[x])
	else:
		pcp=do_operator(stack , dict[x] ,x, pcp)
	print "PCD : "
	print pcp
	if pcp != 0 and len(graph[x]) != 0:
		y=pcp%len(graph[x])
	print "Y : "
	print y
	if x not in graph.keys():
		break

	if len(graph[x]) == 0:
		break
	x=graph[x][y]
	#print x
	print stack

print stack