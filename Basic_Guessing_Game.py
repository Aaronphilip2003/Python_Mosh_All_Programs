guess_limit=3
guess_counter=0
secret_number=8
while guess_counter<guess_limit:
    guess=int(input("Guess the number (0-9):"))
    guess_counter+=1
    if(guess==secret_number):
        print(("CORRECT!"))
        break
    else:
        print("INCORRECT!")
