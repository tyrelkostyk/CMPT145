## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a5q2.py, due Saturday March 3rd, 2018, 10pm

import node as node

def count_chain(node_chain):
    """
    Purpose:
        Counts the number of nodes in the node chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
    Return:
        :return: The number of nodes in the node chain.
    """
    counter = 0
    # special case: empty node chain
    if node_chain is None:
        return counter
    else:
        # walk along the chain
        walker = node_chain
        while walker is not None:
            walker = node.get_next(walker)
            counter += 1

    return counter


def copy_chain(node_chain):
    """
    Purpose:
        Make a new node chain with the same values as in node_chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly None
    Return:
        :return: A copy of node chain, with new nodes, but the same data.
    """
    # special case: empty node chain
    if node_chain is None:
        new_chain = None
        return new_chain
    else:
        # walk along the chain
        walker = node_chain
        # create new node chain
        new_chain = node.create(node.get_data(walker))
        # initialize temporary node to iterate through each orignal node
        tmp_node = new_chain
        while walker is not None:
            walker = node.get_next(walker)
            if walker is not None:
                # initialize next node, & assign it as the next node in chain
                next_node = node.create(node.get_data(walker))
                node.set_next(tmp_node, next_node)
                # reassign temp node, to further iterate through orignal chain
                tmp_node = next_node

    return new_chain


def replace(node_chain, target, value):
    """
    Purpose:
        Replace every occurrence of data target in node_chain with data value
        The chain should change data values only!
    Pre-Conditions:
        :param node_chain: a node-chain, possibly empty
        :param target: a data value
        :param value: a data value
    Post-conditions:
        The node-chain is changed, by replacing target with value everywhere.
    Return:
        :return: None
    """
    # special case: empty node chain
    if node_chain is None:
        return None
    else:
        # walk along the chain
        walker = node_chain
        while walker is not None:
            # check if data == target, & replace w/ value if it does
            data = node.get_data(walker)
            if data == target:
                node.set_data(walker, value)
            walker = node.get_next(walker)

    return None
