import random
user_point=0
enter_level=input("enter level from Easy,Medium,Hard : ").lower()
if (enter_level=="easy"):
    print("*********easy level**********")
    computer=random.randint(1,11)
    count=5
    for i in range(5):
        user=int(input("enter the guessed number"))
        if(0<user<11):
            if(user==computer):
                user_point+=10
                print("you guessed wright")
                print("your score is",user_point)
                count-=1
                break
            else:
                if user_point==0:
                    print("you guessed wrong")
                    print("your score is 0")
                    count-=1
                    print(f"you have {count} chances left")
                    if(count==0):
                        print("Computer's choice was",computer)
                else:
                    user_point-=5
                    print("you guessed wrong")
                    count-=1
                    print(f"you have {count} chances left")
                    if(count==0):
                        print("Computer's choice was",computer)
        else:
            print("choose a number between 1 to 10")
            
elif(enter_level=="medium"):
    print("*********medium level**********")
    print("Choose a number from 1-10")
    computer=random.randint(1,51)
    count=3
    for i in range(3):
        user=int(input("enter the guessed number"))
        count-=1
        if(0<user<50):
            if(user==computer):
                user_point+=10
                print("you guessed wright")
                print("your score is",user_point)
                break
            else:
                if user_point==0:
                    print("you guessed wrong")
                    print("your score is 0")
                    print(f"You have {count} chances left")
                    if(count==0):
                        print("Computer's choice was",computer)
                else:
                    user_point-=5
                    print("you guessed wrong")
                    print(f"You have {count} chances left")
                    if(count==0):
                        print("Computer's choice was",computer)
        else:
            print("choose a number between 1 to 50")
elif(enter_level=="hard"):
    count=10
    print("*********hard level**********")
    print("Guess a number from 1 and 2 ('YOU HAVE 10 CHANCES')")
    avail=[1,2]
    computer=random.choice(avail)
    for i in range(10):
        user=int(input("enter the guessed number"))
        count-=1
        if(0<user<2):
            if(user==computer):
                avail.remove(user)
                computer=random.choice(avail)
                user_point=0
                print("you guessed wrong")
                print("your score is",user_point)
                avail.append(user)
                print(f"You have {count} chances left")
            else:
                if user_point==0:
                    print("you guessed wrong")
                    print("your score is 0")
                    print(f"You have {count} chances left")
                else:
                    user_point-=5
                    print("you guessed wrong")
                    print("your score is",user_point)
                    print(f"You have {count} chances left")
        else:
            print("choose a number between 1 to 2")
else:
        print("Invalid level entered. Defaulting to Easy.")
        enter_level="easy"
        if (enter_level=="easy"):
            print("*********easy level**********")
            print("Choose a number from 1-10")
            computer=random.randint(1,11)
            count=5
            for i in range(5):
                user=int(input("enter the guessed number"))
                count-=1
                if(0<user<11):
                    if(user==computer):
                        user_point+=10
                        print("you guessed wright")
                        print("your score is",user_point)
                        break
                    else:
                        if user_point==0:
                            print("you guessed wrong")
                            print("your score is 0")
                            print(f"You have {count} chances left")
                            if(count==0):
                                print("Computer's choice was",computer)
                        else:
                            user_point-=5
                            print("you guessed wrong")
                            print(f"You have {count} chances left")
                            if(count==0):
                                print("Computer's choice was",computer)
                else:
                    print("ERROR choose a number between 1 to 10")
