# include or import this function in your a4q2 submission.
# We might cover exceptions.  Don't worry about it.  Just use it.

def isfloat(str_val):
    """
    Purpose:
        Check whether a string represents a floating point str_val
    Preconditions:
        str_val: a string
    Post-conditions:
        None
    Return: 
        True if str_val can be converted to a floating point number
    """
    try:
        float(str_val)
        return True
    except:
        return False
