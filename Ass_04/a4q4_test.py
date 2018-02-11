## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a4q1.py, due Friday Feb 9th 10pm

# import TQueue as Queue
import QueueTwo as Queue

## NOTE: There's no point in formally testing enqueue() by itself(no outputs)
## so I'm simply testing every other function, which by definition also tests
## enqueue()

##############################################################################
### Testing: is_empty() && enqueue()
test_is_empty = [
    {'inputs' : [],
     'outputs': True,
     'reason' : "Don't add anything"},
    {'inputs' : [5],
     'outputs': False,
     'reason' : 'Added something'},
    {'inputs' : [5,0,99],
     'outputs': False,
     'reason' : 'Added multiple things'}
]

# loop over every test case in test_is_empty
for t in test_is_empty:
    args_in = t['inputs']
    expected = t['outputs']

    # initialize function data structure (if needed)
    thing = Queue.create()
    # use the inputs
    for val in args_in:
        Queue.enqueue(thing, val)

    # now call your function
    result = Queue.is_empty(thing)

    if result != expected:
        print('Error in is_empty(): expected output', expected,
              'but found', result, '---', t['reason'])

##############################################################################
### Testing: size() && enqueue()
test_size = [
    {'inputs' : [],
     'outputs': 0,
     'reason' : "Didn't add anything"},
    {'inputs' : [5],
     'outputs': 1,
     'reason' : 'Added one item'},
    {'inputs' : [5,6,8,11],
     'outputs': 4,
     'reason' : 'Added four items'},
    {'inputs' : [1,0,-99,66,8,-15],
     'outputs': 6,
     'reason' : 'Added six items, some Negative'}
]

# loop over every test case in test_is_empty
for t in test_size:
    args_in = t['inputs']
    expected = t['outputs']

    # initialize function data structure (if needed)
    thing = Queue.create()
    # use the inputs
    for val in args_in:
        Queue.enqueue(thing, val)

    # now call your function
    result = Queue.size(thing)

    if result != expected:
        print('Error in size(): expected output', expected,
              'but found', result, '---', t['reason'])

##############################################################################
### Testing: dequeue() && enqueue()
test_dequeue = [
    {'inputs' : [],
     'outputs': [],
     'reason' : "Didn't add anything"},
    {'inputs' : [3],
     'outputs': [3],
     'reason' : 'Added one item'},
    {'inputs' : [9,1,2,3],
     'outputs': [9,1,2,3],
     'reason' : 'Added four items'},
    {'inputs' : [23,45,-77,-1245,22,0],
     'outputs': [23,45,-77,-1245,22,0],
     'reason' : 'Added six items, some Negative'}
]

# loop over every test case in test_dequeue
for t in test_dequeue:
    args_in = t['inputs']
    expected = t['outputs']

    # initialize function data structure (if needed)
    thing = Queue.create()
    # use the inputs
    for val in args_in:
        Queue.enqueue(thing, val)

    # now call your function
    result = []
    for val in range(Queue.size(thing)):
        result.append(Queue.dequeue(thing))

    if result != expected:
        print('Error in dequeue(): expected output', expected,
              'but found', result, '---', t['reason'])

print('*** Test Script Complete ***')
