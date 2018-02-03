## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab04
## a3, due Friday Feb 2nd 10pm

import a3q3 as count

#####################################################################
# test a3q3.create()

test_create = [
    {'inputs' : [],    # takes no inputs
     'outputs': 0,     # total count is initially zero
     'reason' : 'Takes no inputs, only need a single test'}
]

for t in test_create:
    args_in = t['inputs']       # pointless, but keeps the pattern consistent
    expected = t['outputs']

    # create the Counter data structure
    thing = count.create()

    # check the total count
    if thing['total'] != expected:
        print('Error in create(): expected total count', expected,
              ' but found ', thing['total'], '---', t['reason'])


#####################################################################
# test a3q3.see(counter, value)

test_see = [
    {'inputs' : [0],      # single value input
     'outputs': [1,1],    # total count is one, count of ['0'] is 1
     'reason' : 'Single input of 0'},
    {'inputs' : [1,1,1,1],
     'outputs': [4,1],
     'reason' : 'Four inputs of 1'}
]

for t in test_see:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Counter data structure
    thing = count.create()

    # call count.see() function
    for val in args_in:
        count.see(thing, val)

    # check each unique value's count
    if thing[str(val)] != expected[]:
        print('Error in see(): expected', args_in[i], 'count', expected[i],
              ' but found ', thing[str(args_in[i])], '---', t['reason'])

    # check the total count
    if thing['total'] != expected[0]:
        print('Error in see(): expected total count', expected[0],
              ' but found ', thing['total'], '---', t['reason'])



#####################################################################
print('*** Test script completed ***')
#####################################################################
