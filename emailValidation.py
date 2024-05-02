import re
def main():
     email = input("Ingresa tu email")
     if emailValidation(email):
          print('Es un email valido')
     else:
        print('Es invalido')

def emailValidation(email):
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if re.match(regex, email):
        
            return True
        
        else:        
            return False


main()
