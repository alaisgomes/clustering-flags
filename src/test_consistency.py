# Universidade de Brasilia
# TAG - Teoria e Aplicacao de Grafos
# Projeto - Agrupamento Espectral

import csv
import pytest

data_file = "data/flag.csv"

class InconsistencyException(Exception):
    def __init__(self, value, country):
        self.value = value
        self.country = country


def test_landmass(land):
    if int(land) not in range(1,7):
        print(land)
        raise ValueError

def test_zone(zone):
    if int(zone) not in range(1,5):
        raise ValueError

def test_area(area):
    if not isinstance(int(area), int):
        raise ValueError

def test_population(pop):
    if not isinstance(int(pop), int):
        raise ValueError

def test_language(lang):
    if int(lang) not in range(1,11):
        raise ValueError

def test_religion(reli):
    if int(reli) not in range(0,8):
        raise ValueError

def test_bars(bars):
    if not isinstance(int(bars), int):
        raise ValueError

def test_stripes(stripes):
    if not isinstance(int(stripes), int):
        raise ValueError

def test_stripes(stripes):
    if not isinstance(int(stripes), int):
        raise ValueError


def main():
    try:
        with open(data_file, 'r') as csvfile:
            flags_reader = csv.reader(csvfile, delimiter=',')

            for flag in flags_reader:
                print (flag)
                test_landmass(flag[1])
                test_zone(flag[2])
                test_area(flag[3])
                test_population(flag[4])
                test_language(flag[5])
                test_religion(flag[6])
                test_bars(flag[7])


        csvfile.close()
    
    except:
        print("Inconsistent")
            

if __name__ == '__main__':
    main()
