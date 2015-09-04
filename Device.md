# [Página Inicial](http://code.google.com/p/adaptive-device-framework/wiki/PaginaInicial) -> Device.py #

Este arquivo contém duas classes, a Device e a AdaptiveDevice.


## Device ##

Esta classe representa o dispositivo subjacente. Possui dois atributos, uma lista contendo todas suas transições e uma variável indicando seu estado atual. Nesta verão do projeto, não decidiu-se por não se utilizar explicitamente uma lista de estados, sendo que estes estão contidos implicitamente nas [transições](http://code.google.com/p/adaptive-device-framework/wiki/Transition).

Esta classe pode representar qualquer dispositivo computacional. Para alterar seu funcianamento atual, basta criar uma especialização desta classe, sobrescrevendo qualquer um dos métodos que se deseje alterar.

### Realize() ###

Este método executa a transição que estiver habilitada no momento, sendo que uma transição é considerada habilitada quando o estado atual e o símbolo sendo lido no momento correspondem aos respectivos atributos da transição.

### ProcessInput() ###

Este método recebe uma cadeia de símbolos e os processa sequencialmene, atualizando o estado  atual do dispositivo conforme cada transição é executada.

## AdaptiveDevice ##

Uma especialização da classe Device, onde o atributo que contém as transições é alterado para permitir que as transições possam conter ações adaptativas associadas a elas.