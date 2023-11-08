# -*- coding: utf-8 -*-
from math import sqrt


def primo(n):
    '''(int) -> bool

       Recebe um número inteiro n e retorna True se n é primo.
       Em caso contrário a função retorna False.
    '''
    for i in range(2,round(sqrt(n))+1):
        if(n%i==0):
            return False
    return True
    
    
def goldbach(n):
    '''(int) -> bool, int, int 

       Recebe um número inteiro n e retorna True se n pode
       ser escrito como a soma de dois nḿeros primos. 
       Nesse caso a função deve retornar dois números primos
       p e q tais que p + q == n.

       Em caso contrário a função retorna False, 0, 0.
    '''
    if(n<0):
        return False,0,0
    list = [*range(n)]

    primos_menores_que_n = [i for i in list if primo(i)]

    for i in primos_menores_que_n:
        for j in reversed(primos_menores_que_n):
            print(f"{i} + {j} == {i+j}")
            if(i+j>n):
                print(f"{i} + {j} == {i+j}")
                break
            elif(i+j == n):
                return True,i,j
    return False,0,0
    

def inverte(n):
    '''(int) -> int

        Recebe um número inteiro n e retorna um número inteiro 
        com os algarismos invertidos de n. Ex:
                entrada: 12345
                saída: 54321     
    '''
    return int(str(n)[::-1])
    
     
    
def fatorial(n): 
    '''(int) -> int
        Recebe um inteiro >= 0 e retorna o fatorial desse
        número 
    
    '''
    if(n==1):
        return 1
    else:
        return n * fatorial(n-1)    

    #escreva aqui 
def ocorrencia(lista):
    '''(list) -> None
        Recebe uma lista de tamanho m de inteiros 0 <= n <= 9 aleatórios e imprime
        a ocorrência de cada um deles. Ex:
        lista = [0,5,4,2,8,4,7,8,4,5,6,6,6,3]
        0 : 1
        1 : 0
        2 : 1
        3 : 1
        4 : 3
        5 : 2
        6 : 3 
        7 : 1
        8 : 2
        9 : 0
    '''

    dict = {}
    for i in lista:
        if(dict.get(i)==None):
            dict[i] = 1
        else: 
            dict[i] += 1
    print(dict)    
    
ocorrencia([0,5,4,2,8,4,7,8,4,5,6,6,6,3])        
print(goldbach(12))