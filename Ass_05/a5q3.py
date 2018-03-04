## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a5q3.py, due Saturday March 3rd, 2018, 10pm

import node as node
import a5q1 as a5q1
import a5q2 as a5q2

def split_chain(node_chain):
    """
    Purpose:
        Splits the given node chain in half, returning the second half.
        If the given chain has an odd length, the extra node is part of
        the second half of the chain.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
    Post-conditions:
        the original node chain is cut in half!
    Return:
        :return: A tuple (nc1, nc2) where nc1 and nc2 are node-chains
         each containing about half of the nodes in node-chain
    """
    # calculate mid_point location
    node_length = a5q2.count_chain(node_chain)
    mid_point = node_length // 2

    # special case: empty node chain
    if node_chain is None:
        return None, None
    elif node_length == 1:
        return None, node_chain
    else:
        # walk along the chain
        last_half = node_chain
        counter = 0
        while counter < mid_point:
            last_half = node.get_next(last_half)
            counter += 1

        # at end of first half, cut it off
        tmp = node_chain
        for i in range(mid_point-1):
            tmp = node.get_next(tmp)
        node.set_next(tmp, None)

    return node_chain, last_half


def remove_chain(node_chain, val):
    """
    Purpose:
        Remove the first occurrence of val from node_chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
        :param val: a value to be removed
    Post-conditions:
        The first occurrence of the value is removed from the chain.
        If val does not appear, the node-chain is unmodified.
    Return:
        :return: The resulting node chain with val removed
    """

    return None





def insert_at(node_chain, value, index):
    """
    Purpose:
        Insert the given value into the node-chain so that
        it appears at the the given index.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
        :param value: a value to be inserted
        :param index: the index where the new value should appear
        Assumption:  0 <= index <= n
                     where n is the number of nodes in the chain
    Post-condition:
        The node-chain is modified to include a new node at the
        given index with the given value as data.
    Return
        :return: the node-chain with the new value in it
    """

    return None
