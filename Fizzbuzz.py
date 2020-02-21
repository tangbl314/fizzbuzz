# Making a Fizzbuzz Program

# import necessary supporting libraries or packages
from numbers import Numbers

def fizz(x):
    # Determine if x is a number or not
    if isinstance(x, Number):
        # yes, it is a number and a multiple of 3
        if x % 3 == 0:
            return 'fizz'
        else:
            return x
        else:
            # no, it is NOT a number
            return x














for each in range(1, 101):
    if each % 3 == 0 and each % 5 == 0:
        print ('fizzbuzz')
    elif each % 5 == 0:
        print ('buzz')
    elif each % 3 == 0:
        print ('fizz')
    else:
        print (each)
