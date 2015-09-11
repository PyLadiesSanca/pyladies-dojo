# coding: utf-8
"""
    Fazer o primeiro LED do display piscar
    Fazer os n LEDs piscarem
    Criar uma lista que represente todos os pinos    
    Fazer os LEDs acenderem 
    Fazer os LEDs acenderem na sequência
    Fazer os LEDs acenderem E apagarem na sequencia
    Fazer a sequencia dos LEDs repetir
"""

import pingo
import time

board = pingo.detect.get_board()

pins_pos = [15, 13, 22,18,16,12]

lista = [board.pins[pin] for pin in pins_pos]

for pin in lista:
   pin.mode = pingo.OUT

while True:
   for pin in lista:
      pin.hi()
      time.sleep(0.5)
      pin.lo()

board.cleanup()
