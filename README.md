# Projeto - Agrupamento Espectral

## Objetivo

## Grupo
* Aline Laís Tavares
* Géssica Sodré
* João Paulo Araújo

## Tarefas
A seguir, uma leve descrição do que é preciso ser feito para o projeto.

### Escolher um conjunto de dados
O conjunto de dados a ser estudado encontra-se em: https://archive.ics.uci.edu/ml/datasets/Flags
Basicamente, são dados com informações de todas as bandeiras nacionais de cada país existente. Atributos incluem cores das bandeiras, língua do país, continente, etc. São 30 atributos no total e 194 instâncias (bandeiras).

### Preparar conjunto de dados
* Procurar dados em formato inconsistente e: (a) removê-los ou (b) prever seus reais valores pela média de todos os outros. 
No caso dos nosso conjunto de dados, não foram detectados dados inconsistentes.

* Verificar se conjunto de dados possuem atributos nominais e tratá-los.
Será necessário remover atributos nominais e atribuit valores aos mesmos. 
No caso deste conjunto de dados, os atributos de cores predominantes e cores nos cantos esquerda-superior e direita-inferior precisarão ser convertidos em valores, da seguinte forma:

| Cor  |  id |
| ---  | --- |
|blue  | TBA |
|green | TBA |
| red  | TBA |
| gold | TBA |
| ...  | TBA |

...


### Algoritmo de agrupamento espectral a ser utilizado
Dado um conjunto de pontos (os _n_ atributos para cada bandeira)  ![https://www.codecogs.com/eqnedit.php?latex=S&space;=&space;{s_1,\cdots,&space;s_n}&space;\in&space;\mathbb{R}^i](https://latex.codecogs.com/gif.latex?S&space;=&space;{s_1,\cdots,&space;s_n}&space;\in&space;\mathbb{R}^i), é preciso realizar os seguintes passos: [1]
1. Formar a matriz de afinidade ![](https://latex.codecogs.com/gif.latex?A%20%5Cin%20%5Cmathbb%7BR%7D%5E%7Bn%20%5Ctimes%20n%7D) definido por:
	* ![](https://latex.codecogs.com/gif.latex?A_%7Bij%7D%20%3D%20%7B%5Cexp%28-%7C%7Cs_i%20-%20s_j%7C%7C%5E%7B2%7D%7D/%7B2%7D%5Csigma%20%5E2%29)  ![](https://latex.codecogs.com/gif.latex?i%20%5Cneq%20j)
	* ![](https://latex.codecogs.com/gif.latex?A_%7Bij%7D%20%3D%200%2C%20%5C%20se%20%5C%20i%20%3D%20j) 
Lembrando que deve se escolher o melhor valor de ![](https://latex.codecogs.com/gif.latex?%5Csigma), além de definir a distância [2]  euclidiana para dois atributos como, por exemplo, ![](https://latex.codecogs.com/gif.latex?%5Cexp%28-%7C%7Cs_1%20-%20s_2%7C%7C%5E%7B2%7D%29%20%3D%20%5Csqrt%7B%28s_%7Bii%7D%20-%20s_%7B11%7D%29%5E2%20&plus;%20%28s_%7B12%7D-s_%7B22%7D%29%20&plus;%20%28s_%7B13%7D-s_%7B23%29%5E2%7D%7D) 

2. Definir a matriz diagonal onde o ![](https://latex.codecogs.com/gif.latex?%28i%2Ci%29elemento) é a soma dos valores de _A_ na _i-ésima_ linha. E com isso, construir a matriz ![](https://latex.codecogs.com/gif.latex?L%20%3D%20D%5E%7B-1/2%7D%20A%5Ccdot%20D%5E%7B-1/2%7D)

3. Achar ![](https://latex.codecogs.com/gif.latex?x_1%2C%20x_2%2C%20%5Ccdots%20x_k), maiores _k_ autovetores de _L_ (escolhidos para serem ortogonal um ao outro no caso de autovalores repetidos) e formar a matrix ![](https://latex.codecogs.com/gif.latex?X%20%3D%20%5Bx_1%20x_2%20%5Ccdots%20x_k%5D%20%5Cin%20%5Cmathbb%7BR%7D%5E%7Bn%20%5Ctimes%20k%7D) através do empilhamento dos autovetores em colunas.

4. Formar a matriz _Y_ a partir de _X_ através da renormalização  de cada linha de X para ter uma unidade de largura( ex: ![](https://latex.codecogs.com/gif.latex?I_%7Bij%7D%20%3D%20%5Cfrac%7BX_%7Bij%7D%7D%7B%28%5Csum_%7Bj%7D%20X_%7Bij%7D%5E2%29%5E%7B1/2%7D%7D) ).

5. Tratar cada linha de Y como um ponto em ![](https://latex.codecogs.com/gif.latex?%5Cmathbb%7BR%7D%5Ek), agrupando-os em _k_ grupos através do _K-means_ ou outro algorítmo (na tentativa de minimizar distorções).

6. Finalmente, atribuir aos pontos originais ![](https://latex.codecogs.com/gif.latex?s_i) ao grupo _j_ se e somente se a linha _i_ da matriz _Y_ foi atribuida ao grupo _j_.


### Resultados Experimentais


## Referências
[1] Ng, A., Jordan, M., Weiss, Y.: [On Spectral Clustering: Analysis and an algorithm.](https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/ng-nips-01.pdf) In: Dietterich, T., Becker, S., Ghahramani, Z. (eds.) Advances in Neural Information Processing Systems 14, pp. 849–856. MIT Press, Cambridge (2002).
[2] Euclidean distance, 24 May 2017. In _Wikipedia: The Free Encyclopedia_. Wikimedia Foundation Inc. Encyclopedia on-line. Available from https://en.wikipedia.org/wiki/Euclidean_distance#n_dimensions. Retrieved at 21 June 2014.
