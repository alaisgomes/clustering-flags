import math
import csv
import numpy as np
import sys
import scipy
import scipy.linalg
import matplotlib.pyplot as plt

SIGMA = 20.0
N_INSTANCES = 194

final_file = "data/formatted.csv"

def initialize_matrix(size=N_INSTANCES):
    matrix = np.mat([
        [0.0 for i in range(N_INSTANCES)] 
        for j in range(N_INSTANCES)
    ])

    return matrix

def euclidean_ditance(s1, s2):
    value = 0.0

    for i in range(1,30):
        value += math.pow((int(s1[i]) - int(s2[i])), 2)

    return math.sqrt(value)

   
def affinity_matrix(pfile):

    with open(pfile, 'r') as csvfile:
        flags_reader = csv.reader(csvfile, delimiter=',')
        flags = list(flags_reader)

        matrix = initialize_matrix()
        i = 0
        j = 0

        sig_pow = 2*pow(SIGMA, 2)

        for s1 in flags:
            j = 0
            for s2 in flags:
                if (i != j):
                    ed = euclidean_ditance(s1, s2)    
                    matrix[i,j] = math.exp(-(ed/sig_pow))

                j += 1
            i += 1

    csvfile.close()

    return matrix


def laplacian_matrix(A):
    D = initialize_matrix()
    L = initialize_matrix()

    # for i in range(N_INSTANCES):
    #     D[i, i] = A.sum(axis=i)

    np.fill_diagonal(D, A.sum(axis=1))

    for i in range(N_INSTANCES):
        for j in range(N_INSTANCES):
            L[i, j] = D[i, j] - A[i, j]
    return L   

def eigen_vectors(L):
    e_vals, e_vecs = scipy.linalg.eig(L)
    return (e_vals, e_vecs)


def sum_line_values(line):
    total = 0.0

    for item in line:
        total += math.pow(item, 2)

    return total

def renormalize_matrix(X):
    Y = initialize_matrix()

    for i in range(N_INSTANCES):
        sum_i = math.sqrt(sum_line_values(X[i, :]))
        for j in range(N_INSTANCES):
            Y[i, j] = X[i, j]/sum_i

    return Y