import random

n = 4

gold= random.randint(1,n)

tiger= random.randint(1,n)

while gold == tiger:
    gold= random.randint(1,n) 
y = 1

##gold = 7
##tiger = 8

while y < 4:
    x = 1 
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
        x = x+1
        print("There is nothing behind the door! Choose again")
        door = enterDoor()
    if door == gold:
        print("Congradulations, you've found gold! Number of tries:" + str(x))
    elif door == tiger:
        print("Oh no, you got eaten! Number of tries:" + str(x))
        y= y+1

print("You can't play anymore!")
