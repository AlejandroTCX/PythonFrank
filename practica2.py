def main():
    string = input("Ingresa una cadena de texto: ")
    cadena = string

    while True:
        print("1-. Escribe una función que devuelva verdadero o falso si la primera letra de la cadena de texto es mayúscula.")
        print("2-. Escribe una función que cuente las palabras que forman la cadena de texto.")
        print("3-. Escribe una función que reciba como argumento la cadena de texto y regrese una lista con las palabras que la forman.")
        print("4-. Escribe una función que regrese la cadena de texto invertida.")
        print("5-. Escribe una función que regrese la cadena original con la última letra de cada palabra en mayúscula.")

        selection = input("Ingresa la opcion deseada: ")

        if selection == '1':
            result = function_1(cadena)
            print(result)
        elif selection == '2':
            length = len(cadena)
            print(length)
        elif selection == '3':
            lista = cadena.split()
            print(lista)
        elif selection == '4':
            print (cadena [::-1])
        elif selection == '5':
            lista = cadena.split()
            lista = list(map(lambda palabra: palabra[:-1] + palabra[-1].upper(), lista))
            print (lista)
        elif selection == '6':
            main()

def function_1(cadena):

    if cadena and cadena[0].isupper():
        return True
    else:
        return False
    


main() 
