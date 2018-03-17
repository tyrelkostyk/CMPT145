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
    :returns: the (now modified) chain
    '''
    # base case
    if chain == None:
        return None
    else:
        # change target data
        if node.get_data(chain) == t:
            node.set_data(chain, r)
        # recrusive call
        subst(node.get_next(chain), t, r)
        return chain

# b)
def reverse(chain):
    '''
    reverses all data in node chain
    :params:
    chain - node, initialized & possibly empty
    :returns: the (now modified) chain
    '''
    # base case
    if chain == None:
        return chain
    else:
        # recursive call
        node.set_data(node.get_data( reverse(node.get_next(chain)) ))

        return chain

# c)
def copy(chain):
    '''
    produces a new chain, with same structure & values as original chain
    :params:
    chain - node, possibly empty
    :returns: new (identical but seperate) chain
    '''
    # special case: empty node
    if chain == None:
        return None
    # base case
    # elif node.get_next(chain) == None:
    #     return node.create(node.get_data(chain))
    else:
        # new_chain = copy(node.get_next(chain))
        # node.set_data(new_chain, node.get_data(chain))
        # node.set_next(new_chain, node.get_next(chain))

        return node.create(node.get_data(chain), next=copy(node.get_next(chain)) )
