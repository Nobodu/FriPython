import random

gold= random.randint(1,9)

tiger= random.randint(1,9)

while gold == tiger:
    gold= random.randint(1,9) 


##gold = 7
##tiger = 8


print("There are nine doors in front of you, and behind one of them is gold. Behind another is a tiger that will eat you.")

def enterDoor():
    print("Choose door(#between 1-9)")
    door = input()
    door = int(door)
    return door
door = enterDoor()
##if door == gold:
##    print("Congradulations, you've found gold!")
##elif door == tiger:
##    print("Oh no, you got eaten!")
while door!= gold and door!= tiger:
    print("There is nothing behind the door! Choose again")
    door = enterDoor()
if door == gold:
    print("Congradulations, you've found gold!")
elif door == tiger:
    print("Oh no, you got eaten!")
        

