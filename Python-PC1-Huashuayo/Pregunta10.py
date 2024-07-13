lista_colores = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
posicion = [0,4,5]
posicion_eliminar = [lista_colores[i] for i in posicion]
for valor in posicion_eliminar:
    lista_colores.remove(valor)
print(lista_colores)