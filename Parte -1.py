from script import lista_personajes
import os

#B
def punto_b(lista_personajes):
    for var_nombre in lista_personajes:
        nombre = var_nombre["nombre"]
        print(f"Nombre del superheroe / heroína:{nombre}")

# punto_b(lista_personajes)
#C
def punto_c(lista_personajes):
    for personaje in lista_personajes:
        nombre = personaje["nombre"]
        altura = personaje["altura"]
        print(f"Nombre: {nombre} || Altura: {altura} cm")


# punto_c(lista_personajes)
#D
def punto_d(lista_personajes):
    
    personaje_mas_alto = None
    altura_maxima = 0

    for personaje in lista_personajes:
        altura = personaje["altura"]
        altura = int(float(altura))
        if altura > altura_maxima:
            altura_maxima = altura
            personaje_mas_alto = personaje["nombre"]
    print(f"El personaje más alto es {personaje_mas_alto} con una altura de {altura_maxima}")

# punto_d(lista_personajes)
#E
def punto_e(lista_personajes):
    persona_mas_baja = None

    for personaje in lista_personajes:
        altura = float(personaje["altura"])
        if persona_mas_baja == None or altura < persona_mas_baja:
            altura_minima = altura
            personaje_petiso = personaje["nombre"]

    print(f"El personaje más bajo es {personaje_petiso} con una altura de {altura_minima}") #####NO ME ANDA

# punto_e(lista_personajes)
#F
def punto_f(lista_personajes):
    acumulador = 0
    contador = 0
    for personaje in lista_personajes:
        altura = personaje["altura"]
        altura = int(float(altura))
        acumulador += altura
        contador += 1
        if contador > 0:
            promedio = acumulador / contador
    print(f"El promedio de altura es de {promedio}")

# punto_f(lista_personajes)

#G

### 
def punto_g(lista_personajes):
    persona_mas_alta = None
    persona_mas_baja = None
    altura_min = float('inf')  
    altura_max = 0  
    
    for personaje in lista_personajes:
        altura = float(personaje["altura"])
        
        if altura < altura_min:
            altura_min = altura
            persona_mas_baja = personaje["nombre"]
        elif altura > altura_max:
            altura_max = altura
            persona_mas_alta = personaje["nombre"]
    
    print(f"El personaje más bajo es {persona_mas_baja} con una altura de {altura_min} y el más alto es {persona_mas_alta} con {altura_max}")

# punto_g(lista_personajes)
#H
def punto_h(lista_personajes):
    mas_pesado = None
    menos_pesado = None
    mayor_peso = 0
    menor_peso = 1000

    for personaje in lista_personajes:
        peso = personaje["peso"]
        peso = int(float(peso))
        
        if peso > mayor_peso:
            mayor_peso = peso
            mas_pesado = personaje["nombre"]
        if peso < menor_peso:
            
            menor_peso = peso
            menos_pesado = personaje["nombre"]

    print(f"El personaje más pesado es {mas_pesado} con un peso de {mayor_peso} y el menos pesado es {menos_pesado}con un peso de {menor_peso}")

# punto_h(lista_personajes)   

def punto_i(lista_personajes):
    print("Funcion que llama a las otras")
    punto_b(lista_personajes)
    punto_c(lista_personajes)
    punto_d(lista_personajes)
    punto_e(lista_personajes)
    punto_f(lista_personajes)
    punto_h(lista_personajes)

# punto_i(lista_personajes)


######     MENU DE OPCIONES

seguir = True
flag_nombre = False
flag_brindis = False

while seguir:
    print("        *Lista de superheroes*         ")
    print("1-Nombre de los superhéroes")
    print("2-Nombre de los superhéroes y altura")
    print("3-Superhéroe más alto")
    print("4-Superhéroe más bajo")
    print("5-Promedio de altura")
    print("6-Superhéroe más alto y más enano")
    print("7-Héroe más y menos pesado")
    print("8-Salir")

    opcion = input("Ingrese opción: ")

    if opcion == "1":
        punto_b(lista_personajes)
    elif opcion == "2":
        punto_c(lista_personajes)
    elif opcion == "3":
        punto_d(lista_personajes)
    elif opcion == "4":
        punto_e(lista_personajes)
    elif opcion == "5":
        punto_f(lista_personajes)
    elif opcion == "6":
        punto_g(lista_personajes)
    elif opcion == "7":
        punto_h(lista_personajes)
    elif opcion == "8":
        print("Saliendo")
        break

    else:
        print("Elija una opción valida")

    
    if seguir:
     os.system("pause")
    
