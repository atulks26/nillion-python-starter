from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")

    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    #result = my_int1^2 + my_int1*my_int2 + my_int2^2 (POLYNOMIAL)
    term1 = my_int1 * my_int1
    term2 = my_int1 * my_int2
    term3 = my_int2 * my_int2

    result = term1 + term2 + term3

    return [Output(result, "polynomial_result", party1)]