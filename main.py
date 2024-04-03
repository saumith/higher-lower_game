import random
from art import logo, vs
from game_data import data
from replit import clear

print(logo)

def format_data(data):
    """Format the data to display name, description, and country."""
    return f"{data['name']}, a {data['description']}, from {data['country']}"

def game():
    score = 0
    compare_A = random.choice(data)

    while True:
        Against_B = random.choice(data)
        while Against_B == compare_A:
            Against_B = random.choice(data)

        print(f"Compare A: {format_data(compare_A)}")
        print(vs)
        print(f"Against B: {format_data(Against_B)}")

        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
        if (user_input == "a" and compare_A["follower_count"] > Against_B["follower_count"]) or (user_input == "b" and 
           Against_B["follower_count"] > compare_A["follower_count"]):
            score += 1
            print(f"You're right! Current score: {score}")
            compare_A = Against_B
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return
        input("Press Enter to continue...")
        clear()

game()
