import random

print("Bienvenido al programa de LA PORSCHE SUPERCUP")
print("\n")

print("Gracias a la buena vuelta que hicistes en el dia de la quali tu equipo y tu salis en P4. Llevais un Porsche 911 GT3 pero con un motor algo menos potente que los tres pilotos que tienes por delante. \n"
    "La unica opcion para poder quedar en P1 es tomar las mejores decisiones e intentar hacer un undercut en la vuelta exacta a los pilotos que tienes por encima. El circuito en el que corres es en Circuito de Spa-Francorchamps y sales por el lado izquiero. " 
    "Suerte.")

opcion = input("A (En la salida decides coger el medio)  || B (En la salida decides coger el lado izquierdo): ")

if opcion == "A":
    print("Has decidio coger el carril del medio. Ahora tienes dos opciones.")
    opcion = input("A (Giras hacia el lado derecho de la pista.) || B (Te quedas en el medio.): ")

    if opcion == "A":
        print("Al girar hacia el lado derecho te encuentras con el coche de Uwe Alzen y los dos salis disparados contra el muro.\nFIN DE TU CARRERA. DNF")
    elif opcion == "B":
        print("Has conseguido hacer la salida sin chocarte contra ningun rival. Ahora viene la primera curva y tienes dos opciones. ")
        opcion = input("A (Decides apurar la frenada para poder adelantar al rival.) || B (Frenas antes de tiempo para no irte largo y salirte fuera de la pista.): ")

        if opcion == "A":
            print("Has conseguido adelantar a los tres primeros gracias a que has apurado la frenada.")
            print("Has ganado la carrera.")
        elif opcion == "B":
            print("Has decido frenar antes de tiempo por lo tanto el piloto Nikita Mazepin te da por detras y los dos os vais contra el muro.\n"
                  "Pero gracias al golpe que se ha dado contigo Nikita Mazepin no podra volver a correr en todo lo que queda de año.\nNo has conseguido terminar la carrera")

        else:
            print("\nEsa opcion no es valida.")

    else:
        print("\nEsa opcion nos es valida.")

elif opcion == "B":
    print("Has decidido coger el lado izquierdo. Ahora te encuentras con la primera curva ¿Que haces?")
    opcion = input("A (Tomar la curva por el interior) || B (Tomar la curva por el exterior): ")

    if opcion == "A":
        numero_random_vendedor = random.randint(1, 200)
        print("Has decido coger la curva por el interior y te dicen por radio que pongas la configuracion A. Para poner la configuracion necesitas saber la  \n"
              "siguiente multiplicación: 25 * {}".format(numero_random_vendedor))
        opcion = int(input("¿Cual es el número correcto?: "))

        if opcion == 25 * numero_random_vendedor:
            print("Al acertar la multiplicación el coche pone la configuración A. Ahora tienes una recta en la cual puedes adelantar al coche que tienes delante.")
            opcion = input("A (Lo adelantas por su lado derecho) || B (Lo adelantas por el lado izquierdo): ")

            if opcion == "A":
                print("Al adelantarlo por la derecha pisas con la rueda de atras la tierra y el coche te hace un trompo y te chocas contra el coche que querias adelantar.\nDNF")

            elif opcion == "B":
                print("Le consigues adelantar por el lado izquierdo pero llegas muy apurado a la siguiente curva. ¿Que haces? \n")
                opcion = input("A (Bloquear la rueda delantera) || B (No hacer nada y que pasa lo que pase): ")

                if opcion == "A":
                    print("Gracias al bloquear la rueda delantera consigues coger la curva de tus sueños y acabas la carrare en primera posicion. \n")
                    print("Has quedado P1")
                elif opcion == "B":
                    print("Has decido no hacer nada, por lo cual te vas largo y te estrellas contra el muro.\nDNF")

                else:
                    print("\nEsa opcion no es valida.")

            else:
                print("\nEsa opcion no es valida.")

        elif opcion != 25 * numero_random_vendedor:
            print ("Has FALLLADO. Te has salido de la pista y tu coche a sufrido daños en el motor.\nDNF")

        else:
            print("\nEsa opcion no es valida.")

    elif opcion == "B":
        print("has decido tomar la curva por el exterior. Tienes dos opciones. ¿Cual eliges?")
        opcion = input("A (En la siguiente recta adelantarle.) || B (Aguantar y no adelantar al coche que tienes por delante): ")

        if opcion == "A":
            print("Le intentas adelantar pero el piloto que tienes delante te cierra y te chocas contra el muro.\nDNF")
        elif opcion == "B":
            print("Decides no adelantar. LLegas a la siguiente curva ¿Que haces?")
            opcion = input("A (El equipo te dice que pongas la configuración de ataque) || B (No haces caso al equipo y sigues con la configuración que tenias): ")

            granada_inventario = False

            if opcion == "A":
                print("Has decido hacer caso a tu equipo y poner la configuracion de ataque.")
                granada_inventario = True
            elif opcion == "B":
                print("Has decidido no hacer caso a tu equipo.")

            print("Solo te queda un piloto por adelantar y lo podrias hacer en la siguiente curva. ¿Que haces?")
            opcion = input("A (Le adelantas por el interior) || B (Le adelantas por el exterior): ")

            if opcion == "A":
                print("Al adelantarlo por el interior os chocais mutuamente pero con la mala suerte de que sales disparado contra el muro.\nDNF")
            elif opcion == "B" and granada_inventario:
                print("Gracias a que has elegido poner la configuracion de ataque le consigues adelantar por el exterior al piloto que tenias delante.")
                print("Has conseguido ganar la carrera. P1")
            else:
                print("Al no elegir la configuracion de ataque no le consigues adelantar por el exterior y no ganas la carrera. \nFIN")
        else:
            print("\nEsa opcion no es valida.")

    else:
        print("\nEsa opcion no es valida.")

else:
    print("\nEsa opcion no es valida.")

print("\nFIN DEL JUEGO. ESPERO QUE TE HAYA GUSTADO <3")