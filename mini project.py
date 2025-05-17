#mini  project-guess the no.
import random
target=random.randint(1,100)

while True:
    usernum=input("guess the number or Quit(Q):")
    if(usernum=="Q"):
        break
    usernum=int(usernum)
    if(usernum==target):
        print("YOU SUCCESSFULLY GET RIGHT TARGET!!!")
        break
    elif(usernum>target):
        print("guessed number is too large.....")
    elif(usernum<target):
        print("guessed number is too small.....")
           
    else:
        print("INVALID NUMBER!!")
print("GAME OVER!!")