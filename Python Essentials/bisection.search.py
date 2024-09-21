print("Please think of a number between 0 and 100!")

low = 0 
high = 100

while True:
    guess = (low + high) // 2  # Bisection guess (integer division)
    print("Is your secret number {}?".format(guess))
    
    # Get user input
    user_input = input("Enter 'h' for too high, 'l' for too low, 'c' if correct: ")
    
    # Handle different cases
    if user_input == 'h':
        # Guess is too high, adjust the high bound
        high = guess
    elif user_input == 'l':
        # Guess is too low, adjust the low bound
        low = guess
    elif user_input == 'c':
        # Correct guess
        print("Game over. Your secret number was {}.".format(guess))
        break
    else:
        # Invalid input, prompt again
        print("Sorry, I did not understand your input.")
