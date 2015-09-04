# [Página Inicial](http://code.google.com/p/adaptive-device-framework/wiki/PaginaInicial) -> Automata.py #

Este arquivo foi criado para servir de exemplo de utilização do framework.

## Classe A ##

Esta classe representa uma função adaptativa de nome A. Observe que a função execute() foi sobrescrita, adicionando funcionalidades a ela.

Esta função só utiliza a primitiva de adição, sendo que adiciona uma transição do estado '0', para o estado '1', consumindo o símbolo 'b'.

## Classe Automata ##

Uma classe que herda as características da classe Device, sendo que só foi necessário implementar seu construtor. Esta classe possui as características de um autômato adaptativo finito.

## Definindo o Autômato ##

Para iniciar, é necessário invocar o construtor, passando como argumento o estado inicial do autômato.

Em seguida, são adicionadas as transições subjacentes que pertencem a esse autômato. É instanciado também uma variável do tipo A, que representará a função adaptativa.

É então utilizado o método [includeAdaptiveFunction()](http://code.google.com/p/adaptive-device-framework/wiki/Transition), passando como argumento a qual transição a função será adicionada (identificada pelo estado inicial, símbolo e estado de destino), a variável que representa a função adaptativa, e o tipo da função (se é do tipo 'before' ou 'after').

Para executar o autômato, basta invocar o método [processInput()](http://code.google.com/p/adaptive-device-framework/wiki/Device), passando como argumento a cadeia de símbolos a serem processados.