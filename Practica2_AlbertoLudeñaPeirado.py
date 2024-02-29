import random
import time

# crear 3 abbs vacios
arbol1 = {"raiz": None}
arbol2 = {"raiz": None}
arbol3 = {"raiz": None}

def pedir_usuarios():
    while True:
        try:
            id_usuario = int(input("Dime el ID del usuario (debe ser un número entre 0 y 999999): "))
            if id_usuario < 0 or id_usuario > 999999:
                print("El ID del usuario no es válido. Por favor, inténtelo de nuevo.")
            else:
                break
        except ValueError:
            print("ID tiene que ser un numero entero.")

    # nombre usuario
    while True:
        nombre = input("Introduce el nombre: ")
        if not nombre.isalpha() or len(nombre) > 10:
            print("Nombre no valido, maximo 10 caracteres.")
        else:
            break

    # edad usuario
    while True:
        try:
            edad = int(input("Introduce la edad "))
            if edad < 0 or edad > 99:
                print("La edad del usuario no es válida, tiene que ser entre 0 y 99.")
            else:
                break
        except ValueError:
            print("Edad tiene que ser un numero entero.")

    # genero usuarios
    while True:
        genero = input("Introduce el género (masculino, femenino u otro): ")
        if genero not in ["masculino", "femenino", "otro"]:
            print("El género no es masculino, femenino u otro, esta mal puesto, intentalo otra vez.")
        else:
            break

    # tipo de cine
    while True:
        tipo_cine = input("Introduce tipo de cine (comedia, terror o fantasia): ")
        if tipo_cine not in ["comedia", "terror", "fantasia"]:
            print("no valido el cine introducido, eliga comedia, terror o fantasia.")
        else:
            break

    # entrada
    while True:
        entrada = input("va a querer una entrada (si o no): ")
        if entrada not in ["si", "no"]:
            print("tiene que ser si o no, introduzca de nuevo.")
        else:
            break

    # Creamos el diccionario con los datos del usuario y lo devolvemos
    diccionario_del_usuario = {
        "id": id_usuario,
        "nombre": nombre,
        "edad": edad,
        "genero": genero,
        "tipo_cine": tipo_cine,
        "entrada": entrada,
    }
    return diccionario_del_usuario

# funcion para crear un nodo a partir de este diccionario

def nuevo_nodo(dicc_nodo_usuario):
    return {
        "id": dicc_nodo_usuario["id"],
        "nombre": dicc_nodo_usuario["nombre"],
        "edad": dicc_nodo_usuario["edad"],
        "genero": dicc_nodo_usuario["genero"],
        "tipo_cine": dicc_nodo_usuario["tipo_cine"],
        "entrada": dicc_nodo_usuario["entrada"],
        "izq": None,
        "dcha": None,
    }


# funcion para meter_nodo_arbol un nodo en el arbol
# lo que hacemos aqui es que si el id es menor lo pondremos a la izq del nodo del que partimos y si es mayor a la dcha


def meter_nodo_arbol(usuario, nodo):
    if nodo is None:
        return nuevo_nodo(usuario)
    elif usuario["id"] < nodo["id"]:
        if "izq" in nodo:
            if nodo["izq"] is not None:
                nodo["izq"] = meter_nodo_arbol(usuario, nodo["izq"])
            else:
                nodo["izq"] = nuevo_nodo(usuario)
        else:
            nodo["izq"] = nuevo_nodo(usuario)
    else:
        if "dcha" in nodo:
            if nodo["dcha"] is not None:
                nodo["dcha"] = meter_nodo_arbol(usuario, nodo["dcha"])
            else:
                nodo["dcha"] = nuevo_nodo(usuario)
        else:
            nodo["dcha"] = nuevo_nodo(usuario)
    return nodo


# funcion para encontrar_nodo un nodo en el arbol
def encontrar_nodo(id_usuario, nodo):
    if nodo is None:
        return None
    elif id_usuario == nodo["id"]:
        return nodo
    elif id_usuario < nodo["id"]:
        return encontrar_nodo(id_usuario, nodo["izq"])
    else:
        return encontrar_nodo(id_usuario, nodo["dcha"])


