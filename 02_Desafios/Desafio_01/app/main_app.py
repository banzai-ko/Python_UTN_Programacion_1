from funciones_utn import (
    mostrar_menu,
    play_sound,
    limpiar_pantalla


)
from validaciones import (
    validar_opcion
)
from funciones_utn import (
    utn_mostrar_nombres_heroes,
    utn_mostrar_identidades_heroes,
    utn_mostrar_heroe_mayor_altura
)

def utn_heroes_app(lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos):

    while True:
        mostrar_menu()
        opcion = validar_opcion(1, 10)
        play_sound()
        match opcion:
            case 1:
                utn_mostrar_nombres_heroes(lista_nombres)
            case 2:
                utn_mostrar_identidades_heroes(lista_identidades)    
            case 3:
                utn_mostrar_heroe_mayor_altura(lista_alturas, lista_nombres)
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                print("Saliendo...")
                break
            case _:
                print('Opcion no valida')

        limpiar_pantalla()
