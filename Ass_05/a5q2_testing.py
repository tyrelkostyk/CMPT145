# CMPT 145: Assignment 5 Question 2
# test script


import a5q1 as a5q1
import a5q2 as a5q2
import node as node

test_count_chain = [
    {'inputs' : None,
     'outputs': 0,
     'reason' : 'Empty node chain'},

    {'inputs' : node.create(1),
     'outputs': 1,
     'reason' : 'node chain with one node'},

    {'inputs' : node.create(1, node.create('two')),
     'outputs': 2,
     'reason' : 'node chain with two nodes'},

    {'inputs' : node.create(1, node.create('two', node.create(3))),
     'outputs': 3,
     'reason' : 'node chain with three nodes'},
]

for t in test_count_chain:
    args_in = t['inputs']
    expected = t['outputs']
    result = a5q2.count_chain(args_in)
    assert result == expected, 'count_chain(): got '\
        +str(result)+' expected '+str(expected)+' -- ' +t['reason']

test_copy_chain = [
    {'inputs' : None,
     'outputs': None,
     'reason' : 'Empty node chain'},

    {'inputs' : node.create(1),
     'outputs': None,
     'reason' : 'node chain with one node'},

    {'inputs' : node.create(1, node.create('two')),
     'outputs': None,
     'reason' : 'node chain with two nodes'},

    {'inputs' : node.create(1, node.create('two', node.create(3))),
     'outputs': None,
     'reason' : 'node chain with three nodes'},
]

for t in test_copy_chain:
    args_in = t['inputs']
    result = a5q2.copy_chain(args_in)

    assert (args_in is None and result is None) \
           or (args_in is not result), \
        'copy_chain(): original chain returned -- '+t['reason']

    assert args_in == result, 'copy_chain(): chains not equal -- '+t['reason']



test_replace = [
    {'inputs' : [None, 1, 1],
     'outputs': "EMPTY",
     'reason' : 'Empty node chain'},

    {'inputs' : [node.create(1), 1, 2],
     'outputs': "[ 2 | / ]",
     'reason' : 'node chain with one node, target in'},

    {'inputs' : [node.create(1), 5, 2],
     'outputs': "[ 1 | / ]",
     'reason' : 'node chain with one node, target not in'},

    {'inputs' : [node.create(1, node.create('two')),
                 1, 'one'],
     'outputs': "[ one | *-]-->[ two | / ]",
     'reason' : 'node chain with two nodes, target first'},

    {'inputs' : [node.create(1, node.create('two')),
                 5, 'five'],
     'outputs': "[ 1 | *-]-->[ two | / ]",
     'reason' : 'node chain with two nodes, target not in'},
    {'inputs' : [node.create(1, node.create('two')),
                 'two', 2],
     'outputs': "[ 1 | *-]-->[ 2 | / ]",
     'reason' : 'node chain with two nodes, target last'},

    {'inputs' : [node.create(1, node.create('two', node.create(3))),
                 'two', 2],
     'outputs': "[ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]",
     'reason' : 'node chain with three nodes, target middle'},
]

for t in test_replace:
    args_in = t['inputs']
    expected = t['outputs']
    a5q2.replace(args_in[0], args_in[1], args_in[2])
    result = a5q1.to_string(args_in[0])
    assert result == expected, \
        'replace(): got "'+result+'" expected "'+expected+'" -- '+t['reason']

print('*** testing complete ***')
