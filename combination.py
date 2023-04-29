from common import factorial

"""
n! / r!(n-r)!
"""
def choose(n,r):
    n_fact = factorial(n)
    r_fact = factorial(r)
    n_r_fact = factorial(n - r)
    return n_fact // ( r_fact * n_r_fact )

