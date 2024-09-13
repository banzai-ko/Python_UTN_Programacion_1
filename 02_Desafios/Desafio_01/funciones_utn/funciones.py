
#     utn_filtrar_heroes_genero, utn_mostrar_heroe_mayor_altura,
#     utn_mostrar_heroes_mas_fuertes, utn_mostrar_identidades_heroes,
#     utn_mostrar_nombres_heroes, utn_mostrar_heroes_poder_superior_promedio,
#     utn_mostrar_heroes_mas_debiles
def utn_filtrar_heroes_genero():
    pass


def utn_mostrar_heroe_mayor_altura(lista: list, lista_nombres_heroes: list):
    pos = obtener_mayor(lista)
    print(f"El heroe con mayor altura es: {
          lista_nombres_heroes[pos]}, con {lista[pos]}cm de altura")


def utn_mostrar_heroes_mas_fuertes():
    pass


def utn_mostrar_identidades_heroes(lista_identidades: list):
    mostrar_lista(lista_identidades)


def utn_mostrar_nombres_heroes(lista_nombres: list):
    mostrar_lista(lista_nombres)


def utn_mostrar_heroes_poder_superior_promedio():
    pass


def utn_mostrar_heroes_mas_debiles():
    pass


def mostrar_lista(lista):
    for i in range(len(lista)):
        print(lista[i])


def obtener_mayor(lista: list, indice=None):
    if indice is None:
        indice = len(lista) - 1

    if indice == 0:  # Caso Base
        return 0

    indice_mayor = obtener_mayor(lista, indice - 1)  # Caso recursivo

    # Comparar el valor en el índice actual con el valor almacenado
    if lista[indice] > lista[indice_mayor]:
        return indice
    else:
        return indice_mayor
