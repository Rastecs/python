""" If there are 23 students in your class, what are the chances that two of you have the same birthday? You can estimate this probability by generating random samples of 23 birthdays and checking for matches. Hint: you can generate random birthdays with the randint function in the random module."""
import random

def has_duplicates(lst):
    return len(lst) != len(set(lst))

def generate_birthdays(n):
    birthdays = []
    for i in range(n):
        birthday = random.randint(1, 365)
        birthdays.append(birthday)
    return birthdays

def estimate_probability(n, m):
    count = 0
    for i in range(m):
        birthdays = generate_birthdays(n)
        if has_duplicates(birthdays):
            count += 1
    probability = count / m
    return probability

n = 23
m = 10000
probability = estimate_probability(n, m)
print(f"The probability that two students in a class of {n} have the same birthday is approximately {probability:.2%}.")
