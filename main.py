from conditional import conditional_probability
from bayes_rule import get_probability
from combination import choose
from permutation import permuatation

if __name__ == "__main__":
    pB = choose(8,2) + choose(7, 2)
    pA_int_B = choose(8, 2)
    print(conditional_probability(0, pB, pA_int_B)) 
