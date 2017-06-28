# Universidade de Brasilia
# TAG - Teoria e Aplicacao de Grafos
# Projeto - Agrupamento Espectral

import csv

data_file = "data/formated.csv"

# class InconsistencyException(Exception):
#     def __init__(self, value, country):
#         self.value = value
#         self.country = country


def test_int_in_range(value, myrange, test_type):
    if int(value) not in myrange:
        raise ValueError

def test_is_int(value, test_type):
    if not isinstance(int(value), int):
        raise ValueError

def test_bool(color, type):
    if int(color) not in range(0,2):
        raise ValueError 

def main():
    with open(data_file, 'r') as csvfile:
        flags_reader = csv.reader(csvfile, delimiter=',')

        for flag in flags_reader:
            print (flag[0])
            test_int_in_range(flag[1], range(1,7), "landmass")
            test_int_in_range(flag[2], range(1,5), "zone")
            test_is_int(flag[3], "area")
            test_is_int(flag[4], "population")
            test_int_in_range(flag[5], range(1,11), "language")
            test_int_in_range(flag[6], range(0,8), "religion")
            test_is_int(flag[7], "total_bars")
            test_is_int(flag[8], "total_stripes")
            test_is_int(flag[9], "total_colors")

            for i in range(10,17):
                test_bool(flag[i], "color_present")

            # 17 = mainhue
            test_int_in_range(flag[17], range(0,8), "main_hue")

            test_is_int(flag[18], "total_circles")
            test_is_int(flag[19], "total_crosses")
            test_is_int(flag[20], "total_saltires")
            test_is_int(flag[21], "total_quarters")
            test_is_int(flag[22], "total_sunstars")

            test_bool(flag[23], "crescent_moon")
            test_bool(flag[24], "triangle")
            test_bool(flag[25], "icon")
            test_bool(flag[26], "animate")
            test_bool(flag[27], "text")

            # 28: topleft color - name
            # 29 : bottom right color - name

    csvfile.close()            

if __name__ == '__main__':
    main()
