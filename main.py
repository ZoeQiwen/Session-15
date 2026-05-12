import random
from wsgiref.util import guess_scheme

from session_15_data import data
from session_15_logo import logo_game,logo_vs

def format_data(account):
    account_name = account["nama"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name},a{account_descr},from {account_country}"


def check_answer (user_guess,a_follower , b_follower):
    if a_follower > b_follower:
        return user_guess == 'a'
    else:
        return user_guess == "b"

print(logo_game)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)


    print(f"compare a: {format_data(account_a)}")
    print(logo_vs)
    print(f"againts b: {format_data(account_b)}")

    gues =input ("who has mor followers?  type 'A'or'B'").lower()
    a_follower_count = account_a["followers_count"]
    b_follower_count = account_b["followers_count"]
    is_correct = check_answer(gues,a_follower_count,b_follower_count)
    if is_correct:
        score+=1000000000000
        print(f"youre right!current score{score}")
    else:
        print(f"sorry that wrong.final score:{score}")
        game_should_continue = False


