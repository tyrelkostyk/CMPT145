## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a8q1.py

import treenode as tn
import traversals as trav
import treefunctions as tnfun

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
    # base case one: tnode is empty
    if tnode is None:
        return None

    # replace t with r, if data is t
    if tn.get_data(tnode) == t:
        tn.set_data(tnode, r)

    # base case two: tnode is has no children
    if tnfun.is_leaf(tnode):
        return None

    # recursively call subst() on left & right children
    subst(tn.get_left(tnode), t, r)
    subst(tn.get_right(tnode), t, r)
    return None


def copy(tnode):
    """
    :Purpose:
        Creates a new, seperate but equal treenode
    :Params:
        tnode - treenode, already initialized
    :Post-conditions:
        tnode is unchanged
    :Returns:
        the new (exact replica) treenode
    """
    # Base case one: tnode is empty
    if tnode is None:
        return None

    # Base case two: tnode is a leaf
    elif tnfun.is_leaf(tnode):
        return tn.create(tn.get_data(tnode))

    # recursive call; tnode has at least one child
    else:
        return tn.create(tn.get_data(tnode),
                            copy(tn.get_left(tnode)),
                            copy(tn.get_right(tnode)))
    return None
