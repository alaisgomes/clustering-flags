# Universidade de Brasilia
# TAG - Teoria e Aplicacao de Grafos
# Projeto - Agrupamento Espectral

import csv
import sys
import os


data_file = "data/flag.csv"
formatted_data_file = "data/formatted.csv"

def clean(flags):
    print ("Cleaning data set. Setting nominal colors with following ids:")

    colors = []

    with open('data/formatted.csv', 'wb') as csvfile:
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


def process_args(flags_reader):
    for arg in sys.argv:
        if (arg == '--clean'):
            clean(flags_reader)


def main():   
    with open(data_file, 'rb') as csvfile:
        flags_reader = csv.reader(csvfile, delimiter=',')
        
        process_args(flags_reader)
        

    csvfile.close()
            
            

if __name__ == '__main__':
    main()
