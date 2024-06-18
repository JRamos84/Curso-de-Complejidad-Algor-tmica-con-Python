import random

def busqueda_linea(lista, objetivo):
    match = False
    for elemeneto in lista: # O(n)
        if elemeneto == objetivo:
            match = True
            break
    return match

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño sera la lista?: '))
    objectivo = int(input('Qué número quieres encontrar?: '))
    
    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    encontrado = busqueda_linea(lista,objectivo )
    print(lista)
    print(f'El elemento {objectivo} {"Esta" if encontrado else "no esta"}')