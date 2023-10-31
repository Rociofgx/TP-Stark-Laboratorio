from script import lista_personajes
import os

#A
def punto_a():
    for personaje_M in lista_personajes:
        if personaje_M["genero"] == "M":
            print(personaje_M["nombre"])
punto_a()
#B
def punto_b():
    for personaje_f in lista_personajes:
        if personaje_f["genero"] == "F":
            print(personaje_f["nombre"])
punto_b()
#C
def punto_c():
    altura_maxima = 0
    personaje_mas_alto = None
    
    for personaje in lista_personajes:
        if personaje["genero"] == "M":
            altura_str = personaje["altura"]
            altura = float(altura_str)
            if altura > altura_maxima:
                altura_maxima = altura
                personaje_mas_alto = personaje
    
    if personaje_mas_alto is not None:
        print(f"El superhéroe más alto de género M es {personaje_mas_alto['nombre']} con una altura de {altura_maxima} cm.")

punto_c()
#D
def punto_d():
    altura_maxima = 0
    personaje_mas_alto = None
    
    for personaje in lista_personajes:
        if personaje["genero"] == "F":
            altura_str = personaje["altura"]
            altura = float(altura_str)
            if altura > altura_maxima:
                altura_maxima = altura
                personaje_mas_alto = personaje
    
    if personaje_mas_alto is not None:
        print(f"La heroína más alta de género F es {personaje_mas_alto['nombre']} con una altura de {altura_maxima} cm.")


punto_d()

#E 
def punto_e():
    altura_minima = float('inf')  
    personaje_mas_bajo = None

    for personaje in lista_personajes:
        if personaje["genero"] == "M":
            altura_str = personaje["altura"]
            altura = float(altura_str)
            if altura < altura_minima:
                altura_minima = altura  
                personaje_mas_bajo = personaje

    if personaje_mas_bajo is not None:
        print(f"El héroe masculino más bajo es {personaje_mas_bajo['nombre']} con una altura de {altura_minima} cm")

punto_e()

#F
def punto_f():
    altura_minima = float('inf')  
    personaje_mas_bajo = None

    for personaje in lista_personajes:
        if personaje["genero"] == "F":
            altura_str = personaje["altura"]
            altura = float(altura_str)
            if altura < altura_minima:
                altura_minima = altura  
                personaje_mas_bajo = personaje

    if personaje_mas_bajo is not None:
        print(f"La heroína más baja es {personaje_mas_bajo['nombre']} con una altura de {altura_minima} cm")

punto_f()
#G
def calculadora_promedio():
    acumulador = 0
    contador = 0
    for personaje in lista_personajes:
        if personaje["genero"] == "M":
            altura = personaje["altura"]
            altura = int(float(altura))
            acumulador += altura
            contador += 1
        if contador > 0:
            promedio = acumulador / contador

    print(f"El promedio de altura es de los héroes M es{promedio}")

calculadora_promedio()
#H
def calculadora_promedio_F():
    acumulador = 0
    contador = 0
    for personaje in lista_personajes:
        if personaje["genero"] == "F":
            altura = personaje["altura"]
            altura = int(float(altura))
            acumulador += altura
            contador += 1
        if contador > 0:
            promedio = acumulador / contador

    print(f"El promedio de altura es de las heroínas es{promedio}")

calculadora_promedio_F()
#I
def punto_i():
    print("Funcion principal que llama a las otras")
    punto_c()
    punto_d()
    punto_e()
    punto_f()
    calculadora_promedio()
    calculadora_promedio_F()

punto_i()
#J
def contar_colores_ojos(lista_personajes):
    recuento_colores_ojos = {}

    for personaje in lista_personajes:
        color_ojos = personaje.get("color_ojos", "Desconocido")
        if color_ojos in recuento_colores_ojos:
            recuento_colores_ojos[color_ojos] += 1
        else:
            recuento_colores_ojos[color_ojos] = 1

    for color, cantidad in recuento_colores_ojos.items():
        print(f"{cantidad} superhéroes tienen color de ojos {color}")


contar_colores_ojos(lista_personajes)
#K
def contar_color_pelo(lista_personajes):
    recuento_color_pelo = {}

    for personaje in lista_personajes:
        color_pelo = personaje.get("color_pelo","No Hair")
        if color_pelo in recuento_color_pelo:
            recuento_color_pelo[color_pelo] +=1
        else:
            recuento_color_pelo[color_pelo] = 1
        
    
    for color, cantidad in recuento_color_pelo.items():
        print(f"{cantidad} superheroes tienen color de pelo {color}")

contar_color_pelo(lista_personajes)
#L
def contar_inteligencia(lista_personajes):
    recuento_inteligencia = {}

    for personaje in lista_personajes:
        inteligencia = personaje.get("inteligencia", "No Tiene")
        if inteligencia in recuento_inteligencia:
            recuento_inteligencia[inteligencia] += 1
        else:
            recuento_inteligencia[inteligencia] = 1

    for inteligencia, cantidad in recuento_inteligencia.items():
        print(f"{cantidad} superhéroes tienen inteligencia: {inteligencia}")


contar_inteligencia(lista_personajes)
#M
def listar_superheroes_por_color_ojos(lista_personajes):
    superheroes_por_color_ojos = {}

    for personaje in lista_personajes:
        color_ojos = personaje.get("color_ojos")
        if color_ojos in superheroes_por_color_ojos:
            superheroes_por_color_ojos[color_ojos].append(personaje)
        else:
            superheroes_por_color_ojos[color_ojos] = [personaje]

    for color_ojos, superheroes in superheroes_por_color_ojos.items():
        print(f"Color de ojos: {color_ojos}")
        for superheroe in superheroes:
            print(f"  - {superheroe['nombre']}")


listar_superheroes_por_color_ojos(lista_personajes)
#N
def contar_personas_por_color_pelo(lista):
    conteo_por_color = {}
    for personaje in lista:
        color_pelo = personaje.get("color_pelo")
        if color_pelo == "":
            color_pelo = "no hair"

        if color_pelo in conteo_por_color:
            conteo_por_color[color_pelo] += 1
        else:
            conteo_por_color[color_pelo] = 1

    for color, cantidad in conteo_por_color.items():
        print(f"Personas con pelo de color {color}: {cantidad}")

contar_personas_por_color_pelo(lista_personajes)
#O
def listar_superheroes_por_tipo_inteligencia(lista_personajes):
    superheroes_por_tipo_inteligencia = {}

    for personaje in lista_personajes:
        tipo_inteligencia = personaje.get("inteligencia", "Desconocido")
        if tipo_inteligencia in superheroes_por_tipo_inteligencia:
            superheroes_por_tipo_inteligencia[tipo_inteligencia].append(personaje)
        else:
            superheroes_por_tipo_inteligencia[tipo_inteligencia] = [personaje]

    for tipo_inteligencia, superheroes in superheroes_por_tipo_inteligencia.items():
        print(f"Tipo de inteligencia: {tipo_inteligencia}")
        for superheroe in superheroes:
            print(f"  - {superheroe['nombre']}")

listar_superheroes_por_tipo_inteligencia(lista_personajes)
