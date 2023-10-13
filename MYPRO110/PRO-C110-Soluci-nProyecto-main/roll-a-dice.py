import random 
  
# Toma una variable para almacenar la respuesta para seguir tirando un dado
response = "y"
   
while response == "y": 
      
    # Genera un numero aleatorio
    # entre el 1 y 6 (incluyendo
    # también el 1 y 6) 
    no = random.randint(1,6) 

    # condiciones para comprobar el valor del número
    if no == 1: 
        print("[-----]") 
        print("[     ]") 
        print("[  0  ]") 
        print("[     ]") 
        print("[-----]") 
    if no == 2: 
        print("[-----]") 
        print("[ 0   ]") 
        print("[     ]") 
        print("[   0 ]") 
        print("[-----]") 
    if no == 3: 
        print("[-----]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[-----]") 
    if no == 4: 
        print("[-----]") 
        print("[0   0]") 
        print("[     ]") 
        print("[0   0]") 
        print("[-----]") 
    if no == 5: 
        print("[-----]") 
        print("[0   0]") 
        print("[  0  ]") 
        print("[0   0]") 
        print("[-----]") 
    if no == 6: 
        print("[-----]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[-----]") 
          
    # Pide al usuario que introduzca una respuesta     
    response=input("presiona y para rodar de nuevo, presiona n para salir:") 
    print("\n") 
