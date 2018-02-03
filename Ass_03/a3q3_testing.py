## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab04
## a3, due Friday Feb 2nd 10pm

import a3q3 as count

#####################################################################
# test a3q3.create()

test_create = [
    {'inputs' : [],
     'outputs': [0,0],
     'reason' : 'Takes no inputs, only need a single test'}
]

for t in test_create:
    args_in = t['inputs']       # pointless, but keeps the pattern consistent
    expected = t['outputs']

    # create the Counter data structure
    thing = count.create()

    # check the total count
    if thing['total'] != expected[0]:
        print('Error in create(): expected total count', expected[0],
              ' but found ', thing['count'], '---', t['reason'])

    # check the unique count
    if thing['unique'] != expected[1]:
        print('Error in create(): expected unique count', expected[1],
              ' but found ', thing['avg'], '---', t['reason'])

#####################################################################
print('*** Test script completed ***')
#####################################################################
