## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a5q1.py, due Saturday March 3rd, 2018, 10pm

import node as node

def to_string(node_chain):
    """
    Purpose:
        Create a string representation of the node chain.  E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
    Pre-conditions:
        :param node_chain:  A node-chain, possibly empty
    Post_conditions:
        None
    Return: A string representation of the nodes.
    """
    # special case: empty node chain
    if node_chain is None:
        result = 'EMPTY'
        return result
    else:
        # walk along the chain
        walker = node_chain
        value = node.get_data(walker)
        # print the data
        result = '[ ' + str(value) + ' |'
        while walker is not None:
            walker = node.get_next(walker)
            if walker is not None:
                value = node.get_data(walker)
                # represent the next with an arrow-like figure
                result += ' *-]-->[ '+str(value)+' |'

        # at the end of the chain, use '/'
        result += ' / ]'

    return result
