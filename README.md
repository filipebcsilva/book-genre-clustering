# Agrupamento de livros por gênero a partir das descrições

Trabalho prático da disciplina de Introdução à Ciência de Dados (UFES). A pergunta é: **dá para descobrir o gênero de um livro só pela sinopse, sem usar rótulos?** Agrupamos cerca de 25 mil livros do Goodreads pelas descrições e depois verificamos se os gêneros reais se concentram em grupos diferentes.

Comparamos duas formas de representar o texto: **TF-IDF + LSA** (abordagem clássica, baseada na frequência das palavras) e **embeddings de um modelo de linguagem** (Sentence Transformers), que captam o significado das frases.

## Resultado principal

Os embeddings formaram grupos bem mais concentrados por gênero que o TF-IDF, com o mesmo número de grupos (k = 24):

| Representação + algoritmo | Grupos | Grupos com ≥ 50% de um gênero | ≥ 60% | ≥ 70% | Média do gênero principal |
| --- | --- | --- | --- | --- | --- |
| TF-IDF + LSA + K-means | 24 | 91,7% | 75,0% | 33,3% | 67,2% |
| TF-IDF + LSA + Hierárquico (Ward) | 16 | 87,5% | 75,0% | 25,0% | 65,0% |
| **Embeddings + K-means** | 24 | **95,8%** | **87,5%** | **50,0%** | **70,9%** |

Os grupos também fazem sentido pelos termos mais característicos. Por exemplo: *planet, alien, galaxy, space* (ficção científica), *murder, case, crime, suspect* (mistério) e *practice, guide, inform* (não ficção prática).

## Metodologia

1. **Pré-processamento:** remoção das descrições que não estão em inglês (com `langdetect`, ficando 24.568 livros), tokenização, minúsculas, remoção de pontuação e stopwords e stemming (Porter).
2. **TF-IDF:** frequência mínima de documento (`min_df`) escolhida pelo método do cotovelo, que reduziu o vocabulário de mais de 110 mil termos para cerca de 2.600 (`min_df = 100`). Também usamos frequência máxima de 15% e stopwords extras específicas do dataset.
3. **Redução de dimensionalidade:** Truncated SVD (LSA) com 100 componentes, escolhidas pelo joelho dos valores singulares, seguido de normalização L2.
4. **Agrupamento:** K-means (k escolhido por silhueta e inércia) e hierárquico aglomerativo com ligação de Ward (cortes escolhidos pelo dendrograma).
5. **Validação:** termos mais característicos de cada grupo, os 3 gêneros predominantes por grupo e a fração de grupos dominados por um único gênero.
6. **Embeddings (extra):** `all-MiniLM-L6-v2` aplicado às descrições originais, sem pré-processamento, já que o modelo entende contexto e palavras como "não" e "sem" mudam o sentido.

## Classificação por similaridade (extra)

Também testamos classificar cada livro comparando o embedding da descrição com o embedding do nome de 12 gêneros, por similaridade de cosseno. Atribuindo a cada livro o mesmo número de gêneros que ele tem de verdade, a precisão média (micro) ficou em 0,47. Os melhores casos foram ficção literária (F1 0,72) e romance (F1 0,59). Os detalhes por gênero estão no notebook.

## Dados

[`goodreads_books.csv`](goodreads_books.csv): 25 mil livros amostrados de um dataset público do Goodreads, com título, autor, descrição e gêneros (um livro pode ter vários, separados por `|`). O enunciado completo está em [`roteiro.md`](roteiro.md).

## Tecnologias

Python · Pandas · NumPy · scikit-learn (TF-IDF, TruncatedSVD, KMeans, AgglomerativeClustering) · SciPy · NLTK · langdetect · Sentence Transformers · Matplotlib

## Como rodar

```bash
pip install pandas numpy scikit-learn scipy nltk langdetect sentence-transformers matplotlib jupyter
jupyter notebook main.ipynb
```

## Autores

Filipe de Barros Carneiro Silva · Heitor Pinheiro Sousa · João Vitor Toneto Machado

Repositório original: [heitorps/CD_TP](https://github.com/heitorps/CD_TP)
