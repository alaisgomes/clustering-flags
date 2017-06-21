# Projeto - Agrupamento Espectral

## Objetivo

## Grupo
Aline Laís Tavares
Géssica Sodré
João Paulo Araújo

## Tarefas
A seguir, uma leve descrição do que é preciso ser feito para o projeto.

### Escolher um conjunto de dados
O conjunto de dados a ser estudado encontra-se em: https://archive.ics.uci.edu/ml/datasets/Flags
Basicamente, são dados com informações de todas as bandeiras nacionais de cada país existente. Atributos incluem cores das bandeiras, língua do país, continente, etc. São 30 atributos no total e 194 instâncias (bandeiras).

### Preparar conjunto de dados
1. Procurar dados em formato inconsistente e: (a) removê-los ou (b) prever seus reais valores pela média de todos os outros. 
No caso dos nosso conjunto de dados, não foram detectados dados inconsistentes

2. Verificar se conjunto de dados possuem atributos nominais e tratá-los.
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


### Algorítmo de agrupamento espectral a ser utilizado
Dado um conjunto de pontos (os _n_ atributos para cada bandeira) \\((S = {s_1,\cdots, s_n})\\) in \\(\mathbb{R}^i\\), é preciso realizar os seguintes passos: [1]
1. Formar a matriz de afinidade \\(A \in \mathbb{R}^{n \times n}\\) definido por:
	* \\(A_{ij} = {\exp(-||s_i - s_j||^{2}}/{2}\sigma ^2)\\) se \\(i \neq j \\) 
	* \\(A_{ij} = 0\\) se \\(i = j \\) 
Lembrando que deve se escolher o melhor valor de \\(\sigma\\) e a distância euclidiana para dois atributos é, por exemplo, \\( \exp(-||s_1 - s_2||^{2}) = \sqrt{(s_{ii} - s_{11})^2 + (s_{12}-s_{22}) + (s_{13}-s_{23)^2}} \\) [2]

2. Definir a matriz diagonal onde o \\((i,i)\\)_elemento é a soma dos valores de \\(A\\) na \\(i\\)-ésima linha. E com isso, construir a matriz \\(L = D^{-1/2} A\cdot D^{-1/2} \\)

3. Achar \\(x_1, x_2, \cdots x_k\\), maiores _k_ autovetores de _L_ (escolhidos do be ortogonal um ao outro no caso de autovalores repetidos) e formar a matrix \\(X = [x_1 x_2 \cdots x_k] \in \mathbb{R}^{n \times k}\\) através do empilhamento dos autovetores em colunas.

4. Formar a matriz _Y_ a partir de _X_ através da renormalização  de cada linha de X para ter uma unidade de largura( ex: \\( I_{ij} = \frac{X_{ij}}{(\sum_{j} X_{ij}^2)^{1/2}} \\)).

5. Tratar cada linha de Y como um ponto em \\(\mathbb{R}^k\\), agrupando-os em _k_ grupos através do _K-means_ ou outro algorítmo (na tentativa de minimizar distorções).

6. Finalmente, atribuir aos pontos originais \\(s_i\\) ao grupo _j_ se e somente se a linha _i_ da matriz _Y_ foi atribuida ao grupo _j_.


### Resultados Experimentais


## Referências
[1] Ng, A., Jordan, M., Weiss, Y.: [On Spectral Clustering: Analysis and an algorithm.](https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/ng-nips-01.pdf) In: Dietterich, T., Becker, S., Ghahramani, Z. (eds.) Advances in Neural Information Processing Systems 14, pp. 849–856. MIT Press, Cambridge (2002).
[2] Euclidean distance, 24 May 2017. In _Wikipedia: The Free Encyclopedia_. Wikimedia Foundation Inc. Encyclopedia on-line. Available from https://en.wikipedia.org/wiki/Euclidean_distance#n_dimensions. Retrieved at 21 June 2014.