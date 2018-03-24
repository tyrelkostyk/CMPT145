## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a8q1.py

import treenode as tn
import traversals as trav
import treefunctions as TreeF

def subst(tnode, t, r):
    """
    :purpose:
        Replaces all occurances of t ('target') with r ('replacement') in given treenode tnode
    :params:
        tnode - treenode, already created
        t - 'target', data value to be replaced
        r - 'replacement', data value to replace target
    :post-conditions:
        All occurances of t will be replaced by r
    :returns:
        None
    """
    # check if tnode is empty
    if TreeF.is_leaf(tnode):
        return None

    # replace t with r, if data is t
    elif tn.get_data(tnode) == t:
        tn.set_data(tnode, r)

    # recursively call subst() on left & right children
    subst(tn.get_left(tnode), t, r)
    subst(tn.get_right(tnode), t, r)
    return None
