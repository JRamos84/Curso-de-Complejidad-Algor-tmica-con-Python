import random

def busqueda_linea(lista, objetivo):
    match = False
    count = 0
    for elemeneto in lista: # O(n)
        count +=1
        if elemeneto == objetivo:
            match = True
            print(f'n: {count}' )
            break
    return match

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño sera la lista?: '))
    objectivo = int(input('Qué número quieres encontrar?: '))
    
    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    encontrado = busqueda_linea(lista,objectivo )
    print(lista)
    print(f'El elemento {objectivo} {"Esta" if encontrado else "no esta"}')