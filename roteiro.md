# Trabalho Prático

O objetivo geral deste trabalho é praticar os conceitos discutidos em sala de aula, principalmente: representação e pré-processamento de dados textuais; redução de dimensionalidade e algoritmos de agrupamento.

## Conjunto de Dados

Para este trabalho utilizaremos um conjunto de dados de livros do Goodreads, disponibilizado publicamente para pesquisa em mineração de texto e sistemas de recomendação. O arquivo `goodreads_books.csv` contém dados de 25000 livros amostrados de um dataset público. As colunas presentes são:

* **book_id:** identificador único do livro no Goodreads;
* **title:** título do livro;
* **author:** nome do autor principal;
* **description:** sinopse/descrição textual do livro;
* **genre:** gênero(s) do livro, podendo conter múltiplos valores separados por | (ex: fantasy|romance);
* **publication_year:** ano de publicação
* **average_rating:** média das avaliações dos leitores, escala de 0 a 5;
* **ratings_count:** número total de avaliações recebidas;
* **num_pages:** número de páginas do livro;

**ATENÇÃO**
É possível que seu computador não consiga lidar com o conjunto de dados completo. Se for o caso, faça uma amostra aleatória de livros do conjunto de dados. Deixe claro o processo de amostragem, o tamanho das amostras finais que considerou no trabalho e as especificações do computador utilizado.

Os dados para o trabalho estão disponíveis no AVA da disciplina, Tópico "Trabalho Prático".

## Objetivo

Vocês deverão utilizar aprendizado não supervisionado (neste caso, agrupamento) para investigar se há relação entre a **descrição** de um livro e o(s) **gênero(s)** ao(s) qual(quais) ele pertence.

Mais especificamente, o objetivo é agrupar livros a partir da similaridade entre suas descrições e, posteriormente, verificar se os gêneros se distribuem de maneira distinta entre os grupos encontrados.

## Metodologia

Para atingir o objetivo proposto, vocês deverão seguir ao menos os seguintes passos:

1. Pré-processamento dos dados textuais;
2. Construção da matriz de TF-IDF;
3. Redução de dimensionalidade, via PCA (Leia também sobre o *Truncated SVD*: https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html);
4. Aplicação de ao menos dois algoritmos de agrupamento vistos na disciplina;
5. Validação da metodologia utilizada;
6. Interpretação dos resultados.

**PS:** essas são as exigências mínimas. Caso vocês queiram fazer/propor algo extra, será permitido (e pode ajudar na nota se a proposta for relevante).

### Abordagem com LLM (Extra)

O intuito dessa etapa é explorar o uso de [Modelos de Linguagem](https://arxiv.org/abs/1706.03762) para representar as descrições dos livros a partir de [embeddings](https://www.ibm.com/br-pt/think/topics/embedding), capazes de capturar relações semânticas dos textos, ao invés da tradicional abordagem baseada em TF-IDF, focada na frequência dos termos.

**Importante**: Essa etapa é opcional e valerá até 1 ponto (de 10) extra na nota final do trabalho.

Passos sugeridos:

1. Escolha um modelo pequeno da biblioteca [`SentenceTransformers`](https://www.sbert.net/) (eg. `all-MiniLM-L6-v2`, `paraphrase-MiniLM-L6-v2`)
2. Gere embeddings para as descrições dos livros
3. **Importante**: Avalie se a estratégia de agrupamento precisa ser alterada quando usando embeddings ao invés de TF-IDF. Se sim, tente entender e justificar o porquê.
4. **Agrupamento**: Aplique ao menos um algoritmo de agrupamento (pode ser diferente dos vistos em aula)
5. **Classificação por Similaridade**: Implemente uma abordagem alternativa usando similaridade de cosseno:
   - Gere embeddings para os rótulos (gêneros) disponíveis
   - Para cada livro, calcule a similaridade de cosseno entre o embedding da descrição e os embeddings dos gêneros
   - Atribua cada livro ao(s) gênero(s) mais similar(es)
   - Compare os resultados com os gêneros reais dos livros

**Análise Comparativa**: Compare os resultados obtidos com sentence embeddings versus TF-IDF. Qual abordagem gerou agrupamentos mais coerentes com os gêneros reais?

## Resultados esperados

Dois tipo de resultados são esperados: validação e análise.

### Resultados de validação

O trabalho deve conter resultados mostrando que os algoritmos (e respectivos parâmetros) foram escolhidos e utilizados de forma correta. Entre os pontos importantes:
1. Como foi escolhido o número de componentes principais para o PCA? O número de componentes principais tem um impacto significativo nos resultados? É necessário usar PCA neste trabalho?
2. Como o número de grupos para cada algoritmo de agrupamento foi definido? A escolha do algoritmo de agrupamento impacta significativamente os resultados? E o número de grupos?

Fará parte da avaliação a forma que escolherem para validar a metodologia. Vocês podem recorrer a visualizações interessantes, medidas internas...

### Análise

Após validar e entender os resultados (e se convencerem que estão corretos e fazem sentido), você deve responder as perguntas principais:
- Há diferença nas distribuições de gêneros dos livros em grupos diferentes?
- Há relação entre as descrições dos livros e os respectivos gêneros?
- Diferentes algoritmos de agrupamento produzem resultados semelhantes?

- **Opcional, pontuação extra:** se, além das descrições, você também considerar as demais informações no conjunto de dados para os algoritmos de agrupamento, é possível encontrar uma melhor associação entre os grupos e os gêneros dos livros?


Novamente, recorra às ferramentas que já vimos no curso para responder essa pergunta: visualizações, medidas externas... **soluções que tiverem achados interessantes nessa parte do trabalho ganharão ponto extra**.


## Observações importantes

1. Durante a fase de agrupamento, apenas a informação da descrição deve ser utilizada. A informação de **gênero dos livros** deve ser usada apenas após a fase de agrupamento para validar e analisar os resultados.
2. Vocês podem usar todas as bibliotecas Python que venho mostrando em aula. Caso queiram usar algo muito diferente (por exemplo, alguma biblioteca de uso comercial), perguntem ao professor antes (em nosso fórum do AVA).
3. Vocês serão avaliados pela:
  - Qualidade dos resultados quantitativos;
  - Escolha e condução da metodologia;
  - Uso de visualizações informativas e bem feitas;
  - Explicação dos passos seguidos e das decisões tomadas;
  - Justificativas para as decisões tomadas;
  - Análise dos resultados;
  - Conclusões.
4. Qualquer colaboração, entre grupos ou de fontes externas, deve ser citada e mencionada no trabalho. **NÃO HAVERÁ TOLERÂNCIA PARA COLABORAÇÕES INDEVIDAS!**

## Grupos

- **Graduação:** até 3 pessoas
- **Pós-graduação:** individual

## Entrega

- **Linguagem de programação:** Python
- **O que entregar:** um *Jupyter Notebook*, contendo texto, código e resultados. Deve ser possível que o professor execute o seu código, mas o arquivo ``.ipynb`` submetido já deve conter todos os resultados (i.e., deve ser possível corrigir seu trabalho apenas abrindo o arquivo). Apenas um integrante do grupo deve fazer a submissão no AVA. Lembrem-se de colocar a informação de todos os integrantes do grupo (nome, matrícula e e-mail).

## Dúvidas?

Postem em nosso fórum do AVA!