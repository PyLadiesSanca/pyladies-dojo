''' 
    
    >>> tempo_nova_bola(2, 20, [3, 2])
    'impossivel'
    >>> fatora(12)
    [1, 2, 3, 4, 6, 12]
    >>> tempo_nova_bola(4, 6, [1, 2, 3, 6])
    'impossivel'
    >>> tempo_nova_bola(2, 12, [2, 4])
    3
'''

'''
    >>> print(bolas, tempo)
    2 12
    https://www.urionlinejudge.com.br/judge/pt/problems/view/1909
'''

def tempo_nova_bola(bolas, tempo, tempos_bolas):
    fatores = fatora(tempo)
    if tempos_bolas == fatores:
        return 'impossivel'
    
    for tempo_bola in tempos_bolas:
        if tempo_bola not in fatores:
            return 'impossivel'
    
    for tempo_bola in tempos_bolas:
        fatores.remove(tempo_bola)
        
    print(fatores)
    
    return fatores[0] if fatores[0] != 1 else fatores[1]
        
def fatora(numero):
    lista = []
    for divisor in range(1,numero+1):
        if numero % divisor == 0:
            lista.append(divisor)
            
    return lista
        
        
    
bolas, tempo = map(int, input().split(' '))
while (bolas != 0 and tempo != 0):
    tempos_bolas = map(int, input().split(' '))
    print(tempo_nova_bola(bolas, tempo, tempos_bolas))
    bolas, tempo = map(int, input().split(' '))
    
    


