#menu
def calcular():
    while True:
        print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
        opcion = input("Elija una opción: ")

        match opcion:
            case "1":
                try:
                    num1 = float(input("Ingrese Primer número a sumar: "))
                    num2 = float(input("Ingrese segundo número a sumar: "))
                    sumar()
                except ValueError:
                    print("Error: Debes ingresar un número válido.")
            case "2":
                try:
                    num1 = float(input("Ingrese Primer número a restar: "))
                    num2 = float(input("Ingrese segundo número a restar: "))
                    restar()
                except ValueError:
                    print("Error: Debes ingresar un número válido.")
            case "3":
                try:
                    num1 = float(input("Ingrese Primer número a multiplicar: "))
                    num2 = float(input("Ingrese segundo número a multiplicar: "))
                    multiplicar()
                except ValueError:
                    print("Error: Debes ingresar un número válido.")
            case "4":
                try:
                    num1 = float(input("Ingrese Primer número a dividir: "))
                    num2 = float(input("Ingrese segundo número a dividir: "))
                    division()
                except ValueError:
                    print("Error: Debes ingresar un número válido.")
                except ZeroDivisionError:
                    print("Error: No se puede dividir entre cero.")
            case "5":
                break
            case _:
                print("Ingrese un número válido e intente nuevamente")


calcular()