def quitar_nodo(nodo, padre):
    if nodo is None:
        return

    # Si el nodo a borrar no tiene hijos
    if nodo["izq"] is None and nodo["dcha"] is None:
        if padre is None:  # Es la raíz
            nodo = None
        elif padre["izq"] == nodo:
            padre["izq"] = None
        else:
            padre["dcha"] = None
    # Si el nodo a borrar tiene un solo hijo
    elif nodo["izq"] is None:
        hijo = nodo["dcha"]
        nodo["id"] = hijo["id"]
        nodo["izq"] = hijo["izq"]
        nodo["dcha"] = hijo["dcha"]
    elif nodo["dcha"] is None:
        hijo = nodo["izq"]
        nodo["id"] = hijo["id"]
        nodo["izq"] = hijo["izq"]
        nodo["dcha"] = hijo["dcha"]
    # Si el nodo a borrar tiene dos hijos
    else:
        padre_sucesor = nodo
        sucesor = nodo["dcha"]
        while sucesor["izq"] is not None:
            padre_sucesor = sucesor
            sucesor = sucesor["izq"]
        nodo["id"] = sucesor["id"]
        quitar_nodo(sucesor, padre_sucesor)


def print_abb_en_order(nodo, orden):
    if nodo is None:
        return
    if orden == "inorder":
        print_abb_en_order(nodo.get("izq"), orden)
        print(nodo["id"])
        print_abb_en_order(nodo.get("dcha"), orden)
    elif orden == "preorder":
        print(nodo["id"])
        print_abb_en_order(nodo.get("izq"), orden)
        print_abb_en_order(nodo.get("dcha"), orden)
    elif orden == "postorder":
        print_abb_en_order(nodo.get("izq"), orden)
        print_abb_en_order(nodo.get("dcha"), orden)
        print(nodo["id"])
    else:
        print("Lo que ha introducido no es correcto, por favor introduzca inorder, preorder o postorder")


def extension(nodo, nv_actual):
    if nodo is None:
        return 0, nv_actual - 1
    izq_extension, izq_profundidad = extension(nodo.get("izq"), nv_actual + 1)
    dcha_extension, dcha_profundidad = extension(nodo.get("dcha"), nv_actual + 1)
    return izq_extension + dcha_extension + 1, max(izq_profundidad, dcha_profundidad)


def crea_usuario_random():
    id_tarjeta = random.randrange(100000, 999999)
    nombres = [
        "Alberto", "Fran","Luis", "Silvia","Mario","Lucia","Carlos","Alejandro", "Marta", "Nicolas", "Maria","Laura", "Marcos"]
    nombre = random.choice(nombres)
    edad = random.randrange(1, 99)
    generos = ["masculino", "femenino", "otro"]
    genero = random.choice(generos)
    tipo_cine = ["comedia", "terror", "fantasia"]
    tipo_cine = random.choice(tipo_cine)
    entrada = ["si", "no"]
    entrada = random.choice(entrada)
    usuario = {
        "id": id_tarjeta,
        "nombre": nombre,
        "edad": edad,
        "genero": genero,
        "tipo_cine": tipo_cine,
        "entrada": entrada,
    }

    return usuario


def apartado1():
    print("Ha elegido la opción 1")
    # tenemos que meter_nodo_arbol un usuario en un arbol
    # pedimos los datos del usuario
    dicc_nodo_usuario = pedir_usuarios()
    # crear el nodo raiz que sera el id del usuario generado
    nodo = nuevo_nodo(dicc_nodo_usuario)
    # preguntamos en que arbol queremos meter_nodo_arbol el nodo
    while True:
        arbol = input("En que arbol quieres meter el nodo (1, 2 o 3): ")
        if arbol not in ["1", "2", "3"]:
            print("El arbol no es válido.")
        else:
            break
    if arbol == "1":
        if arbol1["raiz"] is None:
            arbol1["raiz"] = nodo
        else:
            meter_nodo_arbol(dicc_nodo_usuario, arbol1["raiz"])
    elif arbol == "2":
        if arbol2["raiz"] is None:
            arbol2["raiz"] = nodo
        else:
            meter_nodo_arbol(dicc_nodo_usuario, arbol2["raiz"])
    else:
        if arbol3["raiz"] is None:
            arbol3["raiz"] = nodo
        else:
            meter_nodo_arbol(dicc_nodo_usuario, arbol3["raiz"])

    print("Usuario añadido a ", arbol)

    # imprimir el arbol y si esta vacio decir que esta vacio en un print
    print("El arbol", arbol, "es:")
    if arbol == "1":
        if arbol1["raiz"] is None:
            print(" vacio")
        else:
            print(arbol1["raiz"])
    elif arbol == "2":
        if arbol2["raiz"] is None:
            print(" vacio")
        else:
            print(arbol2["raiz"])
    else:
        if arbol3["raiz"] is None:
            print(" vacio")
        else:
            print(arbol3["raiz"])


