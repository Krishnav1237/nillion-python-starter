from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    set1 = SecretList(Input(name="Set1", party=party1), SecretInteger)
    set2 = SecretList(Input(name="Set2", party=party2), SecretInteger)

    intersection = []
    for element1 in set1:
        for element2 in set2:
            if hash(element1) == hash(element2):
                intersection.append(element1)

    return [Output(intersection, "intersection", party1)]