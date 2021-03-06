## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab04
## a3, due Friday Feb 2nd 10pm


def create():
    """
    Purpose:
        Create a Statistics record.
    Pre-conditions:
        (none)
    Post-conditions:
        a new record is allocated
    Return:
        A reference to a Statistics record.
    """
    b = {}
    b['count'] = 0      # how many data values have been seen
    b['avg'] = 0        # the running average so far
    b['max'] = None
    b['min'] = None
    return b


def add(stat, value):
    """
    Purpose:
        Use the given value in the calculation of statistics.
    Pre-Conditions:
        stat: a Statistics record
        value: the value to be added
    Post-Conditions:
        none
    Return:
        none
    """
    stat['count'] += 1

    k = stat['count']           # convenience
    diff = value - stat['avg']  # convenience
    stat['avg'] += diff/k

    if stat['max'] == None:
        stat['max'] = value
    else:
        stat['max'] = max(stat['max'], value)

    if stat['min'] == None:
        stat['min'] = value
    else:
        stat['min'] = min(stat['min'], value)
    return


def mean(stat):
    """
    Purpose:
        Return the mean of all the values seen so far.
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        (none)
    Return:
        The mean of the data seen so far.
        Note: if no data has been seen, 0 is returned.
              This is clearly false.
    """
    return stat['avg']


def count(stat):
    """
    Purpose:
        Returns the number of all the values seen so far.
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        (none)
    Return:
        The number of data values seen so far.
    """
    return stat['count']


def maximum(stat):
    """
    Purpose:
        Returns the highest value seen thus far by the stat (None, if no data has been seen)
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        (none)
    Return:
        The highest data value seen so far.
    """
    return stat['max']


def minimum(stat):
    """
    Purpose:
        Returns the lowest value seen thus far by the stat (None, if no data has been seen)
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        (none)
    Return:
        The lowest data value seen so far.
    """
    return stat['min']
