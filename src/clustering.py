# Universidade de Brasilia
# TAG - Teoria e Aplicacao de Grafos
# Projeto - Agrupamento Espectral

import csv

data_file = "data/flag.csv"

def main():
    with open(data_file, 'rb') as csvfile:
        flags_reader = csv.reader(csvfile, delimiter=',')

        for flag in flags_reader:
            print (flag[0])
            

if __name__ == '__main__':
    main()