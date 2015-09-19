# Dojo 18/09/2015
Nesse dojo continuamos a mexer no display de LED de 7 segmentos.
Implementamos duas versões de uma "cobra" (dois LEDs contínuos do display ligados ao mesmo tempo).

## Cobra aleatória:
Ela "percorre" todos os LEDs de forma aleatória. O código está no arquivo cobra_aleatoria.py

## Cobra indecisa:
Quando a cobra alcança uma bifurcação (onde existe dois caminhos possíveis para seguir) a cobra para e fica aguardando que um dos dois botões do circuito sejam apertados. Quando o primeiro botão é apertado a cobra opta pelo primeiro caminho, já quando o segundo botão é apertado a cobra segue para o segundo.
