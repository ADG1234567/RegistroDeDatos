def entradadeDatos():
    global nombre, edad, dinero, deportista, deporte, color, favorito, casa, house, estatura, bird, food, celular, celu
    nombre = input("Cómo te llamas? ").title()
    while True: # lee la edad
        try:
            edad = int(input("Cuántos años tienes? "))
            break
        except:
            print('La "edad" es un valor entero.Intentalo de nuevo. \n ')
            continue
    dinero = float(input("Cuánto dinero tienes? "))
    deportista = input("Te gusta el deporte: ")
    if deportista in {"s","si","y","yes"}:
        deporte = input("Cuál es tu deporte favorito? ")
    color = input("Tienes un color favorito?: ")
    if color in {"s","si","y","yes"}:
        favorito = input("Cuál es tu color favorito?: ")
    casa = input("Tienes una casa?: ")
    if casa in {"s","si","y","yes"}:
        house = input("Dónde vives?: ")
    estatura = input("Cuánto mides?: ")
    bird = input("Cuándo naciste? ")
    food = input("Cuál es tu comida favorita? ")
    celular = input("Tienes un ceular? ")
    if celular in {"s","si","y","yes"}:
        celu = input("De qué marca es tu celular? ").title()


def salidadeDatos():
    global nombre, edad, dinero, deportista, deporte, color, favorito, casa, house, estatura, bird, food, celular, celu
    print("""Hola {}
    Espero que estes bien
    Hoy es un dia nublado, tu edad es {} años,
    Hoy tienes {} pesos
    Mides {} m
    Naciste el {}
    Te gusta comer {}""".format(nombre,edad,dinero,estatura,bird,food))
    if celular in {"s","si","y","yes"}:
        print("Tu celular es marca {}".format(celu))
    if deportista in {"s","si","y","yes"}:
        print("Te gusta el deporte {}".format(deporte))
    if color in {"s","si","y","yes"}:
        print("Tu color favorito es {}".format(favorito))
    if casa in {"s","si","y","yes"}:
        print("Vives en {}".format(house))

# programa principal ( main )
while True:
    entradadeDatos()
    salidadeDatos()
    respuesta = input ("Otra ronda? [si o no]: ").lower()
    if respuesta not in {'s,si,y,yes'}:
        break