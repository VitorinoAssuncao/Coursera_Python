def insertion_sort(lista):
    for x in range(1,len(lista)):
        valor = lista[x]
        i = x -1

        while i >= 0 and valor <= lista[i]:
            lista[i+1] = lista[i]
            i -= 1

        lista[i+1] = valor
    return lista