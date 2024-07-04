from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    data1 = SecretList(Input(name="Data1", party=party1), SecretInteger)
    data2 = SecretList(Input(name="Data2", party=party2), SecretInteger)

    total_sum = sum(data1) + sum(data2) # ... Add sums from other parties

    total_count = len(data1) + len(data2) # ... Add counts from other parties

    mean = total_sum / total_count

    squared_diffs_sum = sum((x - mean)**2 for x in data1) 
    squared_diffs_sum += sum((x - mean)**2 for x in data2)

    variance = squared_diffs_sum / total_count

    std_dev = variance ** 0.5

    return [
        Output(mean, "Mean"),
        Output(variance, "Variance"),
        Output(std_dev, "Standard Deviation")
    ]