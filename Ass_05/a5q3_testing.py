# CMPT 145: Assignment 5 Question 3
# test script

import a5q1 as a5q1
import a5q3 as a5q3
import node as node


test_split_chain = [
    {'inputs' : None,
     'outputs': ["EMPTY","EMPTY"],
     'reason' : 'Empty node chain'},

    {'inputs' : node.create(1),
     'outputs': ["EMPTY", "[ 1 | / ]"],
     'reason' : 'node chain with one node'},

    {'inputs' : node.create(1, node.create('two')),
     'outputs': ["[ 1 | / ]","[ two | / ]"],
     'reason' : 'node chain with two nodes'},

    {'inputs' : node.create(1, node.create('two', node.create(3))),
     'outputs': ["[ 1 | / ]", "[ two | *-]-->[ 3 | / ]"],
     'reason' : 'node chain with three nodes'},

    {'inputs' : node.create(1, node.create('two', node.create(3,node.create('four')))),
     'outputs': ["[ 1 | *-]-->[ two | / ]","[ 3 | *-]-->[ four | / ]"],
     'reason' : 'node chain with four nodes'},

    {'inputs' : node.create(1, node.create('two', node.create(3,node.create('four', node.create(5))))),
     'outputs': ["[ 1 | *-]-->[ two | / ]", "[ 3 | *-]-->[ four | *-]-->[ 5 | / ]"],
     'reason' : 'node chain with five nodes'},

    {'inputs' : node.create(1, node.create('two', node.create(3,node.create('four', node.create(5, node.create('six')))))),
     'outputs': ["[ 1 | *-]-->[ two | *-]-->[ 3 | / ]", "[ four | *-]-->[ 5 | *-]-->[ six | / ]"],
     'reason' : 'node chain with six nodes'},
]


for t in test_split_chain:
    args_in = t['inputs']
    expected = t['outputs']
    first, second = a5q3.split_chain(args_in)

    str_result = a5q1.to_string(second)
    str_args_in = a5q1.to_string(first)
    assert str_result == expected[1] and str_args_in == expected[0], \
        'split_chain(): got '\
        +str_args_in+' and '+str_result+' -- ' +t['reason']

'''
test_remove_chain = [
    {'inputs' : [None, 1],
     'outputs': "EMPTY",
     'reason' : 'Empty node chain'},

    {'inputs' : [node.create(1), 1],
     'outputs': "EMPTY",
     'reason' : 'node chain with one node, val in'},

    {'inputs' : [node.create(1), 2],
     'outputs': "[ 1 | / ]",
     'reason' : 'node chain with one node, val not in'},

    {'inputs' : [node.create(1, node.create('two')), 'two'],
     'outputs': "[ 1 | / ]",
     'reason' : 'node chain with two nodes, val last'},

    {'inputs' : [node.create(1, node.create('two')), 1],
     'outputs': "[ two | / ]",
     'reason' : 'node chain with two nodes, val first'},

    {'inputs' : [node.create(1, node.create('two')), 3],
     'outputs': "[ 1 | *-]-->[ two | / ]",
     'reason' : 'node chain with two nodes, val not in'},

    {'inputs' : [node.create(1, node.create('two', node.create(3))), 'two'],
     'outputs': "[ 1 | *-]-->[ 3 | / ]",
     'reason' : 'node chain with three nodes, val in middle'},

    {'inputs' : [node.create(1, node.create('two', node.create(1, node.create('four')))), 1],
     'outputs': "[ two | *-]-->[ 1 | *-]-->[ four | / ]",
     'reason' : 'node chain with four nodes, val at front and middle'},

    {'inputs' : [node.create(1, node.create(1, node.create(1, node.create('four')))), 1],
     'outputs': "[ 1 | *-]-->[ 1 | *-]-->[ four | / ]",
     'reason' : 'node chain with four nodes, val repeated at front'},

    {'inputs' : [node.create(2, node.create(1, node.create(1, node.create('four')))), 1],
     'outputs': "[ 2 | *-]-->[ 1 | *-]-->[ four | / ]",
     'reason' : 'node chain with four nodes, val repeated in mid'},

    {'inputs' : [node.create(2, node.create(1, node.create('four', node.create('four')))), 'four'],
     'outputs': "[ 2 | *-]-->[ 1 | *-]-->[ four | / ]",
     'reason' : 'node chain with four nodes, val repeated at end'},

]

for t in test_remove_chain:
    args_in = t['inputs']
    expected = t['outputs']
    result = a5q3.remove_chain(args_in[0], args_in[1])

    str_result = a5q1.to_string(result)
    assert str_result == expected, 'remove_all_chain(): got "'\
        +str_result+'" expected "'+expected+'" -- ' +t['reason']


test_insert_at = [

    {'inputs' :  [None, 1, 0],
     'outputs': "[ 1 | / ]",
     'reason' : 'empty node chain'},

    {'inputs' :  [node.create('a'), 1, 0],
     'outputs': "[ 1 | *-]-->[ a | / ]",
     'reason' : 'node chain with one node, insert at front'},

    {'inputs' :  [node.create('a'), 1, 1],
     'outputs': "[ a | *-]-->[ 1 | / ]",
     'reason' : 'node chain with one node, insert at back'},

    {'inputs' :  [node.create('a', node.create('b')), 1, 0],
     'outputs': "[ 1 | *-]-->[ a | *-]-->[ b | / ]",
     'reason' : 'node chain with two nodes, insert at front'},

    {'inputs' :  [node.create('a', node.create('b')), 1, 2],
     'outputs': "[ a | *-]-->[ b | *-]-->[ 1 | / ]",
     'reason' : 'node chain with two nodes, insert at back'},

    {'inputs' :  [node.create('a', node.create('b')), 1, 1],
     'outputs': "[ a | *-]-->[ 1 | *-]-->[ b | / ]",
     'reason' : 'node chain with two nodes, insert at mid'},

    {'inputs' :  [node.create('a', node.create('b', node.create('c', node.create('d')))), 1, 2],
     'outputs': "[ a | *-]-->[ b | *-]-->[ 1 | *-]-->[ c | *-]-->[ d | / ]",
     'reason' : 'node chain with 4 nodes, insert at mid'},

    {'inputs' :  [node.create('a', node.create('b', node.create('c', node.create('d')))), 1, 4],
     'outputs': "[ a | *-]-->[ b | *-]-->[ c | *-]-->[ d | *-]-->[ 1 | / ]",
     'reason' : 'node chain with 4 nodes, insert at back'},

]

for t in test_insert_at:
    args_in = t['inputs']
    expected = t['outputs']
    result = a5q3.insert_at(args_in[0], args_in[1], args_in[2])

    str_result = a5q1.to_string(result)
    assert str_result == expected, 'insert_at(): got "'\
        +str_result+'" expected "'+expected+'" -- ' +t['reason']
'''

print('*** testing complete ***')
