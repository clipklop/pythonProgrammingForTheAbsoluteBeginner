###
# Chapter 05
# Task 01: Print random ordered list without repeating.
###
import random

WORDS = ["Senya", "Vitalya", "Natasha", "Katya", "Nastya", "Misha", "Gosha", "Gosha", "Misha"]
random.shuffle(WORDS)

words_list = []

for word in WORDS:
    if word not in words_list:
        words_list.append(word)

print(words_list)
