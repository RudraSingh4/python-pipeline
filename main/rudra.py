winning_number = 27
guessed_number = int(input("Enter the guess number: "))
if winning_number==guessed_number:
    print("YOU WIN !!!!")
else:
    if guessed_number<winning_number:
        print("Too Low")
    else:
        print("Too High")