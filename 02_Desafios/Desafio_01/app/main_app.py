from funciones_utn import (
    mostrar_menu,
    play_sound,
    limpiar_pantalla


)
from validaciones import (
    validar_opcion
)


def utn_heroes_app(lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos):

    while True:
        mostrar_menu()
        opcion = validar_opcion(1, 10)
        play_sound()
        match opcion:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
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
