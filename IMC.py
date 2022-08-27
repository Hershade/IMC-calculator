#Creo funciones para hacer mas legible y menos repetitivo el codigo
def imc_message(name, age, IMC, result):
    print('Hola' , name , 'Tienes' , age , 'años', 'Tu IMC es ' , IMC , result )

#Menu que vera el usuario
menu = """
1.- Calcular
2.-Salir
"""
option = ""
message = ""

second_menu = """
1.-- Recomendaciones segun mi peso
2.-- Regresar al menu principal
"""
#Falso mientras el usuario este usando el sistema 
leave = False 
# Iniciamos el ciclo
while not leave:
    print(menu)
    selection = input('Selecciona una opcion del menu:  ')
    # estructura de condiciones para el menu
    if selection == '1':
        # Inicia el programa
        #Solicitamos al usuario su nombre
        user_name = input('Ingresa tu nombre:  ')
        #Solicitamos al usuario su edad
        user_age = input('Ingresa tu edad:  ')
        #Solicitamos al usuario su peso en libras
        weight_pounds = float(input('Ingresa tu peso en libras:  '))
        #Solicitamos al usuario su altura en centimetros
        height_centimeters = float(input('Ingresa tu altura en centimetros:  '))

        #Necesitamos crear mas variables para poder usuar la formula del IMC
        #Convertimos el peso en libras a kilogramos
        weight_kg = weight_pounds / 2.205
        height_mtrs = height_centimeters / 100

        #formula del IMC
        IMC = round(weight_kg /(height_mtrs**2) , 2)
        #Clasificacion del IMC del usuario
        if IMC <= 18.5:
            imc_message(user_name, user_age, IMC, "Actualmente te encuentras por debajo de tu peso ideal")
        if IMC >= 18.5 and IMC <= 24.9:
            imc_message(user_name, user_age, IMC, " Actualmente estas en tu peso ideal " )
        if IMC >= 25 and IMC <= 29.9:
            imc_message(user_name, user_age, IMC,'Actualmente estas en sobrepeso' )
        if IMC >= 30 and IMC <= 34.9:
            imc_message(user_name, user_age, IMC, 'Actualmente estas en obesidad tipo I ' )
        if IMC >= 35 and IMC <= 39.9:
            imc_message(user_name, user_age, IMC,'Actualmente estas en obesidad tipo II ' )
        if IMC >= 40:
            imc_message(user_name, user_age, IMC,'Actualmente estas en obesidad tipo III ' )
        # Variables y funciones para el menu secundario
        print(second_menu)
        option = input('Elige una opcion: ')
        if option == '1':
            if IMC <= 18.5:
                message = """
                1.-Come con más frecuencia.
                2.-Prueba licuados y batidos de fruta.
                3.-Agrega aderezos a tus comidas sin exederte.
                5.-Hacer ejercicio.
                4.-Para una mejor guia acude a tu medico. 
                """
            if IMC >= 18.5 and IMC <= 24.9:
                message = """
                1.-Mantener una dieta saludable.
                2.-Haz Ejercicio regular.
                3.-Merienda saludable.
                4.-Beba mucho líquido.
                5.-Para una mejor guia acude a tu medico.
                """
            if IMC >= 25 and IMC <= 29.9:
                message ="""
                1.-Empieza una dieta.
                2.-Haz ejercicio con frecuencia.
                3.-Ve evitando las comiadas altas en calorias.
                4.-Acude inmediatamente a tu medico para una mejor orientacion.
                """
            if IMC >= 30 and IMC <= 34.9:
                message ="""
                1.-Empieza una dieta saludable.
                2.-Haz ejercicio con frecuencia.
                3.-Acude inmediatamente a tu medico para una mejor orientacion.
                """
            if IMC >= 35 and IMC <= 39.9:
                message = """
                1.-Empieza a cuidar tu alimentacion.
                2.-Evita las comidas altas en calorias.
                3.-Empieza una rutina de ejercicios.
                4.-Acude inmediatamente a tu medico para una mejor orientacion.
                """
            if IMC >= 40:
                message = """
                1.-Empieza a cuidar tu alimentacion.
                2.-Evita las comidas altas en calorias.
                3.-Empieza una rutina de ejercicios.
                4.-Acude inmediatamente a tu medico para una mejor orientacion.
                """
            print(message)
        elif option == '2':
            pass        
    elif selection == '2':
        print('Gracias por usar mi Calculadora')
        leave = True  




