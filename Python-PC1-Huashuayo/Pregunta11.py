def Eliminar_repetidas(lista):  
    Lista_sin_repetidas = list(set(lista))
    return Lista_sin_repetidas
Lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
Lista_sin_repetidas = Eliminar_repetidas(Lista_original)
print("Lista sin duplicados:", Lista_sin_repetidas)