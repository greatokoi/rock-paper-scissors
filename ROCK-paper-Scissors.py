import random
print("WELCOME TO ROCK, PAPER AND SCISSORS")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

items = [rock, paper, scissor]

def compare(u_guess,c_guess,u_score,c_score):
    if u_guess == c_guess:
        print("It's a Tie!!")
    elif u_guess == 0 and c_guess == 2:
        print("You Win!!")
        u_score += 1
    elif c_guess == 0 and u_guess == 2:
        print("You Lose")
        c_score += 1
    elif u_guess > c_guess:
        print("You Win!!")
        u_score += 1
    elif c_guess > u_guess:
        print("You Lose!!")
        c_score += 1
    else:
        print("Invalid input")

    return u_score, c_score


continue_playing = True
u_point = 0
c_point = 0
while continue_playing:
    u_guess = int(input("Enter your choice\nType 0 for rock\n1 for paper\n2 for scissors: "))

    if u_guess >= 0 and u_guess <= 2:
        print(f"You guessed:\n{items[u_guess]}")


    c_guess = random.randint(0,2)
    print(f"Computer guessed:\n{items[c_guess]}")

    u_point, c_point = compare(u_guess,c_guess, u_point, c_point)

    should_continue = input("Do you want to keep Playing 'y' or 'n': ").lower()
    if should_continue == "y":
        compare(u_guess,c_guess, u_point, c_point)
    elif should_continue == "n":
        continue_playing = False
        print(f"Your score is {u_point}, the computer's score is {c_point}")

    else:
        print("Invalid Input")
