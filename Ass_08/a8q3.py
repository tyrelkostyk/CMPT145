## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a8q1.py

import treenode as tn
import treefunctions as tnfun

def complete(tnode):
    """
    :purpose:
        Determines if a tree is A complete binary tree
    :params:
        tnode - treenode, already created
    :post-conditions:
        none
    :returns:
        True, height; if a complete Binary Tree. False, None; otherwise
    """
    def cmplt(tnode):
        if tnode is None:
            return True, 0
        else:
            flag1, ldepth = cmplt(tn.get_left(tnode))
            flag2, rdepth = cmplt(tn.get_right(tnode))
            if (flag1) and (flag2) and (ldepth == rdepth):
                return True, 1 + rdepth
            else:
                return False, None
    flag, height = cmplt(tnode)
    return flag
