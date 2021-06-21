import random
name=['apple','mango','orange','banana','papaya','guava']
chosen=random.choice(name)
print("Start the game!,you can guess any fruit ,you have 3 chances")
for guesses in range(1,4):
    print('Take a guess')
    guess=input()
    if guess!=chosen:
        print("you guessed it wrong!,try again ")
    else:
        break
if guess==chosen:
    print("Great,you guessed it right in " +str(guesses) +" guesses!")
else:
    print("Nope your chance is over,I was thinking " + str(chosen)) 
