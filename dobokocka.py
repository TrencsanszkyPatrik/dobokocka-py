
import random
  
  
x = "y"
   
while x == "y":

    no = random.randint(1,6)
      
    if no == 1:
        print("-------")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("-------")
        print("\n")
        print("Egyet dobtál!")
        
    if no == 2:
        print("-------")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("-------")
        print("\n")
        print("Kettőt dobtál!")

    if no == 3:
        print("-------")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("-------")
        print("\n")
        print("Hármat dobtál!")


    if no == 4:
        print("-------")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("-------")
        print("\n")
        print("Négyet dobtál!")

    if no == 5:
        print("-------")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("-------")
        print("\n")
        print("Ötöt dobtál!")

    if no == 6:
        print("-------")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("-------")
        print("\n")
        print("Hatot dobtál!")
          
    x=input("Nyomd meg az y-t hogy újradobj, vagy pedig lépj ki az n betűvel:")
    print("\n")