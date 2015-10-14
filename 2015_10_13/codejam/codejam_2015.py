'''
    >>> NumberOfFiles()
    4
    >>> MaxDistance()
    2
    >>> print(identifiers)
    [1000, 1500, 0, 500]
    >>> print(identifiers_ordenados)
    [0, 500, 1000, 1500]
    >>> checksum(identifiers_ordenados)
    7000
'''

''' 
                    Arquivos para serem ordenados
    Um arquivo que deveria estar na posicao i esta entre i - k e i + k
    ou seja, esta distante k posicoes da sua posicao original
    
    Cada arquivo tem um identificador, e os arquivos devem ser ordenados
    pelo identificador, ou seja, um arquivo com identificador maior vem
    depois de um arquivo com identificador menor. Para verificar se
    os arquivos estao ordenados, nos multiplicamos o identificador do
    arquivo pela sua posicao e no final somamos todos os valores
    resultantes, e depois aplicando o mod 2²⁰.
    
    OBJETIVO: O programa deve calcular o valor de verificacao (checksum)
    
    INPUT: Um arquivo que define 3 métodos:
        NumberOfFiles()
        MaxDistance()
        Identifier(i) -> Identifier(1) :- 2000000
        
    OUTPUT: O valor do checksum dos arquivos ordenados
'''

from almost_sorted import NumberOfFiles, MaxDistance, Identifier

identifiers = [Identifier(indice) for indice in range(NumberOfFiles())]

identifiers_ordenados = sorted(identifiers)

def checksum(lista):
    soma = 0
    for indice, identificador in enumerate(lista):
        soma += indice * identificador 
        
    soma = soma % (2**20)
    return soma
    
print checksum(identifiers_ordenados)

