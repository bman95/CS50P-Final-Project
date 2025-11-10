import random
import time

# Secuencias de escape ANSI para imprimir texto con colores
RESET = "\033[0m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CIAN = "\033[36m"
BLANCO = "\033[37m"


def main():
    # Mensaje de introducción del juego
    print(
        f"""
    {MAGENTA}"Coin Grab" es un juego de lógica desarrollado en Python sin interfaz gráfica. Dos jugadores compiten por no
    tomar la última moneda. Se inicia con una cantidad fija de monedas, normalmente 15. En cada turno se pueden tomar
    de una a tres monedas. La persona que toma la última moneda pierde. Pon a prueba tu estrategia para no quedarte
    con la moneda final.

    Esta vez jugarás contra la máquina.
    ¿Podrás ganarle?
    """
    )

    while True:
        monedas = pedir_monedas_iniciales()
        if monedas is None:
            return

        juego_monedas(monedas)

        if not preguntar_reintento():
            print(f"{AMARILLO}Gracias por jugar Coin Grab. ¡Hasta la próxima!{RESET}")
            break


def pedir_monedas_iniciales():
    # Solicitar la cantidad inicial de monedas
    while True:
        try:
            monedas = int(
                input(
                    f"{MAGENTA}¿Con cuántas monedas quieres iniciar el juego? {RESET}"
                )
            )
            if 0 < monedas < 1000:
                return monedas
            print(f"{ROJO}Ingresa un número positivo menor a 1000.")
        except ValueError:
            print(f"{ROJO}Entrada inválida. Ingresa un número válido.")
        except KeyboardInterrupt:
            print(f"\n{AMARILLO}Juego interrumpido por el usuario. Saliendo...{RESET}")
            return None


def jugador_toma_monedas():
    # Validar la cantidad de monedas que toma la persona
    while True:
        try:
            monedas = int(input(f"{VERDE}¿Cuántas monedas tomas? (1-3): {RESET}"))
            return tomar_monedas(monedas)
        except ValueError:
            print(f"{ROJO}Entrada inválida. Ingresa un número entre 1 y 3.\n")
        except KeyboardInterrupt:
            print(f"\n{AMARILLO}Juego interrumpido. Saliendo...{RESET}")
            exit()


def tomar_monedas(monedas):
    # Verificar que la cantidad esté en el rango permitido
    if 1 <= monedas <= 3:
        return monedas
    raise ValueError


def maquina_toma_monedas(monedas):
    # Simular que la máquina está pensando
    print(f"{CIAN}La máquina está pensando", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(RESET)

    algoritmo = (monedas - 1) % 4
    seleccion = algoritmo or random.randint(1, 3)
    print(f"{CIAN}La máquina toma {seleccion} monedas.")
    return seleccion


def situacion_ganadora(jugador_actual):
    # Determinar quién perdió
    if jugador_actual == 2:
        return f"\n{ROJO}PIERDES. Tomaste la última moneda.{RESET}\n"
    return f"\n{VERDE}GANAS. La máquina tomó la última moneda.{RESET}\n"


def juego_monedas(monedas):
    # Decidir quién inicia el juego
    print(f"{AMARILLO}\nDeterminando quién inicia", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("")

    jugador_actual = random.choice([1, 2])
    if jugador_actual == 1:
        print(f"{VERDE}TÚ comienzas.")
    else:
        print(f"{CIAN}La máquina comienza.")

    # Bucle principal del juego
    while monedas > 0:
        print(f"\n{BLANCO}Monedas restantes: {monedas}")

        if jugador_actual == 1:
            tomadas = jugador_toma_monedas()
        else:
            tomadas = maquina_toma_monedas(monedas)

        monedas -= tomadas
        jugador_actual = 3 - jugador_actual

    print(f"\n{BLANCO}Monedas restantes: 0")
    print(situacion_ganadora(jugador_actual))


def preguntar_reintento():
    # Preguntar si se desea jugar otra vez
    while True:
        try:
            respuesta = (
                input(f"{MAGENTA}¿Quieres jugar de nuevo? (s/n): {RESET}")
                .strip()
                .lower()
            )
        except KeyboardInterrupt:
            print(f"\n{AMARILLO}Entrada interrumpida. Cerrando el juego.{RESET}")
            return False

        if respuesta in ("s", "si"):
            return True
        if respuesta in ("n", "no"):
            return False

        print(f"{ROJO}Respuesta inválida. Escribe 's' o 'n'.{RESET}")


if __name__ == "__main__":
    main()
