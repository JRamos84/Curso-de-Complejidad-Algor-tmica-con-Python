import time
import sys
sys.setrecursionlimit(200001)

"""_summary_
Lo interesante aquí es que medir el tiempo en que toma correr dos algoritmo diferentes pero queentregan el mismo resultado no es 
muy eficiente, ya que depende de factores extrernos, como el tipo de cpu, ram, los procesos que esten activos en ese momento, etc.
por lo que no es muy eficiente este tipo de medición
"""

def factorial(n):
    respuesta = 1
    while n > 1:
        respuesta *=n
        n -=1
    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial_r(n-1)

if __name__ == '__main__':
    n=200000
    
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)
    
    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)
    
    
    