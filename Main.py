import Bisection_Method
import numpy as np

def Function(x):
    return np.sqrt(x)-np.cos(x)

print(Bisection_Method.FindZerosUsingBisection(Function, 0, 1, 10**(-12)))


