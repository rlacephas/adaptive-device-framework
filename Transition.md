# [Página Inicial](http://code.google.com/p/adaptive-device-framework/wiki/PaginaInicial) -> Transition.py #

Este arquivo contém as classes que implementam as transições de dispositivos, tanto as subjacentes como as adaptativas. Não foi criado uma definição especifica para estados, sendo que estes vão ser implicitamente declarados nas transições.

As transições devem ser descritas da forma (_ei_, _s_, _ed_), onde _ei_ representa o estado de origem, _s_ o símbolo que será consumido, e _ed_ o estado de destino da transição.

Esta classe já fornece métodos que permitem a adição e remoção de transições, conforme o necessário, seja durante a criação do dispositivo, ou durante a execução de uma função adaptativa.

## Classe Transition ##

Esta classe representa as transições subjacentes, sendo que é esta classe que disponibiliza os métodos de adicionar ou remover transições.

### Método addTransition() ###

Recebe como argumentos  o estado de origem, o símbolo a ser consumido, e o estado de destino.

### Método delTransition() ###

Recebe como argumentos o estado origem, o símbolo a ser consumido, e o estado de destino. Se a transição que se deseja remover não existir, nenhuma ação é tomada.

### Método realize() ###

Método recebe como argumentos o estado de origem e o símbolo atual. Este método na versão atual é abstrato, sendo que sua implementação depende do tipo de dispositivo sendo implementado.

## Classe AdaptiveTransition ##

Uma classe especializada de Transition, onde o método realize() é sobrescrito, onde durante a execução de uma transição é verificado se existe alguma função adaptativa associada, chamando-a se existir.

Esta classe possui outro método, que permite que o usuário adicione uma função adaptativa a alguma transição já existente.

### Método includeAdaptiveFunction ###

Recebe como argumento o estado de origem, o símbolo consumido, o estado de destino, a função adaptativa e o tipo dela ('before'/'after').

Se a descrita pelo parâmetros não existir, nenhuma ação é tomada.