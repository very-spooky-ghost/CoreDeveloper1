#!/usr/bin/env python

# Week 2 Exercises: Naming

# Rewrite the two functions below.

# In your commit message, explain what was wrong and how you fixed it.

#-----------------------------------------------------------------------------#
#                                 FUNCTION 1                                  #
#-----------------------------------------------------------------------------#
# FUNCTION 1: Check for a specific value in a list


# ORIGINAL FUNCTION 1
# ===================
'''
def checkNums(l):
    if 1 in l:
        print "There is a 1"
        return
    else:
        for o in l:
            print o
        return
'''

# FIXED FUNCTION 1
# ================
"""
Changes:
--------
- func name camelCase --> snake_case
    WHY: * PEP8 standard python style
           (https://www.python.org/dev/peps/pep-0008/#id45)
         * it's way better than camel case

- made search value an argument
    WHY: the function is meaningless otherwise
         (`def print_if_number_1_is_in_list_or_print_anyway`)

- changed param name
    WHY: never name anything as a single 'l', it can be confused as number 1

- changed behavior of function to return bool based on membership
    WHY: we're checking for a 'specific value in a list', not
         randomly printing shit

"""

def check_nums(nums, val=1):
    """ Check if a specific value <val> is in a list <nums> """
    if val in set(nums):
        print(f"There is a {repr(val)}")
        return True
    return False


#-----------------------------------------------------------------------------#
#                                 FUNCTION 2                                  #
#-----------------------------------------------------------------------------#
# FUNCTION 2: Pick out even numbers


# ORIGINAL FUNCTION 2
# ===================
'''
def evenStevens(thing):
    thanos = []
    for avenger in thing:
        if (avenger % 2) == 0:
            thanos.append(avenger)
    print "I AM INEVITABLE"
    print thanos
    return thanos
'''

# FIXED FUNCTION 2
# ================
"""
Changes:
--------
- func name camelCase --> snake_case
    WHY: * PEP8 standard python style
           (https://www.python.org/dev/peps/pep-0008/#id45)
         * it's way better than camel case

- changed func arg name and return var name
    WHY: `thing` is too vague; we can at least assume it is some collection or
         non-string iterable

- added assertion on input collection member type
    WHY: since we are looking for evens, we should only be considering
         ints--no other data-type is sensical

- removed irrelevant prints
    WHY: they are irrelevant

"""

def select_evens(nums):
    """ Select even numbers from input collection <nums>

    Params
    ------
    nums : (collection) {list, set, tuple}
        some non-string iterable collection data structure like lists

    Returns
    -------
    evens : list
        list of evens in nums; empty if no evens
    """
    evens = []
    for i in nums:
        assert isinstance(i, int)
        if not (i % 2): evens.append(i)
    return evens

