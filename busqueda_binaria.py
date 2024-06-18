import random


def busqueda_binaria(lista,comienzo,final, objetivo):
    if comienzo > final:
        return False
    medio = (comienzo + final) // 2 
    
    if lista[medio] == objectivo:
        return True
    elif lista[medio] < objectivo:
        return busqueda_binaria(medio + 1 , final,objetivo)
    else:
        return busqueda_binaria(lista, comienzo, final - 1 ,objetivo )




if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño sera la lista?: '))
    objectivo = int(input('Qué número quieres encontrar?: '))
    
    lista = sorted([random.randint(0,100) for i in range(tamano_de_lista)])
    
    encontrado =busqueda_binaria(lista, 0, len(lista) ,objectivo)
    
    print(lista)
    print(f'El elemento {objectivo} {"Esta" if encontrado else "no esta"}')