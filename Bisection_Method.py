import numpy as np


def FindZerosUsingBisection(func, a , b, tolerance=10**(-3)):
    if func(a)*func(b) > 0:
        print('Hypothesis of the bisection method is satisfied')
        return None

    elif func(a) == 0:
        return a
    elif func(b) == 0:
        return b
    else:
        c = (a+b)/2

        while np.abs(func(c)) > tolerance:
            if func(a)*func(c) < 0:
                b = c
                c = (a+b)/2

            elif func(b)*func(c) < 0:
                a = c
                c = (a+b)/2

            elif func(c) == 0:
                return c
            else:
                print('Unexpected case encountered')
                print(func(a))
                print(func(b))
                print(func(c))
                return None

        return c
            
                
            
    
    
