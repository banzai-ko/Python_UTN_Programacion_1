from funciones_utn.auxiliares import (
    calcular_promedio,
    mostrar_lista,
    mostrar_super_heroes,
    obtener_mayor,
    ordenar_ascendente_poder,
    mostrar_todos,
    ordenar_descendente_altura,
    ordenar_poder_usuario
)
#     utn_filtrar_heroes_genero, utn_mostrar_heroe_mayor_altura,
#     utn_mostrar_heroes_mas_fuertes, utn_mostrar_identidades_heroes,
#     utn_mostrar_nombres_heroes, utn_mostrar_heroes_poder_superior_promedio,
#     utn_mostrar_heroes_mas_debiles


def utn_filtrar_heroes_genero(lista_generos: list, lista_heroes: list, genero='Femenino') -> None:
    for i in range(len(lista_generos)):
        if lista_generos[i] == genero:
            print(lista_heroes[i])


def utn_mostrar_heroe_mayor_altura(lista: list, lista_nombres_heroes: list) -> None:
    pos = obtener_mayor(lista)
    print(f'El heroe con mayor altura es: {
          lista_nombres_heroes[pos]}, con {lista[pos]}cm de altura')


def utn_mostrar_identidades_heroes(lista_identidades: list):
    mostrar_lista(lista_identidades)


def utn_mostrar_nombres_heroes(lista_nombres: list):
    mostrar_lista(lista_nombres)


def utn_mostrar_heroes_poder_superior_promedio(lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos):
    promedio = calcular_promedio(lista_poderes)
    for i in range(len(lista_poderes)):
        if lista_poderes[i] > promedio:
            print(mostrar_super_heroes(i, lista_nombres, lista_identidades,
                  lista_alturas, lista_poderes, lista_generos))

def utn_mostrar_heroes_mas_debiles(lista: list[list]):
    pass


def utn_mostrar_heroes_mas_fuertes():
    pass


def utn_mostrar_heroes_poder_ascendente(lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos):
    lista_ordenada = ordenar_ascendente_poder(
        lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos)
    mostrar_todos(lista_ordenada)


def utn_mostrar_heroes_altura_descendente(lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos):
    lista_mas_grandes = [[], [], [], [], []]
    lista_mas_chicos = [[], [], [], [], []]
    lista_ordenada = ordenar_descendente_altura(
        [lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos], lista_mas_grandes, lista_mas_chicos)
    mostrar_todos(lista_ordenada)

def utn_mostrar_heroes_poder_usuario(lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos):
    seleccion_usuario = input('Ingrese ASC o DES: ')
    while seleccion_usuario != 'ASC' and seleccion_usuario != 'DES':
        seleccion_usuario = input('Ingrese ASC o DES: ') #mejorar en funcion de validacion

    lista_ordenada = ordenar_poder_usuario(
        lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos, seleccion_usuario
    )    
    mostrar_todos(lista_ordenada)
    pass
