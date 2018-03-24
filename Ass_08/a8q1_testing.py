## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a8q1_testing.py

import treenode as tn
import treefunctions as treefun
import exampletrees as extree
import a8q1


## Testing subst()
test_subst = [
    {'inputs'  : [tn.create(5), 4, 1],
     'expected': tn.create(5),
     'reason'  : 'single-leaf tree, target not in tree'},
     {'inputs'  : [tn.create(5), 5, 6],
      'expected': tn.create(6),
      'reason'  : 'single-leaf tree, target in tree'},
    {'inputs'  : [tn.create(5,
                    tn.create(4),
                    tn.create(7)),
                    7, 8],
     'expected': tn.create(5,
                     tn.create(4),
                     tn.create(8)),
     'reason'  : 'multi-node tree, target in roots right child'},
    {'inputs'  : [tn.create(7,
                    tn.create(4),
                    tn.create(7)),
                    7, 8],
     'expected': tn.create(8,
                     tn.create(4),
                     tn.create(8)),
     'reason'  : 'multi-node tree, target appears twice in tree'},
    {'inputs'  : [tn.create(5,
                  tn.create(1,None,
                            tn.create(4,
                                      tn.create(3,tn.create(2,None,None),None),
                                      None)),
                  tn.create(9,tn.create(8,tn.create(7,tn.create(6,None,None),None),None),
                              tn.create(1,tn.create(3,None,None),tn.create(3,None,None)))),
                  88, 8],
     'expected': tn.create(5,
                   tn.create(1,None,
                             tn.create(4,
                                       tn.create(3,tn.create(2,None,None),None),
                                       None)),
                   tn.create(9,tn.create(8,tn.create(7,tn.create(6,None,None),None),None),
                               tn.create(1,tn.create(3,None,None),tn.create(3,None,None)))),
     'reason'  : 'fairly large tree, target not in tree'},
    {'inputs'  : [tn.create(3,
                  tn.create(1,None,
                            tn.create(4,
                                      tn.create(3,tn.create(2,None,None),None),
                                      None)),
                  tn.create(9,tn.create(8,tn.create(7,tn.create(3,None,None),None),None),
                              tn.create(1,tn.create(3,None,None),tn.create(3,None,None)))),
                  3, 30],
     'expected': tn.create(30,
                   tn.create(1,None,
                             tn.create(4,
                                       tn.create(30,tn.create(2,None,None),None),
                                       None)),
                   tn.create(9,tn.create(8,tn.create(7,tn.create(30,None,None),None),None),
                               tn.create(1,tn.create(30,None,None),tn.create(30,None,None)))),
     'reason'  : 'fairly large tree, target in all corners of tree'}
]

for t in test_subst:
    args_in = t['inputs']
    expected = t['expected']

    test_tree = args_in[0]
    a8q1.subst(test_tree, args_in[1], args_in[2])

    if test_tree != expected:
        print('Error in subst(): expected output', expected,
              'but found', test_tree, '---', t['reason'])

## Testing copy()
test_copy = [
    {'inputs'  : tn.create(5),
     'expected': tn.create(5),
     'reason'  : 'single-leaf tree'},
    {'inputs'  : tn.create(5,
                    tn.create(4),
                    tn.create(7)),
     'expected': tn.create(5,
                     tn.create(4),
                     tn.create(7)),
     'reason'  : 'multi-node tree'},
    {'inputs'  : tn.create(5,
                  tn.create(1,None,
                            tn.create(4,
                                      tn.create(3,tn.create(2,None,None),None),
                                      None)),
                  tn.create(9,tn.create(8,tn.create(7,tn.create(6,None,None),None),None),
                              tn.create(1,tn.create(3,None,None),tn.create(3,None,None)))),
     'expected': tn.create(5,
                   tn.create(1,None,
                             tn.create(4,
                                       tn.create(3,tn.create(2,None,None),None),
                                       None)),
                   tn.create(9,tn.create(8,tn.create(7,tn.create(6,None,None),None),None),
                               tn.create(1,tn.create(3,None,None),tn.create(3,None,None)))),
     'reason'  : 'fairly large tree'}
]

for t in test_copy:
    args_in = t['inputs']
    expected = t['expected']

    tree_replica = a8q1.copy(args_in)

    if (tree_replica != expected):
        print('Error in copy(): expected output', expected,
              'but found', tree_replica, '---', t['reason'])
    if (tree_replica is expected):
        print('Error in copy(): copy has same reference as original')


print('*** Test Script Complete ***')
