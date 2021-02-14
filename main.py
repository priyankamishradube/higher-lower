from replit import clear
import random
from art import logo,vs
from game_data import data
continue_play = True

def pick_card():
  card_index = random.randint(0,len(data)-1)
  return data[card_index]

def compare(option_a, option_b):
  if option_a['follower_count'] > option_b['follower_count']:
    return "A"
  elif option_b['follower_count'] > option_a['follower_count']:
    return "B"

def play_game():
  print(logo)
  score = 0
  while continue_play:
    def add_score(score):
      score = score + 1
      return score
    option_a = pick_card()
    option_b = pick_card()
    print(f"Compare A: {option_a['name']}, a {option_a['description']},from {option_a['country']}")
    print(vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']},from {option_b['country']}")

    user_guess = input("Who has more followers? A or B ")
    clear()
    print(logo)
    if user_guess == compare(option_a,option_b):
      score = score + 1
      print(f"You guessed correctly! Your score is {score}")
    else:
      print(f"Sorry that's wrong. Final score is {score}")
      continue_play == False

play_game()
