## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a8q1.py

import treenode as tn
import treefunctions as tnfun

def ordered(tnode):
    """
    :purpose:
        Determines if a tree is ordered (left substree < root < right substree)
    :params:
        tnode - treenode, already created
    :post-conditions:
        none
    :returns:
        True, if tnode is ordered. False otherwise
    """
    # simple internal program that calculates sum of a treenode
    def sum(tnode):
        if tnode is None:
            return 0
        else:
            return tn.get_data(tnode) + sum(tn.get_left(tnode)) + sum(tn.get_right(tnode))

    if tnode is None:
        return True

    else:
        # assign current value
        val = tn.get_data(tnode)

        # check if the next child nodes are none; if so, ensure they aren't accounted for
        if tn.get_left(tnode) is None:
            left_sum = val - 1
        else:
            left_sum = sum(tn.get_left(tnode))
        if tn.get_right(tnode) is None:
            right_sum = val + 1
        else:
            right_sum = sum(tn.get_right(tnode))

        # if the current node is ordered, recursively check its child nodes
        if left_sum < val < right_sum:
            return ordered(tn.get_left(tnode)) and ordered(tn.get_right(tnode))
        else:
            return False
