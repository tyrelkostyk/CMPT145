## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## A7q5; due Friday Saturday March 17th, 2018, 10pm

# a)
def fibonacci(n):
    '''
    returns the value of the nth fibonacci number
    :params:
    n - non-negative integer
    :returns: the value of the nth fibonacci number
    '''
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
    if n in (0,1,2):
        return n
    elif n > 2:
        return moosonacci(n-1) + moosonacci(n-2) + moosonacci(n-3)
