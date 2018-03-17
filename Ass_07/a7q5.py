## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## A7q5; due Saturday March 17th, 2018, 10pm

# a)
def fibonacci(n):
    '''
    returns the value of the nth fibonacci number
    :params:
    n - non-negative integer
    :returns: the value of the nth fibonacci number
    '''
    # base case
    if (n == 0) or (n == 1):
        return n
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)

# b)
def moosonacci(n):
    '''
    returns the value of the nth moosonacci number
    :params:
    n - non-negative integer
    :returns: the value of the nth moosonacci number
    '''
    # base case
    if n in (0,1,2):
        return n
    elif n > 2:
        return moosonacci(n-1) + moosonacci(n-2) + moosonacci(n-3)

# c)
def substr(s, c, r):
    '''
    composes new string, identical to s except every instance of c replaced with r
    :params:
    s - string, which you wish to edit
    c - string, "target" which you wish to replace with r
    r - string, will replace c
    :returns: the new string
    '''
    # base case
    if s.count(c) == 0:
        return s
    else:
        if s[0] == c:
            return r + substr(s[1:len(s)],c,r)
        else:
            return s[0] + substr(s[1:len(s)],c,r)
