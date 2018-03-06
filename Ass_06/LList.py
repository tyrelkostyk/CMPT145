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
    else:
        walker = alist['head']
        counter = 0
        while (counter < idx) and (walker is not None):
            walker = node.get_next(walker)
            counter += 1
        if walker is None:
            return False, None
        else:
            val = node.get_data(walker)
            return True, val

    return False, None


# TODO: complete set_data_at_index(alist, idx, val)   --- when done, delete this line
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
    return False


# TODO: complete remove_from_front(alist)   --- when done, delete this line
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
    return False, None

# TODO: complete remove_from_back(alist)   --- when done, delete this line
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
    return False
