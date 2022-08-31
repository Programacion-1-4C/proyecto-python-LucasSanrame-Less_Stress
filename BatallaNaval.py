from random import sample
def Menu_j():
    import Menu
def no_paso():
  print("*nada paso*")
def hundido():
  print("*EXPLOCION*")
print("Hola, bienvenido a Batalla naval")
print()
#respuesta_1 = input("¿Quieres empezar un juego nuevo?: -" )
respuesta_1 = input("¿Quieres jugar batalla naval?: -")
if respuesta_1 == "si":
    while respuesta_1 == "si":
     dificultad = print("Como dificultad tienes: Facil, Medio, Dificil y Locura")
     seleccion_de_dificultad = input("¿Cual quieres elegir? -")
     if seleccion_de_dificultad == "facil": 
        posiciones = {}
        barcos_restantes = 40
        for i in "abcdefghij":
         for j in range(1, 11):
           posiciones[f"{i}{j}"] = f"barco"
        d = sample(list(posiciones), 40)
        print(d)
        while barcos_restantes != 0:
         seleccion = input("Seleccione un cuadrante entre el a1 y el j10: -")
         if seleccion in d:
           hundido()
           print(posiciones[d[0]])
           barcos_restantes -= 1
           if barcos_restantes == 0:
               print("Gracias por jugar")
               respuesta_1 = input("¿Quieres jugar otra vez? -")
         else:
           no_paso()
     if seleccion_de_dificultad == "medio":
        posiciones = {}
        barcos_restantes = 20       
        for i in "abcdefghij":
            for j in range(1, 11):
              posiciones[f"{i}{j}"] = f"barco"
        d = sample(list(posiciones), 20)
        print(d)
        while barcos_restantes != 0:
           seleccion = input("Seleccione un cuadrante entre el a1 y el j10: -")
           if seleccion in d:
             hundido()
             print(posiciones[d[0]])
             barcos_restantes -= 1
             if barcos_restantes == 0:
                 print("Gracias por jugar")
                 respuesta_1 = input("¿Quieres jugar otra vez? -")
           else:
             no_paso()
     if seleccion_de_dificultad == "dificil":
        posiciones = {}
        barcos_restantes = 10
        for i in "abcdefghij":
            for j in range(1, 11):
              posiciones[f"{i}{j}"] = f"barco"
        d = sample(list(posiciones), 10)
        print(d)
        while barcos_restantes != 0:
           seleccion = input("Seleccione un cuadrante entre el a1 y el j10: -")
           if seleccion in d:
             hundido()
             print(posiciones[d[0]])
             barcos_restantes -= 1
             if barcos_restantes == 0:
                 print("Gracias por jugar")
                 respuesta_1 = input("¿Quieres jugar otra vez? -")
           else:
              no_paso()
     if seleccion_de_dificultad == "locura":
        posiciones = {}
        barcos_restantes = 5
        for i in "abcdefghij":
             for j in range(1, 11):
               posiciones[f"{i}{j}"] = f"barco"
        d = sample(list(posiciones), 5)
        print(d)
        while barcos_restantes != 0:
           seleccion = input("Seleccione un cuadrante entre el a1 y el j10: -")
           if seleccion in d:
             hundido()
             print(posiciones[d[0]])
             barcos_restantes -= 1
             if barcos_restantes == 0:
                 print("Gracias por jugar")
                 respuesta_1 = input("¿Quieres jugar otra vez? -")
           else:
              no_paso()
else:
  print("Que tenga un buen dia")
  Menu_j()