import random


def generate(size, success_probability):
    bernoulli_array = []
    for i in range(size):
        value = random.uniform(0, 1)
        if success_probability - value < 0.0000001:
            value = 0
        else:
            value = 1
        bernoulli_array.append(value)
