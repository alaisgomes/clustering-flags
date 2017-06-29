import math
import csv

SIGMA = 0.5
# read previous and current line in reader
# calculate the euclidean_distance

def euclidean_ditance(s1, s2):
    value = 0.0

    for i in range(1,30):
        value += math.pow((int(s1[i]) - int(s2[i])), 2)

    return math.sqrt(value)

   
def csv_to_matrix(pfile):
    n = sum(1 for line in open(pfile))

    matrix = [
                [0.0 for i in range(n)] 
                for j in range(n)
            ]


    with open(pfile, 'rb') as csvfile:
        flags_reader = csv.reader(csvfile, delimiter=',')

        i = 0
        j = 0

        sig_pow = pow(SIGMA, 2)

        for line in flags_reader:
            s1 = line
            j = 0
            for row in flags_reader:
                s2 = row
                ed = euclidean_ditance(s1, s2)    
                # print (sig_pow)

                matrix[i][j] = math.pow(math.e, -(ed/sig_pow))

                j += 1

            i += 1


    csvfile.close()

    for i in range (0, 30):
        print (matrix[i])

def affinity_matrix(S):
    pass

def laplacian_matrix(A):
    pass

def eigen_vectors(L):
    pass


def main():
    csv_to_matrix("data/formatted.csv")

if __name__ == '__main__':
    main()