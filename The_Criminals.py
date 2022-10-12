import random
def Menu_j():
    import Menu
vida_enemigo= 500
hola = input("¿Quieres jugar? -")
def opciones():
    print("ATACAR / SALUD")
def fallo():
    print("Fallaste")
def dar():
    print("Le diste")
salud_principal = 300
if hola == "si":
  while hola == "si":
      opciones()
      desicion_1 = input("¿Que vas a hacer ahora? -")
      if desicion_1 == "atacar":
         golpe = ["Dar golpe", "No dar el golpe"]
         dar_golpe = random.choice(golpe)
         if dar_golpe == "Dar golpe": 
             vida_enemigo -= 30
             dar()
             print(vida_enemigo)
         else:
             fallo()
         enemigo_golpe = True
         enemigo_acierta = ["si", "no"]
         enemigo_s = random.choice(enemigo_acierta)
         print("Te atacara tu enemigo")
         if enemigo_s == "si":
              eleccion_2 = input("Esquivaras el ataque? -")
              if eleccion_2 == "si":
                 esquivar2 = ["si", "no"]
                 esquivar = random.choice(esquivar2)
                 if esquivar == "si":
                     print("nada paso")
                 if esquivar == "no":
                     salud_principal -= 50
                     print("Te dio")
                     print(salud_principal)
              if eleccion_2 == "no":
                 salud_principal -= 50
                 print("Te dio")
                 print(salud_principal)
         else:
              print("No pasa nada")
         if salud_principal == 0:
              hola = input("Quieres jugar denuevo? -")
      if desicion_1 == "salud":
          if enemigo_golpe == "False":
              print(salud_principal)
          else:
              print(salud_principal)
          enemigo_acierta = ["si", "no"]
          enemigo_s = random.choice(enemigo_acierta)
          if enemigo_s == "si":
              salud_principal -= 50
              print("Te dio")
              print(salud_principal)
          else:
              print("No pasa nada")
          if salud_principal == 0:
              hola == input("Quieres jugar denuevo? -")
if hola == "no":
    print("Que tenga un buen dia")
    Menu_j()
