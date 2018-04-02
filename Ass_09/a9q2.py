## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a9 due Monday April 2nd 2018

## Adaptation of bstprim.py that uses Key-Value TreeNodes instead of regular TreeNodes
## The implementation of the KVTreeNode is extremely similar to its TreeNode predecessor

import KVTreeNode as TN

def member_prim(tnode, key):
    """
    Purpose:
        Check if value is stored in the binary search tree.
    Preconditions:
        :param tnode: a KVTreeNode with the BST property
        :param key: a key
    Postconditions:
        none
    :return: a pair True, value if key is in the tree
             a pair False, None if the key is not in the tree
    """
    if tnode is None:
        return False, None
    elif tnode.key is key:
        return True, tnode.value
    elif key < tnode.key:
        return member_prim(tnode.left, key)
    else:
        return member_prim(tnode.right, key)


def insert_prim(tnode, key, value):
    """
    Insert a new key,value into the binary search tree.
    Preconditions:
        :param tnode: a KVTreeNode with the BST property
        :param key: a key
    Postconditions:
        If the key is not already in the tree, it is added.
        If the key is already in the tree, the old value is replaced
        with the given value.
    Return
        :return: tuple (flag, tree)
        flag is True if insertion succeeded;
                tree contains the new key-value
        flag is False if the value is already in the tree,
                the value stored with the key is changed
    """
    if tnode is None:
        return True, TN.KVTreeNode(key, value)
    else:
        if tnode.key is key:
            return False, tnode
        elif key < tnode.key:
            left, left_val = insert_prim(tnode.left, key, value)
            if left:
                tnode.left = left_val
                return True, tnode
            return True, tnode
        else:
            right, right_val = insert_prim(tnode.right, key, value)
            if right:
                tnode.right = right_val
                return True, tnode
            return True, tnode

    return False, None



def delete_prim(tnode, key):
    """
    Delete a value from the binary search tree.
    Preconditions:
        :param tnode: a KVTreeNode with the BST property
        :param key: a key
    Postconditions:
        If the key is in the tree, it is deleted.  The tree
        retains the binary search tree property.
        If the key is not there, there is no change to the tree.
    Return
        :return: tuple (flag, tree)
        flag is True if deletion succeeded;
                tree is the resulting without the value
        flag is False if the value was not in the tree,
                tree returned unchanged
    """
    def delete(tnode):
        if tnode is None:
            return False, tnode
        else:
            ckey = tnode.key
            if ckey == key:
                return reconnect(tnode)
            elif key < ckey:
                flag, subtree = delete(tnode.left)
                if flag:
                    tnode.left = subtree
                return flag, tnode
            else:
                flag, subtree = delete(tnode.right)
                if flag:
                    tnode.right = subtree
                return flag, tnode

    def reconnect(delthis):
        if delthis.left is None and delthis.right is None:
            # the deleted node has no children
            return True, None
        elif delthis.left is None:
            # the deleted node has one child
            return True, delthis.right
        elif delthis.right is None:
            # the deleted node has one child
            return True, delthis.left
        else:
            # the deleted node has two children
            left = delthis.left
            right = delthis.right
            # walk all the way to the right from left
            walker = left
            while walker.right is not None:
                walker = walker.right
            walker.right = right
            return True, left

    return delete(tnode)
