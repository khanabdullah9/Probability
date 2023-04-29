from common import factorial

def permuatation(n,r):
    n_fact = factorial(n)
    n_r_fact = factorial(n - r)
    
    return n_fact // n_r_fact