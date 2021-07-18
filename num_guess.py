from random import randint
chance = 5
num = randint(1, 100)
#num = []
#while len(num) < 10:
#    numint = randint(0, 51)
#    num.append(numint)

while chance > 0:
    guess = int(input("guess: "))
    chance -= 1
    diff = abs(guess - num)
    if guess == num and chance != 0:
        print("guessed correctly :)")
        print("Chances left: {}".format(chance))
        break
    elif guess > num and chance != 0:
        if diff <= 20:
            print("Wrong!! But you are close. Guess lower!")
            print("Chances left: {}".format(chance))
        else:
            print("guessed incorrectly :(")
            print("Chances left: {}".format(chance)) 
    elif guess <= num and chance != 0:
        if diff < 20:
            print("Wrong!! But you are close. Guess higher!")
            print("Chances left: {}".format(chance))
        else:
            print("guessed incorrectly :(")
            print("Chances left: {}".format(chance)) 
    else:
        print("guessed incorrectly :(")
        print("Chances left: {}".format(chance))
