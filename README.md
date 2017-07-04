# Projeto - Agrupamento Espectral

## Requisitos
- Python >= 3.4.*

Para rodar:
- python3 clustering.py --test

_--test_ é um argumento opcional, para caso deseja ver alguma matriz de resultado
_--clean_ é um argumento opção que realiza a limpeza dos dados, tratando os atributos nominais.

Lembrar de instalar as bibliotecas necessárias (descritas no passo 3) como sudo (se não utilizar um ambiente virtual).

## Objetivo

## Grupo
* Aline Laís Tavares
* Géssica Sodré
* João Paulo Araújo

### To-do list
Completo até o passo 4 do algoritmo. Falta fazer a partir do passo 5 (K-means)

## Tarefas
A seguir, uma leve descrição do que é preciso ser feito para o projeto.

### Escolher um conjunto de dados
O conjunto de dados a ser estudado encontra-se em: https://archive.ics.uci.edu/ml/datasets/Flags
Basicamente, são dados com informações de todas as bandeiras nacionais de cada país existente. Atributos incluem cores das bandeiras, língua do país, continente, etc. São 30 atributos no total e 194 instâncias (bandeiras).

### Preparar conjunto de dados
* Procurar dados em formato inconsistente e: (a) removê-los ou (b) prever seus reais valores pela média de todos os outros. 
No caso dos nosso conjunto de dados, não foram detectados dados inconsistentes.

* Verificar se conjunto de dados possuem atributos nominais e tratá-los.
No caso deste conjunto de dados, os atributos de cores predominantes e cores nos cantos esquerda-superior e direita-inferior foram convertidos em valores, representados por um identificador, como descrito na tabela a seguir:

| Cor  |  id |
| ---  | --- |
| green  | 0 |
| black | 1 |
| red  | 2 |
| white | 3 |
| blue  | 4 |
| gold  | 5 |
| orange  | 6 |
| brown  | 7 |



### Algoritmo de agrupamento espectral a ser utilizado
Dado um conjunto de pontos (os _n_ atributos para cada bandeira)  ![https://www.codecogs.com/eqnedit.php?latex=S&space;=&space;{s_1,\cdots,&space;s_n}&space;\in&space;\mathbb{R}^i](https://latex.codecogs.com/gif.latex?S&space;=&space;{s_1,\cdots,&space;s_n}&space;\in&space;\mathbb{R}^i), é preciso realizar os seguintes passos: [1]

1. Formar a matriz de afinidade ![](https://latex.codecogs.com/gif.latex?A%20%5Cin%20%5Cmathbb%7BR%7D%5E%7Bn%20%5Ctimes%20n%7D) definido por:
	* ![](https://latex.codecogs.com/gif.latex?A_%7Bij%7D%20%3D%20%7B%5Cexp%28-%7C%7Cs_i%20-%20s_j%7C%7C%5E%7B2%7D%7D/%7B2%7D%5Csigma%20%5E2%29)  ![](https://latex.codecogs.com/gif.latex?i%20%5Cneq%20j)
	* ![](https://latex.codecogs.com/gif.latex?A_%7Bij%7D%20%3D%200%2C%20%5C%20se%20%5C%20i%20%3D%20j) 
Lembrando que deve se escolher o melhor valor de ![](https://latex.codecogs.com/gif.latex?%5Csigma), além de definir a distância [2]  euclidiana para dois atributos. No caso, temos:
 ![](https://latex.codecogs.com/gif.latex?%7C%7Cs_i%20-%20s_j%7C%7C%5E2%20%3D%20%5Csqrt%7B%5Csum_%7Bi%3D0%7D%5E%20d%20%28x_%7Bid%7D-x_%7Bjd%7D%29%5E2%7D) 

2. Definir a matriz diagonal onde o ![](https://latex.codecogs.com/gif.latex?%28i%2Ci%29elemento) é a soma dos valores de _A_ na _i-ésima_ linha. E com isso, construir a matriz ![](https://latex.codecogs.com/gif.latex?L%20%3D%20D%20-%20A)

3. Achar ![](https://latex.codecogs.com/gif.latex?x_1%2C%20x_2%2C%20%5Ccdots%20x_k), maiores _k_ autovetores de _L_ (escolhidos para serem ortogonal um ao outro no caso de autovalores repetidos) e formar a matrix ![](https://latex.codecogs.com/gif.latex?X%20%3D%20%5Bx_1%20x_2%20%5Ccdots%20x_k%5D%20%5Cin%20%5Cmathbb%7BR%7D%5E%7Bn%20%5Ctimes%20k%7D) através do empilhamento dos autovetores em colunas.

Achar autovetores e autovalores: https://stackoverflow.com/questions/6684238/whats-the-fastest-way-to-find-eigenvalues-vectors-in-python

Para usar a biblioteca SciPy, NumPy e plot gráfico, instalar as seguintes bibliotecas:

```sh
pip3 install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
sudo apt-get install python3-tk
```

4. Formar a matriz _Y_ a partir de _X_ através da renormalização  de cada linha de X para ter uma unidade de largura( ex: ![](https://latex.codecogs.com/gif.latex?Y_%7Bij%7D%20%3D%20%5Cfrac%7BX_%7Bij%7D%7D%7B%5Csum_j%7B%28X_%7Bij%7D%5E2%7D%29%5E%7B1/2%7D%7D) ).


5. Tratar cada linha de Y como um ponto em ![](https://latex.codecogs.com/gif.latex?%5Cmathbb%7BR%7D%5Ek), agrupando-os em _k_ grupos através do _K-means_ ou outro algorítmo (na tentativa de minimizar distorções). Ou seja, escolher a quantidade de clusters _k_ e aplicar algum algorítmo de K-means, da forma que se consiga obter dados satisfatórios. Comece por algum tamanho k=2 e pode ir aumentando até obter osmelhores grupos possíveis.

Possível algorítmo de K-means que pode ser utilizado:
http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

6. Finalmente, atribuir aos pontos originais ![](https://latex.codecogs.com/gif.latex?s_i) ao grupo _j_ se e somente se a linha _i_ da matriz _Y_ foi atribuida ao grupo _j_. Em outras palavras, após realizar o K-means, associar um nome/significado a cada ponto de forma que estes representem os nomes das flags inicialmente sendo utilizadas. Por exemplo, se a linha Y[0] da matriz Y estiver em um cluster qualquer representada por um ponto, esse ponto especifico é o ponto _Afghanistan_.


### Resultados Experimentais


## Referências
[1] Ng, A., Jordan, M., Weiss, Y.: [On Spectral Clustering: Analysis and an algorithm.](https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/ng-nips-01.pdf) In: Dietterich, T., Becker, S., Ghahramani, Z. (eds.) Advances in Neural Information Processing Systems 14, pp. 849–856. MIT Press, Cambridge (2002).

[2] Euclidean distance, 24 May 2017. In _Wikipedia: The Free Encyclopedia_. Wikimedia Foundation Inc. Encyclopedia on-line. Available from https://en.wikipedia.org/wiki/Euclidean_distance#n_dimensions. Retrieved at 21 June 2014.
