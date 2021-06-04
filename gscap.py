#%%
#Dado um conjunto representado por uma lista, quantos subconjuntos tem a soma divisível por 13
import random as rng
import numpy as np

MOD = 13
N_SIZE = 3
MIN_RANDOM_INT = 1
MAX_RANDOM_INT = 10

def bitmasking(arr, n, mod):
    print(f"Input: {arr}")
    right_subsets = 0
    for i in range(2**n):
        subset_sum = 0
        for j in range(n):
            if (i & (1 << j)) != 0:
                subset_sum+=arr[j]
        if subset_sum % mod == 0:
            right_subsets += 1
    return right_subsets -1 #o teste sempre inclui o conjunto vazio como resposta

input_list = [rng.randint(MIN_RANDOM_INT,MAX_RANDOM_INT) for i in range(N_SIZE)]
answer = bitmasking(input_list,N_SIZE, MOD)
print(f"Resposta: {answer}")