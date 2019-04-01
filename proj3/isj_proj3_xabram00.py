#!/usr/bin/env python3

import re

# ukol za 2 body
def first_odd_or_even(numbers):
    """Returns 0 if there is the same number of even numbers and odd numbers
       in the input list of ints, or there are only odd or only even numbers.
       Returns the first odd number in the input list if the list has more even
       numbers.
       Returns the first even number in the input list if the list has more odd 
       numbers.

    >>> first_odd_or_even([2,4,2,3,6])
    3
    >>> first_odd_or_even([3,5,4])
    4
    >>> first_odd_or_even([2,4,3,5])
    0
    >>> first_odd_or_even([2,4])
    0
    >>> first_odd_or_even([3])
    0
    """
    #EL - even list; OL - odd list
    EL,OL=[],[]
    OL=[x for x in numbers if not x % 2]
    EL=[x for x in numbers if x % 2]
    if len(OL)<len(EL) and OL:
        return OL[0]     
    elif len(OL)>len(EL) and EL:
        return EL[0]        
    return 0

# ukol za 3 body
def to_pilot_alpha(word):
    """Returns a list of pilot alpha codes corresponding to the input word

    >>> to_pilot_alpha('Smrz')
    ['Sierra', 'Mike', 'Romeo', 'Zulu']
    """

    pilot_alpha = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot',
        'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike',
        'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango',
        'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']

    pilot_alpha_list = []
    #list extends by pilots names, if first letter in name is equal to letter in 'word'
    #UPD: was deleted exception for "4"-Romeo (lambda x: (x[0]==sm.upper()) or (sm=="4" and x[0]=="R"))
    for sm in word:
        pilot_alpha_list.extend(list(filter(lambda x: x[0]==sm.upper(), pilot_alpha)))
    return pilot_alpha_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
