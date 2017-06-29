import math
import csv
import sys
# from scipy import linalg as LA

SIGMA = 0.3
N_INSTANCES = 194

def initialize_matrix(size=N_INSTANCES):
    matrix = [
        [0.0 for i in range(N_INSTANCES)] 
        for j in range(N_INSTANCES)
    ]

    return matrix

def euclidean_ditance(s1, s2):
    value = 0.0

    for i in range(1,30):
        value += math.pow((int(s1[i]) - int(s2[i])), 2)

    return math.sqrt(value)

   
def affinity_matrix(pfile):

    with open(pfile, 'rb') as csvfile:
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
                    matrix[i][j] = math.exp(-(ed/sig_pow))

                j += 1
            i += 1


    csvfile.close()

    return matrix

def sum_line_values(line):
    total = 0.0
    for item in line:
        total += item

    return total

def laplacian_matrix(A):
    D = initialize_matrix()
    L = initialize_matrix()

    for i in range(N_INSTANCES):
        D[i][i] = sum_line_values(A[i])

    for i in range(N_INSTANCES):
        for j in range(N_INSTANCES):
            L[i][j] = D[i][j] - A[i][j]

    return L

    

def eigen_vectors(L):
#    e_vals, e_vecs = LA.eig(A)
#    print (e_vals)
    pass


def main():
    if ("--test" in sys.argv):
        A = affinity_matrix("data/formatted.csv")
        laplacian_matrix(A)


if __name__ == '__main__':
    main()