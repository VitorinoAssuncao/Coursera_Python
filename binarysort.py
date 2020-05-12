import time

def busca(lista,elemento):
    first = 0
    max_position = len(lista) -1

    while first <= max_position:
        mid =  (first + max_position) // 2
        print(mid)
        if lista[mid] == elemento:
            return mid
        else:
            if elemento < lista[mid] :
                max_position = mid -1 
            else:
                first = mid + 1    
    return False