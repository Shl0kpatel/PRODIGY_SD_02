import random
def user_guide():
  """
  Prints a user guide explaining the game rules and feedback mechanism.
  """
  print("""
Welcome to the Number Guessing Game!

This game will generate a random number between 1 and 100 (inclusive).
Your goal is to guess the number in the fewest attempts possible.

Here's how to play:

1. You'll be prompted to enter your guess.
2. The game will provide feedback based on your guess:
   - **Correct guess:** Congratulations! The game will display the number of tries it took you to guess correctly.
   - **Too high:** Your guess is significantly higher than the secret number.
   - **High:** Your guess is higher than the secret number, but not by a large amount (within 10 of the number).
   - **Too low:** Your guess is significantly lower than the secret number.
   - **Low:** Your guess is lower than the secret number, but not by a large amount (within 10 of the number).
3. You can keep guessing until you get the correct number.

Try your best and see how many attempts it takes you!
""")


user_guide()
num = random.randrange(1,100)
count = 0

while True:
    x = int(input("Enter your guess: "))
    count += 1
    if x == num:
        print("You have guess the correct number")
        break
        
    elif x > num :
        diff = x - num
        if diff > 10 :
            print("Your guess is too high")
        else:
            print("Your guess is high")
            
    else :
        diff = num - x
        if diff > 10 :
            print("Your guess is too low")
        else:
            print("Your guess is low")

print(f"You have taken total {count} guesses")