print("Welcome to the Only Fools and Horses Quiz")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay lets play!")

#### These are the Only Fools and Horses Quiz Questions.(They need to be answered in lower case.
score = 0
##1
answer = input("What name did Trigger call Rodney? ")
if answer.lower() == "dave":
    print("Correct!")
    score += 1
else:
    print("Incorrect!  He called him Dave!")
##2
answer = input("Whats Grandads favorite food? ")
if answer.lower() == "hamburgers":
    print("Correct!")
    score += 1
else:
    print("Incorrect! It was hamburgers!")
##3
answer = input("What was Del and Rodney's Surname? ")
if answer.lower() == "trotter":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The Brothers Surname was Trotter! ")
##4
answer = input("How many wheels did the trotters van have? ")
if answer.lower() == "3":
    print("Correct!")
    score += 1
else:
    print("Incorrect! It was a 3 wheel van!")
##5
answer = input("How many episodes of ONLY FOOL AND HORSES were made? ")
if answer.lower() == "64":
    print("Correct!")
    score += 1
else:
    print("Incorrect! There were total of 64 episodes!")
##6
answer = input("Who wrote Only Fools and Horses? ")
if answer.lower() == "john sullivan":
    print("Correct!")
    score += 1
else:
    print("Incorrect! It was John Sullivan ")c
##7
answer = input("Who did John Sullivan based Rodney on ")
if answer.lower() == "his brother":
    print("Correct!")
    score += 1
else:
    print("Incorrect! His own brother")
##8
answer = input("What was Denzil's wife called? ")
if answer.lower() == "corrie":
    print("Correct!")
    score += 1
else:
    print("Incorrect! her name was corrie! ")
##9
answer = input("What part of the Armed forces was Albert a member off? ")
if answer.lower() == "navy":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Albert was in the Navy!")
##10
answer = input("What part of London was Only Fools and Horses set? ")
if answer.lower() == "peckham":
    print("Correct!")
    score += 1
else:
    print("Incorrect!It was Peckham! ")

print("You answered " + str(score) + " questions correct!")
print("You answered " + str((score / 10) *100) + "%")







