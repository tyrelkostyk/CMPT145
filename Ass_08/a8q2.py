## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a8q2.py

import treenode as tn
import treefunctions as tnfun

def mirrored(t1, t2):
    """
    :purpose:
        Determines if two trees satisfy the mirror property
    :params:
        t1 - treenode, already created
        t2 - treenode, already created
    :post-conditions:
        none
    :returns:
        True, if they satisfy the mirror property; False otherwise
    """
    # print('t1:', t1, '\n', 't2:', t2, '\n')
    if (t1 is None) or (t2 is None):
        return t1 == t2

    else:
        return (tn.get_data(t1) == tn.get_data(t2)) and (mirrored(tn.get_left(t1), tn.get_right(t2))) and (mirrored(tn.get_left(t2), tn.get_right(t1)))
    return False
