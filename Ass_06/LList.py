## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## A5q1; LList.py, due Friday March 9th, 2018, 10pm

import node as node
import a5q1 as a5q1

def create():
    """
    Purpose
        creates an empty list
    Return
        :return an empty list
    """
    llist = {}
    llist['size'] = 0     # how many elements in the stack
    llist['head'] = None  # the node chain starts here; initially empty
    llist['tail'] = None
    return llist


def is_empty(alist):
    """
    Purpose
        Checks if the given list has no data in it
    Pre-conditions:
        :param alist: a list created by create()
    Return:
        :return True if the list has no data, or False otherwise
    """
    return alist['size'] == 0


def size(alist):
    """
    Purpose
        Returns the number of data values in the given list
    Pre-conditions:
        :param alist: a list created by create()
    Return:
        :return The number of data values in the list
    """
    return alist['size']


def add_to_front(alist, val):
    """
    Purpose
        Insert val into alist at the front of the node chain
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        The list increases in size.
        The new value is at index 0.
        The values previously in the list appear after the new value.
    Return:
        :return None
    """
    new_first_node = node.create(val, alist['head'])
    alist['head'] = new_first_node

    # special case: empty linked-list
    if alist['size'] == 0:
        alist['tail'] = new_first_node

    alist['size'] += 1
    return None


def add_to_back(alist, val):
    """
    Purpose
        Insert val into alist at the end of the node chain
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        The list increases in size.
        The new value is last in the list.
    Return:
        :return None
    """
    new_last_node = node.create(val)

    # special case: empty linked-list
    if alist['size'] == 0:
        alist['head'] = new_last_node
    else:
        node.set_next(alist['tail'], new_last_node)

    alist['tail'] = new_last_node
    alist['size'] += 1
    return None


def value_is_in(alist, val):
    """
    Purpose
        Check if the given value is in the given list
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        none
    Return:
        :return True if the value is in the list, False otherwise
    """
    # special case: empty linked-list
    if alist['size'] == 0:
        return False
    else:
        walker = alist['head']
        i = 0
        while walker is not None:
            if node.get_data(walker) == val:
                return True
            walker = node.get_next(walker)
            i += 1
    return False


def get_index_of_value(alist, val):
    """
    Purpose
        Return the smallest index of the given val in the given alist.
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        none
    Return:
        :return the tuple (True, idx) if the val appears in alist
        :return the tuple (False, None) if the vale does not appear in alist
    """
    # special case: empty linked-list
    if alist['size'] == 0:
        return False, None
    else:
        walker = alist['head']
        counter = 0
        while walker is not None:
            if node.get_data(walker) == val:
                return True, counter
            walker = node.get_next(walker)
            counter += 1

    return False, None


def retrieve_data_at_index(alist, idx):
    """
    Purpose
        Return the value stored in alist at the index idx
    Preconditions:
        :param alist: a list created by create()
        :param idx:   a non-negative integer, between 0 & n-1 (n = len of alist)
    Post-conditions:
        none
    Return:
        :return (True, val) if val is stored at index idx and idx is valid
        :return (False, None) if the idx is not valid for the list
    """
    # special case: empty linked-list
    if alist['size'] == 0:
        return False, None
    elif idx >= alist['size']:
        return False, None
    else:
        walker = alist['head']
        counter = 0
        while (counter < idx) and (walker is not None):
            walker = node.get_next(walker)
            counter += 1
        val = node.get_data(walker)
        return True, val

    return False, None


def set_data_at_index(alist, idx, val):
    """
    Purpose
        Store val into alist at the index idx
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
        :param idx:   a non-negative integer
    Post-conditions:
        The value stored at index idx changes to val
    Return:
        :return True if the index was valid, False otherwise
    """
    # special case: empty linked-list
    if alist['size'] == 0:
        return False
    # special case: index out of range
    elif idx >= alist['size']:
        return False
    else:
        walker = alist['head']
        counter = 0
        while walker is not None:
            if counter == idx:
                node.set_data(walker, val)
                return True
            walker = node.get_next(walker)
            counter += 1

    return False


