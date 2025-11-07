import random

# Generate a random integer between 1 and 10
random_int = random.randint(1, 10)
print(f"Random integer (1-10): {random_int}")

# Generate a random float between 0 and 1
random_float = random.random()
print(f"Random float (0-1): {random_float}")

# Generate a random float in a specific range
random_range = random.uniform(5.0, 10.0)
print(f"Random float (5-10): {random_range}")

# Choose a random item from a list
colors = ['red', 'blue', 'green', 'yellow']
random_color = random.choice(colors)
print(f"Random color: {random_color}")

# Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")
