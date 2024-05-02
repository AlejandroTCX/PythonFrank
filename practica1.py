def capturaNumeros():
    numeros = []

    
    while True:
        try:
            num = input("Ingresa un numero y escribe S cuando termines de agregar: ")
            if num.lower() == 's':
                break
            numeros.append(float(num))
        except ValueError:
            print("Error: Ingresa un valor numérico válido.")
   
    while True:
        try:
            print("\nSelecciona una opción del menú:")
            print("1. Imprime una sublista de 2 elementos que corresponda a la mitad de la lista original, independientemente de la cantidad de elementos.")
            print("2. De la lista original, imprime solo una línea de código del primer elemento y el último.")
            print("3. De la lista original, agrega los elementos de la lista final de la misma, imprime el resultado.")
            print("4. De la lista obtenida, ordena los elementos de menor a mayor e imprime el resultado.")
            print("5. Vuelve a ordenar sus elementos de mayor a menor e imprime su resultado.")
            print("6. Escribe una función que devuelva el cubo de los elementos de la lista e imprime el resultado.")
            print("7. Salir.")

            eleccion = input("Ingresa la opción: ")

            if eleccion == '1':
                funcion_1(numeros)
            elif eleccion == '2':
                funcion_2(numeros)
            elif eleccion == '3':
                funcion_3(numeros)
            elif eleccion == '4':
                funcion_4(numeros)
            elif eleccion == '5':
                funcion_5(numeros)
            elif eleccion == '6':
                funcion_6(numeros)

            elif eleccion == '7':
                break
            else:
                print("Opción no valida")

        except ValueError:
            print("Ingresa un numero")

def funcion_1(numeros):
    numeros_mitad = len(numeros) // 2
    listaMitad = numeros[numeros_mitad - 1: numeros_mitad + 1]
    print("Lista original: ", numeros)
    print("Sublista de la mitad de la lista original:", listaMitad)

def funcion_2(numeros):
    primeroNumero = numeros[0]
    ultimoNumero = numeros[-1]
    primeroUltimo = [primeroNumero, ultimoNumero]
    print("Lista original: ", numeros)
    print("Primero y último elemento de la lista original:", primeroUltimo)

def funcion_3(numeros):
    ultimoNumero = numeros[-1]
    listaNueva = numeros[:]
    listaNueva.append(ultimoNumero)
  
   

    print("Lista original: ", numeros)
    print("Lista nueva: ", listaNueva)

def funcion_4(numeros):
    numeros_ordenados = sorted(numeros)
    print("Lista original: ", numeros)
    print("Lista ordenada de menor a mayor:", numeros_ordenados)

def funcion_5(numeros):
    numeros_ordenados = sorted(numeros, reverse=True)
    print("Lista original: ", numeros)
    print("Lista ordenada de mayor a menor:", numeros_ordenados)

def funcion_6(numeros):
    cubos = [numero ** 3 for numero in numeros]
    print("Lista original: ", numeros)
    print("Cubos de los elementos de la lista:", cubos)

def funcion_7():
    capturaNumeros(numeros = [])


capturaNumeros()
