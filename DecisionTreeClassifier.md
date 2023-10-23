## Treinamento de um Modelo de Árvore de Decisão com Scikit-Learn

Este código Python ilustra o processo de treinamento de um modelo de Árvore de Decisão usando a biblioteca Scikit-Learn. O exemplo inclui o tratamento de dados, a divisão dos dados em conjuntos de treinamento e teste, o uso da técnica SMOTE para lidar com classes desbalanceadas e a avaliação do modelo usando métricas como Matriz de Confusão, Acurácia, Precisão e Recall.

### Bibliotecas Utilizadas

- `pandas`: Para manipulação de dados.
- `imblearn.over_sampling.SMOTE`: Para balanceamento de classes.
- `sklearn.tree.DecisionTreeClassifier`: Para criar o modelo de Árvore de Decisão.
- `sklearn.model_selection.train_test_split`: Para dividir os dados em conjuntos de treinamento e teste.
- `sklearn.metrics`: Para calcular métricas de avaliação.

### Classes e Funções

- `ColetaDados`: Uma classe para coletar dados a partir de um arquivo CSV.

  - `__init__(self, csv_path)`: O construtor recebe o caminho para o arquivo CSV.
  - `coletar_dados(self)`: Uma função que lê o arquivo CSV e retorna um DataFrame com os dados.
- `TreinarModelo`: A classe principal para treinar o modelo de Árvore de Decisão.

  - `__init__(self, csv_path)`: O construtor recebe o caminho para o arquivo CSV.
  - `ler_dados(self)`: Uma função que utiliza a classe `ColetaDados` para ler os dados do arquivo.
  - `treinar_bot(self)`: A função principal que realiza o pré-processamento, treinamento e avaliação do modelo.

### Pré-Processamento

1. Os dados são lidos a partir de um arquivo CSV usando a classe `ColetaDados`.
2. As variáveis de entrada (`X`) e a variável alvo (`y`) são definidas.
3. A técnica SMOTE é aplicada para tratar classes desbalanceadas, gerando `X_resampled` e `y_resampled`.
4. Os dados são divididos em conjuntos de treinamento e teste (`X_treino`, `X_teste`, `y_treino`, `y_teste`).

### Treinamento do Modelo

5. Um modelo de Árvore de Decisão é criado usando `DecisionTreeClassifier`.
6. O modelo é treinado com os dados de treinamento.

### Avaliação do Modelo

7. O código imprime a Matriz de Confusão, que mostra como o modelo classificou os dados de teste.
8. A Acurácia do modelo é calculada e impressa.
9. A Precisão e o Recall são calculados para cada classe e impressos.

### Execução

O código é executado com o caminho para o arquivo CSV como argumento. Certifique-se de que as bibliotecas necessárias estejam instaladas antes de executar o código.

### Resultados

O resultado do código é a avaliação do modelo de Árvore de Decisão, incluindo a Matriz de Confusão, Acurácia, Precisão e Recall para cada classe.