def apartado2():
    print("Ha elegido la opción 2")

    while True:
        id_usuario = input("Introduzca el id del usuario que desea encontrar: ")
        if not id_usuario.isdigit():
            print("El id no es válido. Por favor, inténtelo de nuevo.")
        else:
            break
    # primero ver si el id están en un nodo raíz de los 3 árboles que tenemos
    # si está en el árbol 1
    if arbol1["raiz"] is not None:
        if id_usuario == str(arbol1["raiz"]["id"]):
            print("usuario en abb 1")
            print(arbol1["raiz"])
            # sacar el usuario entero
            print("El usuario es el nodo raiz de este arbol:")
            return
        # comprobar si lo tenemos en un nodo del árbol 1
        else:
            nodo = encontrar_nodo(int(id_usuario), arbol1["raiz"])
            if nodo is not None:
                print("usuario en abb 1")
                print(nodo)
                # sacar el id del nodo raiz del arbol 1
                print("el id del arbol del usuario es :")
                print("id:", arbol1["raiz"]["id"])

                return
    # si está en el árbol 2
    if arbol2["raiz"] is not None:
        if id_usuario == str(arbol2["raiz"]["id"]):
            print("usuario en abb 2")
            print(arbol2["raiz"])
            # sacar el usuario entero
            print("El usuario es el nodo raiz de este arbol:")
            return
        # comprobar si lo tenemos en un nodo del árbol 2
        else:
            nodo = encontrar_nodo(int(id_usuario), arbol2["raiz"])
            if nodo is not None:
                print("usuario en abb 2")
                print(nodo)
                print("el id del arbol del usuario es :")
                print("id:", arbol2["raiz"]["id"])
                return
    # si está en el árbol 3
    if arbol3["raiz"] is not None:
        if id_usuario == str(arbol3["raiz"]["id"]):
            print("El usuario se encuentra en el arbol 3")
            print(arbol3["raiz"])
            # sacar el usuario entero
            print("El usuario es el nodo raiz de este arbol:")
            return
        # comprobar si lo tenemos en un nodo del árbol 3
        else:
            nodo = encontrar_nodo(int(id_usuario), arbol3["raiz"])
            if nodo is not None:
                print("usuario en abb 3")
                print(nodo)
                print("el id del arbol del usuario es :")
                print("id:", arbol3["raiz"]["id"])
                return


def apartado3():
    print("Ha elegido la opción 3")
    # imprimir lista de usuarios en cualquier arbol sacando la extension y profundidad de cada arbol
    # pedir el arbol que queremos imprimir
    while True:
        arbol = input("De qué árbol quieres imprimir la lista de usuarios (1, 2 o 3): ")
        if arbol not in ["1", "2", "3"]:
            print("Arbol no valido, ponga lista 1, 2 o 3.")
        else:
            break

    # pedir el orden en que se van a imprimir los usuarios
    while True:
        orden = input(
            "En qué orden quieres imprimir los usuarios (inorder, preorder o postorder): ")
        if orden not in ["inorder", "preorder", "postorder"]:
            print("El orden no es válido. Por favor, inténtelo de nuevo.")
        else:
            break

    # Sacar la extension y profundidad del árbol sin usar llamadas a otros métodos
    if arbol == "1":
        if arbol1["raiz"] is None:
            print("El árbol está vacío")
        else:
            tamaño_actual, prof_actual = extension(arbol1["raiz"], 0)
            print(
                f"La extension del árbol es: {tamaño_actual}. La profundidad del árbol es: {prof_actual}.")
            print("Lista de usuarios:")
            print_abb_en_order(arbol1["raiz"], orden)
    elif arbol == "2":
        if arbol2["raiz"] is None:
            print("El árbol está vacío")
        else:
            tamaño_actual, prof_actual = extension(arbol2["raiz"], 0)
            print(
                f"La extension del árbol es: {tamaño_actual}. La profundidad del árbol es: {prof_actual}.")
            print("Lista de usuarios:")
            print_abb_en_order(arbol2["raiz"], orden)
    elif arbol == "3":
        if arbol3["raiz"] is None:
            print("El árbol está vacío")
        else:
            tamaño_actual, prof_actual = extension(arbol3["raiz"], 0)
            print(
                f"La extension del árbol es: {tamaño_actual}. La profundidad del árbol es: {prof_actual}.")
            print("Lista de usuarios:")
            print_abb_en_order(arbol3["raiz"], orden)




