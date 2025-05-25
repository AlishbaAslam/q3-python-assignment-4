# Mad Libs Game in Python

print("Welcome to the Mad Libs Game!")
print("Fill in the blanks below to create your funny story.\n")

# Getting input from user
name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb ending in -ing: ")
food = input("Enter a type of food: ")
emotion = input("Enter an emotion: ")

# Mad Libs story template
story = f"""
One day, {name} went to {place}. On the way, {name} saw a {adjective} {animal}.
It was {verb} while eating {food}! {name} felt very {emotion} and decided to join the fun.
It was the craziest day ever!
"""

# Printing the story
print("\nHere's your Mad Libs story:\n")
print(story)