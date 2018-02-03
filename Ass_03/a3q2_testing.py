## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab04
## a3, due Friday Feb 2nd 10pm

import a3q2 as Stat


#####################################################################
## NEW TEST CASES
#####################################################################
# test Statistics.count()

test_count = [
    {'inputs' : [0],    # data value(s) to be added
     'outputs': 1,      # number of data value(s) encountered
     'reason' : 'Add single zero, mean unchanged'},
    {'inputs' : [0,0,0],
     'outputs': 3,
     'reason' : 'Add multiple zeroes, mean unchanged'},
    {'inputs' : [5,5,20],
     'outputs': 3,
     'reason' : 'Add multiple pos values'},
    {'inputs' : [-10,-10,-10],
     'outputs': 3,
     'reason' : 'Add multiple neg values'},
    {'inputs' : [],
     'outputs': 0,
     'reason' : 'Add empty list as value'}
]

for t in test_count:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()
    # add the given values to the stat
    for val in args_in:
        Stat.add(thing, val)

    # now call count()
    result = Stat.count(thing)

    # finally, check the result of count()
    if result != expected:
        print('Error in count(): expected count', expected,
              ' but found ', result, '---', t['reason'])

#####################################################################
# test Statistics.maximum()

test_maximum = [
    {'inputs' : [5],
     'outputs': 5,
     'reason' : 'Add single value, max becomes that value'},
    {'inputs' : [],
     'outputs': None,
     'reason' : 'Add empty value, max remains None'},
    {'inputs' : [0],
     'outputs': 0,
     'reason' : 'Add 0, max becomes 0'},
    {'inputs' : [1,5,22],
     'outputs': 22,
     'reason' : 'Add multiple values, max becomes highest(22)'},
    {'inputs' : [-5,-44,10,30],
     'outputs': 30,
     'reason' : 'Add multiple values (pos & neg), max highest pos value'},
    {'inputs' : [-70,-44,-6],
     'outputs': -6,
     'reason' : 'Add multiple neg values, max "highest" neg value'}
]

for t in test_maximum:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()
    # add the given values to the stat
    for val in args_in:
        Stat.add(thing, val)

    # now call maximum()
    result = Stat.maximum(thing)

    # finally, check the result of maximum()
    if result != expected:
        print('Error in maximum(): expected max to be', expected,
              ' but found ', result, '---', t['reason'])


#####################################################################
# test Statistics.minimum()

test_minimum = [
    {'inputs' : [5],
     'outputs': 5,
     'reason' : 'Add single value, min becomes that value'},
    {'inputs' : [],
     'outputs': None,
     'reason' : 'Add empty value, min remains None'},
    {'inputs' : [0],
     'outputs': 0,
     'reason' : 'Add 0, min becomes 0'},
    {'inputs' : [3,35,22],
     'outputs': 3,
     'reason' : 'Add multiple values, min becomes lowest(3)'},
    {'inputs' : [0,-44,10,30,66],
     'outputs': -44,
     'reason' : 'Add multiple values (zero, pos, & neg), min is "largest" neg value'},
    {'inputs' : [-70,-44,-6],
     'outputs': -70,
     'reason' : 'Add multiple neg values, min is "largest" neg value'}
]

for t in test_minimum:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()
    # add the given values to the stat
    for val in args_in:
        Stat.add(thing, val)

    # now call minimum()
    result = Stat.minimum(thing)

    # finally, check the result of minimum()
    if result != expected:
        print('Error in minimum(): expected min to be', expected,
              ' but found ', result, '---', t['reason'])


#####################################################################
## OLD TEST CASES (STILL BEING USED)
#####################################################################
# test Statistics.create()
# create() has no parameters, so we only need one test case
# but we can test several things about the statistics data structure

test_create = [
    {'inputs' : [],
     'outputs': [0, 0],
     'reason' : 'Checking initial values'},
]

for t in test_create:
    args_in = t['inputs']       # pointless, but keeps the pattern consistent
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()

    # we'll open the data structure in these tests
    # check the initial count
    if thing['count'] != expected[0]:
        print('Error in create(): expected count', expected[0],
              ' but found ', thing['count'], '---', t['reason'])

    # check the initial ave
    if thing['avg'] != expected[1]:
        print('Error in create(): expected avg', expected[1],
              ' but found ', thing['avg'], '---', t['reason'])


#####################################################################
# test Statistics.add()
# these are integration tests

test_add = [
    {'inputs' : [0],    # single value to be added
     'outputs': [1, 0], # [count, avg]
     'reason' : 'No change to avg'},
    {'inputs' : [1],
     'outputs': [1,1],
     'reason' : 'Value should equal avg'},
    {'inputs' : [-1],
     'outputs': [1,-1],
     'reason' : 'Negative value should equal avg'},
    {'inputs' : [10.89],
     'outputs': [1,10.89],
     'reason' : 'Float change in avg'},
    {'inputs' : [-10.89],
     'outputs': [1,-10.89],
     'reason' : 'Negative Float change in avg'},
    {'inputs' : [342352],
     'outputs': [1,342352],
     'reason' : 'Dramatically change in avg'},
    {'inputs' : [-342352],
     'outputs': [1,-342352],
     'reason' : 'Dramatic Negative change in avg'}
]

for t in test_add:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()

    # now call add()
    Stat.add(thing, args_in[0])

    # we'll open the data structure in these tests
    # check the count
    if thing['count'] != expected[0]:
        print('Error in add(): expected count', expected[0],
              ' but found ', thing['count'], '---', t['reason'])

    # check the ave
    if thing['avg'] != expected[1]:
        print('Error in add(): expected avg', expected[1],
              ' but found ', thing['avg'], '---', t['reason'])


#####################################################################
# test Statistics.mean()

test_mean = [
    {'inputs' : [0,0,0,0,0],    # data values to be added
     'outputs': [5, 0],         #[count, avg]
     'reason' : 'All zeroes'},
    {'inputs' : [0],
     'outputs': [1,0],
     'reason' : 'Add 1 value, no change to avg'},
    {'inputs' : [-1,-1,-1,-1,-1],
     'outputs': [5,-1],
     'reason' : 'All -1'},
    {'inputs' : [10,10,-10],
     'outputs': [3,3],
     'reason' : 'Mixed values(pos & neg), pos output'},
    {'inputs' : [456,44,100],
     'outputs': [3,200],
     'reason' : 'Large pos values'},
    {'inputs' : [-456,-44,-100],
     'outputs': [3,-200],
     'reason' : 'Large Neg values'},
    {'inputs' : [],
     'outputs': [0, 0],
     'reason' : 'Add empty list as value'}
]

for t in test_mean:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()
    # add the give values to the
    for val in args_in:
        Stat.add(thing, val)

    # now call mean()
    result = Stat.mean(thing)

    # we'll open the data structure in these tests
    # check the count
    if thing['count'] != expected[0]:
        print('Error in add(): expected count', expected[0],
              ' but found ', thing['count'], '---', t['reason'])

    # check the ave
    if thing['avg'] != expected[1]:
        print('Error in add(): expected avg', expected[1],
              ' but found ', thing['avg'], '---', t['reason'])

    # check the result of mean()
    if result != expected[1]:
        print('Error in mean(): expected avg', expected[1],
              ' but found ', result, '---', t['reason'])

print('*** Test script completed ***')
