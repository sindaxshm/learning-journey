import random

def choice():
    while True:
        user_input = input("Enter rock, paper, or scissors: ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid input. Please try again.")

def winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    user = choice()
    computer = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer}")
    result = winner(user, computer)
    print(result)
    return result 

def main():
    user_score = 0
    computer_score = 0
    rounds = 0
    while user_score < 2 and computer_score < 2 and rounds < 3:
        result = play()
        if "You win!" in result:
            user_score += 1
        elif "Computer wins!" in result:
            computer_score += 1
        rounds += 1
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif computer_score > user_score:
        print("The computer wins the game!")
    else:
        print("The game is a draw!")      

if __name__ == "__main__":
    main()