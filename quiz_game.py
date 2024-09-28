print("Welcome to my Computer Quiz!")

playing = input("Do you want to play? (yes/no) ").lower()

if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

# Question 1
answer = input("Is python needed to learn data science? ").lower()
if answer == "yes":
    print('Correct! 👏')
    score += 1
else:
    print("Incorrect!")

# Question 2
answer = input("Is Pakistan the only Muslim nuclear power country in the world? (yes/no) ").lower()
if answer == "yes":
    print('Correct! 👏')
    score += 1
else:
    print("Incorrect!")

# Question 3
answer = input("The world's largest deep sea port, Gwadar, is in? ").lower()
if answer == "pakistan":
    print('Correct! 👏')
    score += 1
else:
    print("Incorrect!")

# Question 4
answer = input("Which Foundation proudly runs the world’s largest volunteer ambulance service? ").lower()
if answer == "pakistan’s edhi" or answer == "edhi":
    print('Correct! 👏')
    score += 1
else:
    print("Incorrect!")

# Final score

print("**************************Final score**************************")
print("|")

print(f"You got {score}/4 questions correct!")
