import math
import csv
import numpy as np
import sys
import scipy
import scipy.linalg
import matplotlib.pyplot as plt
from scipy.cluster.vq import * #kmeans,vq, whiten
import pylab

# Constantes para modificar e obter resultados
SIGMA = 13.0
K_CONST = 10   
ATTRIBUTES_RANGE = range(3,5)

final_file = "data/formatted.csv"
N_INSTANCES = sum(1 for line in open(final_file))


def initialize_matrix(size=N_INSTANCES):
    matrix = np.mat([
        [0.0 for i in range(N_INSTANCES)] 
        for j in range(N_INSTANCES)
    ])

    return matrix

def euclidean_ditance(s1, s2):
    value = 0.0

    for i in ATTRIBUTES_RANGE:
        value += math.pow((int(s1[i]) - int(s2[i])), 2)

    return math.sqrt(value)


def affinity_matrix(pfile):

    with open(pfile, 'r') as csvfile:
        flags_reader = csv.reader(csvfile, delimiter=',')
        flags = list(flags_reader)

        labels = [x[0] for x in flags]

        matrix = initialize_matrix()
        i = 0
        j = 0

        sig_pow = 2*pow(SIGMA, 2)

        for i in range(N_INSTANCES):
            s1 = flags[i]
            for j in range(N_INSTANCES):
                s2 = flags[j]
                if (i != j):
                    ed = euclidean_ditance(s1, s2)    
                    matrix[i,j] = math.exp(-(ed/sig_pow))


    csvfile.close()

    return matrix, labels


def laplacian_matrix(A):
    D = initialize_matrix()
    L = initialize_matrix()

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

# def apply_k_means(Y):
#     W = whiten(Y)
#     return kmeans(Y,K_CONST)
    #return KMeans(n_clusters=2, random_state=0).fit(Y)

def apply_k_means(Y, labels):
    data = Y
    initial = [kmeans(data,i) for i in range(1,K_CONST)]
    #plt.plot([var for (cent,var) in initial])
    #plt.show()

    cent, var = initial[1]
    assignment,cdist = vq(data,cent)
    print(assignment)

    X = data[:,0]
    Y = data[:,1]

    plt.scatter(X, Y, c=assignment)

#    for i, txt in enumerate(labels):
#        plt.annotate(txt, (X[i],Y[i]))

    plt.show()

    # plt.plot(data[:][0], data[:][1], linestyle="-")
    #plt.show()

    return K_CONST