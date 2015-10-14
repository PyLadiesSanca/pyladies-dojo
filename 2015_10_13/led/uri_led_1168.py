""" Problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1168

    >>> print(n)
    3
    >>> numero_leds(115380)
    27
"""

leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
def numero_leds(numero):
    qtd_leds = 0
    for caractere in numero:
        qtd_leds += leds[int(caractere)]
    return qtd_leds
    
    
n = int(input())
for _ in range(n):
    numero = str(input())
    print('{0} leds'.format(numero_leds(numero)))
    
