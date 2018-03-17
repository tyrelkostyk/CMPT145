## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## A7q6; due Friday Saturday March 17th, 2018, 10pm

import node

# a)
def subst(chain, t, r):
    '''
    replaces any data value "t" with data value "r", in a given node chain "chain"
    :params:
    chain - node, already instantiated (possibly empty)
    t - data value, to be replaced by r whenever present in chain
    r - data value, replaces all occurances of t
    :pre: Chain already initialized as valid Node data type
    :post: all occurances of t are replaced with r, in chain
    :returns: None
    '''
    # base case
    if chain == None:
        return None
    else:
        if node.get_data(chain) == t:
            node.set_data(chain, r)
        next_node = subst(node.get_next(chain), t, r)
        node.set_next(chain, next_node)
        return chain
