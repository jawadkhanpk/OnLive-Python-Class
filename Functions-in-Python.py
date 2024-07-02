# def my_function():
#     print("Statement1")
#     print("Statement2")
#     print("Statement3")
#     print("Statement4")
#     print("Statement5")
#
# my_function()
import random

def toss():
    coin_flip = random.randint(0,1)

    if coin_flip == 0:
        print("You have gotten Heads")
    elif coin_flip == 1:
        print("You have gotten Tails")


toss()