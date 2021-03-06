# coding: utf-8

"""
    - Mapear os pinos
    - Verificar a ordem dos pinos
    - Movimentacao da cobrinha sóa cabecinha
    - Movimentacao do corpo
    - Abstrair atributos da cobra
    - Criar funcao de acender a cobra
    - Criar funcao de apagar a cobra
    - abstrair leds
    - criar dicionario de caminhos possiveis
    - movimentando a cobra pelo primeiro caminho conhecido
    - movimentar a cobra aleatoriamente pelos caminhos conhecidos
"""

import pingo
import time
import random

board = pingo.detect.get_board()


class Led:
    def __init__(self, seg, pino):
        self.seg = seg
        self.pino = pino


class Python:
    leds = {
        'a': Led('a', board.pins[13]),
        'b': Led('b', board.pins[12]),
        'c': Led('c', board.pins[15]),
        'd': Led('d', board.pins[22]),
        'e': Led('e', board.pins[18]),
        'f': Led('f', board.pins[7]),
        'g': Led('g', board.pins[16])
    }

    for _, led in leds.items():
        led.pino.mode = pingo.OUT
        led.pino.lo()

    def __init__(self, rabo, cabeca):
        self.cabeca = cabeca
        self.rabo = rabo

        self.caminhos = {
            ('a', 'b'): [('b', 'c'), ('b', 'g')],
            ('b', 'c'): [('c', 'd')],
            ('b', 'g'): [('g', 'f'), ('g', 'e')],
            ('c', 'd'): [('d', 'e')],
            ('g', 'f'): [('f', 'a')],
            ('g', 'e'): [('e', 'd')],
            ('d', 'e'): [('e', 'g'), ('e', 'f')],
            ('f', 'a'): [('a', 'b')],
            ('e', 'd'): [('d', 'c')],
            ('e', 'g'): [('g', 'b'), ('g', 'c')],
            ('e', 'f'): [('f', 'a')],
            ('d', 'c'): [('c', 'g'), ('c', 'b')],
            ('g', 'b'): [('b', 'a')],
            ('g', 'c'): [('c', 'd')],
            ('c', 'g'): [('g', 'f'), ('g', 'e')],
            ('c', 'b'): [('b', 'a')],
            ('b', 'a'): [('a', 'f')],
            ('a', 'f'): [('f', 'g'), ('f', 'e')],
            ('f', 'g'): [('g', 'b'), ('g', 'c')],
            ('f', 'e'): [('e', 'd')],
        }

    def acender(self):
        self.cabeca.pino.hi()
        self.rabo.pino.hi()

    def apagar(self):
        self.cabeca.pino.lo()
        self.rabo.pino.lo()

    def andar(self):
        self.apagar()

        caminhos = self.caminhos[(self.rabo.seg, self.cabeca.seg)]
        caminho_escolhido = random.choice(caminhos)
        seg_rabo, seg_cabeca = caminho_escolhido
        self.rabo = self.leds[seg_rabo]
        self.cabeca = self.leds[seg_cabeca]

        self.acender()


botao_1 = board.pins[29]
botao_2 = board.pins[31]
cobra = Python(Python.leds['a'], Python.leds['b'])

cobra.acender()
time.sleep(0.1)
while True:
    cobra.andar()
    time.sleep(0.1)
