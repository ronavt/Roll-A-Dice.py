
import  random

value = 0
response = input("Enter y to roll a dice and n to exit : ")
if(response == 'y'):
    value += 1

while response == 'y':
    no = random.randint(1,6)
    if(no == 1):
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        response = input("Enter y to roll a dice and n to exit : ")
    elif(no == 2):
        print("[-----]")
        print("[     ]")
        print("[ 0 0 ]")
        print("[     ]")
        print("[-----]")
        response = input("Enter y to roll a dice and n to exit : ")
    elif(no == 3):
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
        response = input("Enter y to roll a dice and n to exit : ")
    elif(no == 1):
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
        response = input("Enter y to roll a dice and n to exit : ")
    elif(no == 1):
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
        response = input("Enter y to roll a dice and n to exit : ")
    else:
        print("[-----]")
    
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")
        response = input("Enter y to roll a dice and n to exit : ")

if(response == 'n'):
     if(value == 1):
      print("Thanks for rolling!")
     else:
        print("Roll next time")
    