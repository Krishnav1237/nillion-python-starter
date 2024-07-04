from nada_dsl import *

def nada_main():
    # Create a party
    party1 = Party(name="Party1")
    
    # Create secret integers as inputs from the party
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    my_int3 = SecretInteger(Input(name="my_int3", party=party1))
    
    # Define weights
    weight1 = 0.2
    weight2 = 0.3
    weight3 = 0.5
    
    # Write the computation for weighted average
    weighted_sum = weight1 * my_int1 + weight2 * my_int2 + weight3 * my_int3
    total_weight = weight1 + weight2 + weight3
    weighted_average = weighted_sum / total_weight
    
    # Make sure you change the output below to be your new output
    return [Output(weighted_average, "weighted_average_output", party1)]
