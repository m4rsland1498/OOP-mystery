from rooms import Room
from npcs import NPC

kitchen = Room("Kitchen")
l_room = Room("Living Room")
bathroom = Room("Bathroom")
bedroom = Room("Bedroom")
hallway = Room("Hallway")

k_desc = "You cautiously step into the dimly lit kitchen, where an eerie chill brushes past you."

l_desc = ("Upon entering the living room, you are immediately enveloped in an atmosphere of forgotten grandeur and "
          "intense melancholy.")

b_desc = ("You hesitantly push open the creaking door to the bathroom, revealing a scene of neglect and ghostly "
          "whispers.")

h_desc = "You step cautiously into the hallway, which stretches before you like a forgotten passage to a lone gone era."

bed_desc = "You enter the bedroom, a once sanctuary now transformed into a realm of spectral gloom."
# I do not know why pycharm won't format these paragraphs to PEP8 But I am sure not doing it manually

kitchen.set_description(k_desc)
l_room.set_description(l_desc)
bathroom.set_description(b_desc)
hallway.set_description(h_desc)
bedroom.set_description(bed_desc)

l_room.set_links("North", kitchen)
l_room.set_links("West", hallway)
bathroom.set_links("East", hallway)
bathroom.set_links("North", bedroom)
kitchen.set_links("South", l_room)
kitchen.set_links("West", hallway)
hallway.set_links("North East", kitchen)
hallway.set_links("South East", l_room)
hallway.set_links("North West", bedroom)
hallway.set_links("South West", bathroom)
bedroom.set_links("East", hallway)
bedroom.set_links("South", bathroom)

# NPCs
g_convo_dict = {"opener": "Hey, you; you're finally awake.",
                "1. I just got here?.": "Ah, my mistake. I was somewhere else.",
                "2. Who are you?": "Me? I am Gherahyme. I hired you to help with this... situation."}
g_convo_line1 = {"2. "}
gherahyme = NPC("Gherahyme")
gherahyme.set_conversation(g_convo_dict)

# Starting Room
current = hallway
current.describe()

while True:
    choice = input("What do you do?").title()
    if choice == "Help":
        print("\nTo move, enter compass directions as stated.\n")
    else:
        current = current.move(choice)
        current.describe()

# test
