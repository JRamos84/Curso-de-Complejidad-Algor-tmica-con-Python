import random


def busqueda_binaria(lista,comienzo,final, objetivo,n):
    n +=1
    
    print(f'buscando {objetivo}, n_iteraciones: {n}, entre {lista[comienzo]} y {lista[final -1]}')
    
    if comienzo > final:
        return False
    medio = (comienzo + final) // 2 
    
    if lista[medio] == objetivo:

        return True
    elif lista[medio] < objetivo:

        return busqueda_binaria(lista,medio + 1 , final,objetivo,n)
    
    else:

        return busqueda_binaria(lista, comienzo, final - 1 ,objetivo,n )




if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño sera la lista?: '))
    objetivo = int(input('Qué número quieres encontrar?: '))
    
    lista = sorted([random.randint(0,100) for i in range(tamano_de_lista)])
    
    encontrado =busqueda_binaria(lista, 0, len(lista) ,objetivo,n=0)
    
    print(lista)
    print(f'El elemento {objetivo} {"Esta" if encontrado else "no esta"}')