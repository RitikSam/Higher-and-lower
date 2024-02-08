import random
from art import logo,vs
from game_data import data
# from replit import clear

def get_random():
    return random.choice(data)


def data_formate(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}."


def compare(guess, account_a, account_b):
    if account_a > account_b:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_continue = True
account_b = get_random()
while game_continue:

    account_a = account_b
    account_b = get_random()
    while account_a == account_b:
        account_b = get_random()

    print(f"Compare A: {data_formate(account_a)}.")
    print(vs)
    print(f"Against B: {data_formate(account_b)}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]
    ans = compare(guess, a_follower, b_follower)
    # clear()
    if ans:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")


