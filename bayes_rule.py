"""
P(A | B) = P(B | A) * P(A) / P(B)
"""
def get_probability(pA,pB,pBgivenA):
    return (pBgivenA * pA) / pB
