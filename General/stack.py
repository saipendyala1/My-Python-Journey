# Stack is an ADT based on a Last-In-First-Out (or LIFO) behaviour. 
# That is the most recently added entity to the Stack will be the next entity
# to be removed. Within the stack the order that the entities were added in is
# maintained.

# • Stack creation.
# • Add an element to the top of the stack (known as pushing onto the stack).
# • Remove an element from the top of the stack (known as popping from the stack).
# • Find out the length of the stack.
# • Check to see if the stack is empty.
# • Stacks can be of fixed size or a variable (growable) stack.

# Python List container can be used 
# as a stack using the existing operations
# such as append() and pop()


stack = [] # create an empty stack

stack.append('task1')
stack.append('task2')
stack.append('task3')
print('stack:', stack)

top_element = stack.pop()
print('top_element:', top_element)

print('stack:', stack) 

