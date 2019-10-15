#!/usr/bin/env python

# Week 3 Exercises: Functions

# EXERCISE 1:

# Implement FizzBuzz using function(s) with Clean Code standards

# -----FIZZBUZZ CODE HERE-----
def fizzbuzz(number: int) -> str:
    """
    Implementation of the fizzbuzz algorithm:
        For a given `number`, do the following:
        If the number is divisible by 3 and 5: Return fizzbuzz
        If the number is divisible by 3 but not by 5: Return fizz
        If the number is divisible by 5 but not by 3: Return buzz
        If the number is divisible neither by 3 nor by 5: Return the number
    
    Function returns a string according to the rules above.
    It prints an error and retuns empty string in case you give it something
        other than a number. 
    """

    try:
        if number % 3 == 0 and number % 5 == 0:
            return "fizzbuzz"
        elif number % 3 == 0:
            return "fizz"
        elif number % 5 == 0:
            return "buzz"
        else:
            return str(number)
    except TypeError:
        print("Error: This function only accepts integers.")
        return ""


if __name__ == "__main__":
    # Print fizzbuzz for the first 100 numbers
    for number in range(1, 101):
        print(fizzbuzz(number))


# -----END FIZBUZZ CODE-----

# EXERCISE 2:

# Review the payroll.java code in Listing 3-4 in the book

# Re-implement it as clean Python code. See Listing 3-5 for guidance.

# -----PAYROLL CODE HERE-----


# -----END PAYROLL CODE-----
