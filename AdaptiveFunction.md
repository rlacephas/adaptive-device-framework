# [Página Inicial](http://code.google.com/p/adaptive-device-framework/wiki/PaginaInicial) -> AdaptiveFunction.py #

Este arquivo contém uma classe abstrata que representa as funções adaptativas que serão utilizadas pelo dispositivo sendo implementado pelo usuário. Cada função adaptativa deverá , então, ser uma especialização desta classe, onde o nome desta nova classe deve corresponder ao nome da função adaptativa.

Esta foi projeta para ser uma função adaptativa genérica, sendo que as funções adaptativas que serão utilizadas devem ser especializaçõe desta classe, especificamente implementando o método execute().

A função execute() será chamada toda vez que a transição associada a função adaptativa for utilizada. Esta função, portanto, deve conter todas as ações que a função deve executar. Nesta classe já esta implementada 2 das primitivas necessárias para o funcionamento dos dispositivos.

A classe possui as seguintes funções

## PlusPrimitive() ##

É a primitiva de adição.

Adiciona transições ao dispositivo adaptativo. Deve receber como argumentos o estado de origem, o símbolo que será consumido, o estado de destino e a lista que contém todas as transições atuais do dispositivo.



## MinusPrimitive() ##

A primitiva de remoção

Remove uma transição do dispositivo adaptativo. Os parâmetros que deve receber são os mesmo da primitiva de adição

## QuestionPrimitive() ##

A primitiva de busca.

Esta função deve receber uma lista de parâmetros, correpondentes a lista de variáveis da função adaptativa.

**Ainda não implementada nesta versão**

## Execute() ##

Função abstrata que deve ser implementada, sendo que seu corpo deve conter as primitivas que compõe a função adaptativa que será executada.