# Universidade de Brasilia
# TAG - Teoria e Aplicacao de Grafos
# Projeto - Agrupamento Espectral

import csv
import sys
import os
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from matrix import affinity_matrix, laplacian_matrix
from matrix import eigen_vectors, renormalize_matrix
from matrix import apply_k_means, create_model

data_file = "data/flag.csv"
formatted_data_file = "data/formatted.csv"


def clean(flags):
    print ("\nCleaning data set. Setting nominal colors with following ids:")

    colors = []

    with open(formatted_data_file, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter =',')
        
        i = 0
        for flag in flags:
            row = []
            for index, value in enumerate(flag):                
                if not (index == 17 or index == 28 or index == 29):
                    row.append(value)
                else:
                    if value not in colors:
                        colors.append(value)
                        print ("[{}]: {} \
                           ".format(colors.index(value), colors[len(colors)-1]))

                    row.append(colors.index(value))

            spamwriter.writerow(row)
    csvfile.close()


def process_args():
    not_silent = False
    with open(data_file, 'rb') as csvfile:
        flags_reader = csv.reader(csvfile, delimiter=',')

        for arg in sys.argv:
            if (arg == '--clean'):
                clean(flags_reader)
            if (arg == '--test'):
                not_silent =  True

    csvfile.close()

    return not_silent


def main():   

    not_silent = process_args()

    # passo 1
    A, labels = affinity_matrix(formatted_data_file)

    # passo 2
    L = laplacian_matrix(A)

    # passo 3
    e_values, X = eigen_vectors(L)

    # passo 4
    Y = renormalize_matrix(X)

    # passo 5
    Z, dist = apply_k_means(Y)

    # passo 6
    k_const = create_model(Y, Z, labels, dist)


    result = Y # substitua pela matriz que deseja imprimir na tela

    if (not_silent):
        print("Clusters used: {}.\nData:".format(K_CONST))
        print (result)
                 

if __name__ == '__main__':
    main()
