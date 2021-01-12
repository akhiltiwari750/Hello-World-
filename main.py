from time import sleep
from random import randrange as rand


def print_string(current_string, expected_character):
  some_random_character = rand(0,127)
  while True:
    print("\r" + current_string + chr(some_random_character), end="")
    sleep(0.5) # comment it for instant result
    if chr(some_random_character) == expected_character:
      break
    some_random_character = rand(0,127)

my_string = "Hello World"
current_str = ""

for letter in my_string:
  print_string(current_str,letter)
  current_str += letter
