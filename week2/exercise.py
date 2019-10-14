#!/usr/bin/env python

# Week 2 Exercises: Naming

# Rewrite the two functions below.

# In your commit message, explain what was wrong and how you fixed it.

# FUNCTION 1: Check for a specific value in a list

def checkNums(l):
    if 1 in l:
        print "There is a 1"
        return
    else:
        for o in l:
            print o
        return

# FUNCTION 2: Pick out even numbers

def evenStevens(thing):
    thanos = []
    for avenger in thing:
        if (avenger % 2) == 0:
            thanos.append(avenger)
    print "I AM INEVITABLE"
    print thanos
    return thanos
