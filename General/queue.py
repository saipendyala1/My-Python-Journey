# Abstract Data Type (ADT) is a model for a particular type of data
# data type is defined by its behaviour (or semantics) from the point of view of the
# user of that data type. 
# This behaviour is typically defined in terms of possible # values, 
# possible operations on the data of this type and behaviour of the operations
# provided by the data type.

# Queue is an ADT that defines how a collection of entities are managed and maintained.
# Queues have what is known as a First-In-First-Out (or FIFO)
# behaviour that is the first entity added to a queue is the first thing removed from
# the queue. Within the queue the order in which the entities were added is
# maintained.

# Queue opertions
#-----------------
#• Queue creation.
#• Add an element to the back of the queue (known as enqueuing).
#• Remove an element from the front of the queue (known as dequeuing).
#• Find out the length of the queue.
#• Check to see if the queue is empty.
#• Queues can be of fixed size or variable (growable) in size.
#• Peek at the element at the front of the queue 

# Python List container can be used 
# as a queue using the existing operations
# such as append() and pop()


queue = [] # Create an empty queue

queue.append('task1')
print('initial queue:', queue)

queue.append('task2')
queue.append('task3')

print('queue after additions:', queue)

element1 = queue.pop(0)
print('element retrieved from queue:', element1)
print('queue after removal', queue)


'''
class Queue:
    def __init__(self):
        self._list = [] # initial internal data
    
    def enqueue(self, element):
        self._list.append(element)
    
    def dequeue(self):
        return self._list.pop(0)
    
    def __len__(self):
        """ Supports the len protocol """
        return len(self._list)
    
    def is_empty(self):
        return self.__len__() == 0
    
    def peek(self):
        return self._list[0]
    
    def __str__(self):
        return 'Queue: ' + str(self._list)

'''