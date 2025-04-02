
''' Number Guessing Game '''
import random
answer = random.randint(1, 100)
attempts = 5
for i in range(attempts):
    guess = int(input("Guess the number: "))
    if guess < answer:
        print("Too low")
    elif guess > answer:
        print("Too high")
    else:
        print("Correct number!")
        break
else:
    print("Game Over! The correct number was:", answer)