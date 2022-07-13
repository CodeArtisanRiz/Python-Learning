secret_number = 6
guess_count = 0
guess_limt = 3
while guess_count < guess_limt:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won..!")
        break
    else:
        if guess_count < 3:
            print("try again..")
else:
    print("You failed...")
