## Integrantes do Grupo:
Beatriz Turi Pinto de Araujo: 202203795211
Lucas Fernandes Mosqueira: 202203369016
Lucas José Silva Serejo: 202202714356
Pedro Henrique Rossetto Costa: 202108581259

## Professor
Cassius Figueiredo

## Curso
Engenharia da Computação 

## Matéria
Complexidade de Algoritimos 

## Instrução de compilação
Para poder rodar o código, é preciso fazer o pip install das bibliotecas abaixo:

 ```python
 pip install flask
 ```

  ```python
 pip install collections
 ```
Para a aplicação funcionar é preciso que você insira apenas uma vez cada tipo de grafo (direcionado ou não direcionado). Se quiser inserir outro grafo, reinicie o app.

## Exemplo Grafo Não Direcionado com uma componente desconexa:

No campo de inserir grafo: 

  ```python
 [("A", "B"), ("A", "E"), ("B", "C"), ("B", "E"), ("C", "F"), ("E", "F"), ("F", "I")]
 ```

No campo de inserir componente desconexa: 

  ```python
 [("D", "H"), ("D", "G"), ("G", "H")]
 ```
Obs: Colocar no campo de quantidade: 1

## Exemplo Grafo Direcionado:

No campo de inserir grafo: 

  ```python
 [("A", "B"), ("A", "F"), ("B", "C"), ("B", "E"), ("C", "D"), ("E", "D"), ("E", "G"), ("D", "H"), ("D", "B"), ("G", "F"), ("H", "G"), ("F", "G"), ("F", "E")]
 ```

## Padrão de Commit
Utilizamos tipos de commit para padronizar as mensagens de commit neste projeto. A seguir, estão os tipos de commit a serem utilizados, juntamente com exemplos de sumários correspondentes:

## ADD
Use o tipo "ADD" quando estiver adicionando um novo recurso ou funcionalidade ao código.

Exemplo:

"Adiciona funcionalidade de autenticação de usuário"

## DROP
O tipo "DROP" é usado para indicar a remoção de um recurso ou funcionalidade do código.

Exemplo:

"Remove o módulo de gráficos legados"

## FIX
Utilize "FIX" ao realizar correções de bugs e resolver problemas.

Exemplo:

"Corrige o erro de formatação na página de perfil do usuário"

## REFACTOR
Use "REFACTOR" quando estiver realizando refatorações no código, melhorando sua estrutura ou desempenho sem alterar sua funcionalidade.

Exemplo:

"Refatora a classe de manipulação de dados para melhorar a legibilidade"

## DOCS
O tipo "DOCS" é aplicado a alterações relacionadas à documentação, como adição ou atualização de comentários no código ou no README.

Exemplo:

"Adiciona documentação de código para o método de autenticação"