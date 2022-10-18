print ("CALCULADORA FÍSICA PARA TIROS")
TipoTiro = int(input(
    '''¿Qué tipo de tiro va a querer calcular?
     1. TIRO VERTICAL
     2. CAÍDA LIBRE
     3. TIRO OBLICUO
     4. TIRO HORIZONTAL
     Seleccione un número del 1 al 4: '''))
print ("*La gravedad en todos los casos será de 9,8 m/s2*") 
GRAVEDAD = (-9.8)   

if TipoTiro == 1:
    def pedirdatosV():
        global velinicialV, graficarV, altinicialV
        velinicialV = float(input("Ingrece la velocidad inicial del objeto (m/s): "))
        altinicialV = float(input("Ingrece la altura inicial: "))
        graficarV = input("¿Desea graficar los datos una vez terminado el ejercicio? s/n: ")

    pedirdatosV()
    def calculosV():
        global tiempomaxV, alturamaxV
        tiempomaxV = velinicialV / (-GRAVEDAD)
        alturamaxV = altinicialV + velinicialV * tiempomaxV + 1/2 * GRAVEDAD * tiempomaxV**2

    calculosV()
    print ("La altura máxima fué de: ", alturamaxV, " metros. El tiempo que tardó el objeto en llegar a la altura máxima fué de: ", tiempomaxV, " segundos.")

elif TipoTiro == 2:
    def pedirdatosL():
        global alturaL, velinicialL
        alturaL = float(input("Ingrese la altura de la que cae el objeto: "))
        velinicialL = float(input("Ingrese la velocidad inicial del objeto: "))

    pedirdatosL()
    def calculosL():
        global tiempoL, velfinalL
        tiempoL = alturaL + velinicialL * tiempoL + 1/2 + GRAVEDAD * tiempoL ** 2 = 0
        velfinalL = velinicialL + GRAVEDAD + tiempoL
    
    calculosL()

    print ("El tiempo que tardó el objeto en caer fué de: ", tiempoL, ". La velocidad máxima que alcanzó fué de: ", velfinalL)