def apartado4():
    print("Ha elegido la opción 4")
    # Borrar un espectador, cuya tarjeta haya sido introducida por teclado, si existe en ese ABB
    # pedir el id del usuario que queremos borrar
    while True:
        id_usuario = input("Introduzca el id del usuario que desea borrar: ")
        if not id_usuario.isdigit():
            print("El id no es válido. Por favor, inténtelo de nuevo.")
        else:
            break
    # primero ver si el id están en un nodo raíz de los 3 árboles que tenemos
    # si está en el árbol 1
    if arbol1["raiz"] is not None:
        if id_usuario == str(arbol1["raiz"]["id"]):
            arbol1["raiz"] = None
            print("El usuario se ha borrado correctamente del arbol 1")
            return
        # comprobar si lo tenemos en un nodo del árbol 1
        else:
            nodo = encontrar_nodo(int(id_usuario), arbol1["raiz"])
            if nodo is not None:
                quitar_nodo(nodo, None)
                print("El usuario se ha borrado correctamente del arbol 1")
                return
    # si está en el árbol 2
    if arbol2["raiz"] is not None:
        if id_usuario == str(arbol2["raiz"]["id"]):
            arbol2["raiz"] = None
            print("El usuario se ha borrado correctamente del arbol 2")
            return
        # comprobar si lo tenemos en un nodo del árbol 2
        else:
            nodo = encontrar_nodo(int(id_usuario), arbol2["raiz"])
            if nodo is not None:
                quitar_nodo(nodo, None)
                print("El usuario se ha borrado correctamente del arbol 2")
                return
    # si está en el árbol 3
    if arbol3["raiz"] is not None:
        if id_usuario == str(arbol3["raiz"]["id"]):
            arbol3["raiz"] = None
            print("El usuario se ha borrado correctamente del arbol 3")
            return
        # comprobar si lo tenemos en un nodo del árbol 3
        else:
            nodo = encontrar_nodo(int(id_usuario), arbol3["raiz"])
            if nodo is not None:
                quitar_nodo(nodo, None)
                print("El usuario se ha borrado correctamente del arbol 3")
                return





def apartado5():
    print("Ha elegido la opción 5")

    # Pedir el número de usuarios que queremos crear
    while True:
        num_usuarios = input("Cuantos usuarios quiere crear: ")
        if not num_usuarios.isdigit():
            print("numero no valido, reintentelo.")
        else:
            break

    # Elegir aleatoriamente uno de los tres árboles
    arbol_num = random.randint(1, 3)
    if arbol_num == 1:
        arbol = arbol1
    elif arbol_num == 2:
        arbol = arbol2
    else:
        arbol = arbol3

    # Crear los usuarios y agregar cada usuario al árbol elegido
    for i in range(int(num_usuarios)):
        usuario = crea_usuario_random()
        arbol["raiz"] = meter_nodo_arbol(usuario, arbol["raiz"])

    print("Los usuarios se han creado correctamente")

    # Imprimir contenido de los 3 árboles
    print("Contenido de los 3 árboles:")
    print("Arbol 1:")
    print(arbol1["raiz"])
    print("Arbol 2:")
    print(arbol2["raiz"])
    print("Arbol 3:")
    print(arbol3["raiz"])


def apartado6():
    print("Ha elegido la opción 6")

    # Pedir el número de usuarios que queremos crear
    while True:
        num_usuarios = input("Cuanto usuarios quiere crear: ")
        if not num_usuarios.isdigit():
            print("No valido, reintentelo.")
        else:
            break

    # Generar los usuarios usando la función crea_usuario_random
    usuarios = []
    for i in range(int(num_usuarios)):
        usuario = crea_usuario_random()
        usuarios.append(usuario)

    # meter_nodo_arbol los usuarios en un solo árbol de forma aleatoria
    abbs = [arbol1, arbol2, arbol3]
    abbs_aleatorios = random.choice(abbs)
    usuarios_eliminados = []
    for usuario in usuarios:
        # Comparar los usuarios generados con los que tenemos en el árbol aleatorio,
        # si el id es igual, lo borra del árbol y lo agrega a la lista de usuarios borrados
        if abbs_aleatorios["raiz"] is not None:
            if usuario["id"] == abbs_aleatorios["raiz"]["id"]:
                usuarios_eliminados.append(abbs_aleatorios["raiz"])
                abbs_aleatorios["raiz"] = None
            else:
                nodo = encontrar_nodo(usuario["id"], abbs_aleatorios["raiz"])
                if nodo is not None:
                    usuarios_eliminados.append(nodo)
                    nodo = None

        abbs_aleatorios["raiz"] = meter_nodo_arbol(usuario, abbs_aleatorios["raiz"])

    # Imprimir los usuarios borrados
    if len(usuarios_eliminados) > 0:
        print("Los siguientes usuarios han sido borrados:")
        for usuario in usuarios_eliminados:
            print(usuario)
    else:
        print("No se han borrado usuarios")
    for usuario in usuarios:
        print("Usuario: ", usuario["id"])


