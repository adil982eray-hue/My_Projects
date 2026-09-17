# import the random module
import random

# create subjects
subjects = [
    "sharukh khan",
    "virat kohli",
    "imran khan",
    "Amir khan",
    "chunaid khan",
    "A group of monkeys",
    "Auto rickshaw driver from delhi"
]

actions = [
    "Launches",
    "Cancels",
    "dance with",
    "eats",
    "declare war on",
    "orders",
    "celebrates"
]

place_or_things = [
    "at red fort",
    "in peshawar BRT",
    "a plate of peshawari chawal",
    "inside parliment",
    "at pc hotel",
    "during psl match",
    "at khyber gate"
]

#start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing} "
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower
    if user_input == "no":
        break

    #print goodbye message

    ("\nThanks for using the fake news headline generator. Have fun")