def remove_from_front(alist):
    """
    Purpose
        Removes and returns the first value in alist
    Preconditions:
        :param alist: a list created by create()
    Post-conditions:
        The list decreases in size.
        The returned value is no longer in in the list.
    Return:
        :return The tuple (True, value) if alist is not empty
        :return The tuple (False, None) if alist is empty
    """
    # special case: empty linked list
    if alist['size'] == 0:
        return False, None
    elif alist['size'] == 1:
        value = node.get_data(alist['head'])
        alist['head'] = None
        alist['tail'] = None

        alist['size'] -= 1
        return True, value
    else:
        prev_first_node = alist['head']
        value = node.get_data(prev_first_node)
        alist['head'] = node.get_next(prev_first_node)

        alist['size'] -= 1
        return True, value

    return False, None


def remove_from_back(alist):
    """
    Purpose
        Removes and returns the last value in alist
    Preconditions:
        :param alist: a list created by create()
    Post-conditions:
        The list decreases in size.
        The returned value is no longer in in the list.
    Return:
        :return The tuple (True, value) if alist is not empty
        :return The tuple (False, None) if alist is empty
    """
    if alist['size'] ==  0:
        return False, None
    elif alist['size'] == 1:
        value = node.get_data(alist['head'])
        alist['head'] = None
        alist['tail'] = None

        alist['size'] -= 1
        return True, value
    else:
        # retrieve data from tail of linked list
        prev_last_node = alist['tail']
        value = node.get_data(prev_last_node)

        # walk through linked list
        walker = alist['head']
        for i in range(alist['size']-2):
            walker = node.get_next(walker)

        # reassign linked list's tail
        node.set_next(walker, None)
        alist['tail'] = walker

        alist['size'] -= 1
        return True, value
    return False, None


# TODO: complete insert_value_at_index(alist, val, idx)   --- when done, delete this line
def insert_value_at_index(alist, val, idx):
    """
    Purpose
        Insert val into alist at index idx
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
        :param idx:   a valid index for the list
    Post-conditions:
        The list increases in size.
        The new value is at index idx.
        The values previously in the list at idx or later appear after the new value.
    Return:
        :return If the index is valid, insert_value_at_index returns True.
        :return If the index is not valid, insert_value_at_index returns False.
    """
    # special case: index outside of range of linked list
    if idx > alist['size']:
        return False
    # special case: empty linked list
    elif alist['size'] == 0:
        alist['head'] = node.create(val)
        alist['tail'] = alist['head']
        return True
    else:
        new_node = node.create(val)

        # walk through front half of linked list (up to index)

        # walk past index to connect new node to last half of linked list

    return False


# TODO: complete delete_item_at_index(alist, idx)   --- when done, delete this line
def delete_item_at_index(alist, idx):
    """
    Purpose
        Delete the value at index idx in alist.
    Preconditions:
        :param alist: a list created by create()
        :param idx:   a non-negative integer
    Post-conditions:
        The list decreases in size if the index is valid
        The value at idx is no longer in the list.
    Return:
        :return True if index was valid, False otherwise
    """
    # special case: empty linked list
    if alist['size'] == 0:
        return False
    # special case: index outside of range of linked list
    elif (idx >= alist['size']) or (idx < 0):
        return False
    # special case: single item in linked list
    elif alist['size'] == 1:
        alist['head'] = None
        alist['tail'] = None
        alist['size'] -= 1
        return True
    # special case: index at front of list
    elif idx == 0:
        remove_from_front(alist)
        alist['size'] -= 1
        return True
    # special case: index at back of list
    elif idx == alist['size']-1:
        remove_from_back(alist)
        alist['size'] -= 1
        return True
    else:
        # walk through front half of linked list (up to index)
        before_del_node = alist['head']
        counter = 0
        while counter < idx-1:
            before_del_node = node.get_next(before_del_node)
            counter += 1

        # walk past index to connect new node to last half of linked list
        after_del_node = alist['head']
        counter = 0
        while counter <= idx:
            if counter == idx:
                del_node = after_del_node
            after_del_node = node.get_next(after_del_node)
            counter += 1

        # disconnect deleted node
        node.set_next(del_node, None)
        # connect the two nodes across deleted node
        node.set_next(before_del_node, after_del_node)

        alist['size'] -= 1
        return True
    return False
