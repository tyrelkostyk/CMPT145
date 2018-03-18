# CMPT 145: Assignment 5 Question 3
# test script

import a5q1 as a5q1
import a7q6 as a7q6
import node as node

# Utilizing to_string() function from a5q1

## NOTE: I wasn't able to successfully implpement reverse() in a7q6, however
## I still included the proper test cases for it (see below)

# a)
test_subst = [
    {'inputs' : [None, 5, 10],
     'outputs': 'EMPTY',
     'reason' : 'Empty node chain'},

    {'inputs' : [node.create(1), 1, 5],
     'outputs': '[ 5 | / ]',
     'reason' : 'node chain with one node, target in chain'},

    {'inputs' : [node.create(1), 3, 5],
     'outputs': '[ 1 | / ]',
     'reason' : 'node chain with one node, target not in chain'},

    {'inputs' : [node.create(1, node.create('two', node.create(3))), 1, 'one'],
     'outputs': "[ one | *-]-->[ two | *-]-->[ 3 | / ]",
     'reason' : 'node chain with three nodes, target is in first node'},

    {'inputs' : [node.create(1, node.create(2, node.create(3))), 3, 'three'],
     'outputs': "[ 1 | *-]-->[ 2 | *-]-->[ three | / ]",
     'reason' : 'node chain with three nodes, target is in last node'},

    {'inputs' : [node.create('one', node.create('two', node.create(3))), 7, 'seven'],
     'outputs': "[ one | *-]-->[ two | *-]-->[ 3 | / ]",
     'reason' : 'node chain with three nodes, target is not in node'},

    {'inputs' : [node.create('eight', node.create('two', node.create('three', node.create(5, node.create('six'))))), 5, 'five'],
     'outputs': "[ eight | *-]-->[ two | *-]-->[ three | *-]-->[ five | *-]-->[ six | / ]",
     'reason' : 'node chain with five nodes, target is in chain'},

    {'inputs' : [node.create('hello', node.create('bye', node.create('hello', node.create('hello')))), 'hello', 'hi'],
     'outputs': "[ hi | *-]-->[ bye | *-]-->[ hi | *-]-->[ hi | / ]",
     'reason' : 'node chain with four nodes, target is in three nodes'},
]


for t in test_subst:
    args_in = t['inputs']
    expected = t['outputs']

    result = a5q1.to_string( a7q6.subst(args_in[0], args_in[1], args_in[2]) )
    assert result == expected, 'subst(): expected '+str(expected)+', got ' +result+ ' -- '+t['reason']


# b)
test_reverse = [
    {'inputs' : None,
     'outputs': 'EMPTY',
     'reason' : 'Empty node chain'},

    {'inputs' : node.create(7),
     'outputs': '[ 7 | / ]',
     'reason' : 'node chain with one node'},

    {'inputs' : node.create(1, node.create('two', node.create(11))),
     'outputs': "[ 11 | *-]-->[ two | *-]-->[ 1 | / ]",
     'reason' : 'node chain with three nodes'},
]


for t in test_reverse:
    args_in = t['inputs']
    expected = t['outputs']

    result = a5q1.to_string( a7q6.reverse(args_in) )
    assert result == expected, 'reverse(): expected '+str(expected)+', got ' +result+ ' -- '+t['reason']


# c)
test_copy = [
    {'inputs' : None,
     'outputs': 'EMPTY',
     'reason' : 'Empty node chain'},

    {'inputs' : node.create(1),
     'outputs': '[ 1 | / ]',
     'reason' : 'node chain with one node'},

    {'inputs' : node.create(1, node.create('two', node.create(3))),
     'outputs': '[ 1 | *-]-->[ two | *-]-->[ 3 | / ]',
     'reason' : 'node chain with three nodes'},

    {'inputs' : node.create('eight', node.create('two', node.create('three', node.create(5)))),
     'outputs': '[ eight | *-]-->[ two | *-]-->[ three | *-]-->[ 5 | / ]',
     'reason' : 'node chain with five nodes'}
]


for t in test_copy:
    args_in = t['inputs']
    expected = t['outputs']

    result = a5q1.to_string( a7q6.copy(args_in) )
    assert result == expected and (expected is not args_in), \
        'copy(): expected '+str(expected)+', got ' +result+ ' -- '+t['reason']


print('*** testing complete ***')
