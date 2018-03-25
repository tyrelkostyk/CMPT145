## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a8q2_testing.py


import treenode as tn
import treefunctions as tnfun
import a8q2


## Testing mirrored()
test_mirrored = [
    {'inputs'  : [tn.create(5), tn.create(8)],
     'expected': False,
     'reason'  : 'two single-node trees, not mirrored'},
    {'inputs'  : [tn.create(1), tn.create(1)],
     'expected': True,
     'reason'  : 'two single-node trees, mirrored'},
    {'inputs'  : [tn.create(5, tn.create(8), tn.create(7)), tn.create(5, tn.create(7), tn.create(8))],
     'expected': True,
     'reason'  : 'two mirrored height=2 trees'},
    {'inputs'  : [tn.create(5, tn.create(8),
                               tn.create(7, tn.create(9, tn.create(8),
                                                         None),
                                            None)),
                  tn.create(5, tn.create(7, None,
                                            tn.create(9, None,
                                                         tn.create(8))),
                               tn.create(8))],
     'expected': True,
     'reason'  : 'two mirrored height=4 trees'},
    {'inputs'  : [tn.create(5, tn.create(8),
                               tn.create(7, tn.create(9, tn.create(8),
                                                         None),
                                            None)),
                  tn.create(5, tn.create(7, None,
                                            tn.create(9, None,
                                                         tn.create(9))),
                               tn.create(8))],
     'expected': False,
     'reason'  : 'two non-mirrored height=4 trees'},
]

for t in test_mirrored:
    args_in = t['inputs']
    expected = t['expected']

    result = a8q2.mirrored(args_in[0], args_in[1])

    if result != expected:
        print('Error in mirrored(): expected output', expected,
              'but found', result, '---', t['reason'])


print('*** Test Script Complete ***')
