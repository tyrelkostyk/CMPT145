## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a8q1.py

import treenode as tn
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
    # base case: tnode is empty
    if tnode is None:
        return None

    # replace t with r, if data is t
    if tn.get_data(tnode) == t:
        tn.set_data(tnode, r)

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
        none
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

def collect_data_in_order(tnode):
    """
    :Purpose:
        Collects all the data in tree, in order based on the in-order traversal
    :Params:
        tnode - treenode, already initialized
    :Post-conditions:
        none
    :Returns:
        All the data in the tree in an organized list (based on in-order)
    """
    # base case: tnode is empty
    if tnode is None:
        return []
    else:
        data = collect_data_in_order(tn.get_left(tnode))
        data.append(tn.get_data(tnode))
        data.extend(collect_data_in_order(tn.get_right(tnode)))
        return data

def count_smaller(tnode, t):
    """
    :Purpose:
        counts the number of data values in tnode less than t
    :Params:
        tnode - treenode, already initialized
        t - int, conditional for counting (values must be smaller than t)
    :Post-conditions:
        none
    :Returns:
        the number (int) of values less than t
    """
    # base case: tnode is empty
    if tnode is None:
        return 0
    elif tn.get_data(tnode) < t:
        return 1 + count_smaller(tn.get_left(tnode), t) + count_smaller(tn.get_right(tnode), t)
    else:
        return count_smaller(tn.get_left(tnode), t) + count_smaller(tn.get_right(tnode), t)