def apartado7():
    print("Ha seleccionado la opción 7")
    print("Inicializando simulación...")

    # La simulación dura 60 segundos
    espect_descartados = 0
    for i in range(12):
        # Creamos un espectador
        espectador = crea_usuario_random()
        # Elegimos un árbol aleatoriamente
        abbs = [arbol1, arbol2, arbol3]
        abbs_aleatorios = random.choice(abbs)
        abbs_aleatorios["raiz"] = meter_nodo_arbol(espectador, abbs_aleatorios["raiz"])

        # Imprimimos el espectador que se añadió
        print("Espectador", espectador, "añadido al Árbol",
            abbs.index(abbs_aleatorios) + 1)
        # Verificamos el valor de entrada del usuario
        if espectador["entrada"] == "si":
            # No se borra el espectador del árbol
            pass
        elif espectador["entrada"] == "no":
            # Se borra un espectador de un árbol aleatorio si es que hay alguno
            abbs_aleatorios = random.choice(abbs)
            if abbs_aleatorios["raiz"] is not None:
                # Imprimimos el espectador que se borró
                print("Espectador borrado", abbs_aleatorios["raiz"]["id"])
                abbs_aleatorios["raiz"] = None
                # Contador de espectadores borrados
                espect_descartados += 1
                print("Espectadores borrados:", espect_descartados)
            else:
                print("No hay espectadores para borrar")
        else:
            print("Entrada inválida")

        # Imprimimos el estado actual de los árboles y el segundo de la simulación
        print(f"Estado de los árboles en el segundo {i * 5}:")
        for j, arbol in enumerate(abbs):
            print("Árbol", j+1, end=": ")
            if arbol["raiz"] is not None:
                # Recorremos el árbol en inordcha e imprimimos cada nodo
                stack = []
                actual = arbol["raiz"]
                while True:
                    if actual is not None:
                        stack.append(actual)
                        actual = actual["izq"]
                    elif (stack):
                        actual = stack.pop()
                        print(actual["id"], end=" ")
                        actual = actual["dcha"]
                    else:
                        break
                print()
            else:
                print("vacio")

        # Hacemos una pausa de 5 segundos antes de la siguiente iteración
        time.sleep(5)


def apartado8():
    print("Gracias por usar nuestro programa, hasta pronto")
    exit()


# Aqui vamos a por todo el tema relacionado con el menu

while True:
    print("Bienvenido al menu:")
    print("1. Insertar un miembro en un ABB")
    print("2. encontrar_nodo cualquier espectador en un ABB")
    print("3. Imprimir lista de espectadores en cualquier ABB indicando el recorrido de cualquier forma: extension, profundidad(inorden, preorden, postorden))")
    print("4. Borrar un espectador, cuya tarjeta haya sido introducida por teclado, si existe en ese ABB")
    print("5. Introducir un numero y crear dicha cantidad de espectadores al azar, guardando en el correspondiente ABB estos espectadores:1,2,3")
    print("6. Introducir un numero y generar al azar dicha cantidad de es espectadores, que se borrara, si existen en los ABB")
    print("7. Iniciar la simulacion ")
    print("8. Salir del programa ")

    apartado = input("Ingresa el número de opción: ")

    if apartado == "1":
        apartado1()
    elif apartado == "2":
        apartado2()
    elif apartado == "3":
        apartado3()
    elif apartado == "4":
        apartado4()
    elif apartado == "5":
        apartado5()
    elif apartado == "6":
        apartado6()
    elif apartado == "7":
        apartado7()
    elif apartado == "8":
        apartado8()
    else:
        print("Opción no válida")
