
def generar_palabra(diff, fac, dif):
    import random
    if diff == 0:
        palabra = random.sample(fac, k=1)
    else:
        palabra = random.sample(dif, k=1)
    return palabra[0]

def clear():
    from os import system, name    
    if name == 'nt': # for Windows
        _ = system('cls')
    else:   # for mac and linux(here, os.name is 'posix')
        _ = system('clear')

def esperar_tiempo(nivel):
    import time
    if nivel == 0:
        time.sleep(1.5)
    if nivel == 1:
        time.sleep(1)
    if nivel == 2:
        time.sleep(0.9)

def run():
    words = []
    facil = []
    dificil = []
    dificultad = 0
    tiempo = 0
    exitos = 0
    strike = 0

    with open('./words.txt', 'r', encoding='utf-8') as f: # Apertura del archivo de texto en modo de solo lectura
        for line in f: # Se va a leer cada linea por separado
            if len(line.strip()) > 5 and len(line.strip()) <10: # Se comprueba la longitud del string agregarlo a las lista dificil
                dificil.append(line.strip()) # Se agrega cada linea sin espacios o saltos de linea a la lista dificil
            if len(line.strip()) > 3 and len(line.strip()) <= 5:# Se comprueba la longitud del string agregarlo a las lista facil
                facil.append(line.strip()) # Se agrega cada linea sin espacios o saltos de linea a la lista facil

    while strike < 3:
        palabra_escogida = generar_palabra(dificultad, facil, dificil)
        print(palabra_escogida)
        esperar_tiempo(tiempo)
        # clear()
        palabra_ingresada = input("Ingrese la palabra\n")
        if palabra_ingresada == palabra_escogida:
            print("Palabra correcta, Felicidades \n")
            exitos = exitos + 1
            print("has ganado ", exitos, " Veces \n")
            print("Estas en el nivel \n", dificultad, "\nCon un tiempo para ver la palabra de \n", tiempo)
            if exitos == 2:
                dificultad = 1
                tiempo = tiempo + 1
            if exitos >= 4:
                palabra2 = generar_palabra(dificultad, facil, dificil)
                print(palabra_escogida, palabra2)
                esperar_tiempo(tiempo)
                # clear()
                palabra_ingresada2 = input("Ingrese la palabra 2\n")
                if palabra_ingresada2 == palabra2:
                    print("Palabra 2 correcta, Felicidades \n")

        else:
            print("Palabra Errada")
            if dificultad == 0:
                strike = strike + 1
                print("Llevas ", strike, " Strikes")
            else:
                tiempo = tiempo - 1
                strike = strike + 1


if __name__ == '__main__':
    run()