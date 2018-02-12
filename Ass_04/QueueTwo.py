## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a4q1.py, due Friday Feb 9th 10pm

import TStack as Stack


def create():
    """
    Purpose
        creates an empty queue
    Return
        an empty queue
    """
    q2 = {}
    q2['e-stack'] = Stack.create()
    print('e-stack:', q2['e-stack'])
    q2['d-stack'] = Stack.create()
    print('d-stack:', q2['d-stack'])
    return q2


def is_empty(queue):
    """
    Purpose
        checks if the given queue has no data in it
    Pre-conditions:
        queue is a queue created by create()
    Return:
        True if the queue has no data, or false otherwise
    """
    return True


def size(queue):
    """
    Purpose
        returns the number of data values in the given queue
    Pre-conditions:
        queue: a queue created by create()
    Return:
        The number of data values in the queue
    """
    print('size:', max(len(queue['e-stack'])-2, len(queue['d-stack'])-2))
    return max(len(queue['e-stack'])-2, len(queue['d-stack'])-2)


def enqueue(queue, value):
    """
    Purpose
        adds the given data value to the given queue
    Pre-conditions:
        queue: a queue created by create()
        value: data to be added
    Post-condition:
        the value is added to the queue
    Return:
        (none)
    """
    if len(queue['d-stack'])-2 == 0:
        Stack.push(queue['e-stack'], value)
    elif len(queue['d-stack'])-2 > 0:
        for i in range(len(queue['d-stack']) - 2):
            tmp = Stack.pop(queue['d-stack'])
            Stack.push(queue['e-stack'], tmp)
        Stack.push(queue['e-stack'], value)
    return


def dequeue(queue):
    """
    Purpose
        removes and returns a data value from the given queue
    Pre-conditions:
        queue: a queue created by create()
    Post-condition:
        the first value is removed from the queue
    Return:
        the first value in the queue
    """
    if len(queue['e-stack'])-2 == 0:
        return Stack.pop(queue['e-stack'])
    elif len(queue['e-stack'])-2 > 0:
        for i in range(len(queue['e-stack']) - 2):
            tmp = Stack.pop(queue['e-stack'])
            Stack.push(queue['d-stack'], tmp)
        return Stack.pop(queue['d-stack'], value)
    return None



def peek(queue):
    """
    Purpose
        returns the value from the front of given queue without removing it
    Pre-conditions:
        queue: a queue created by create()
    Post-condition:
        None
    Return:
        the value at the front of the queue
    """
    return None
