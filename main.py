from rooms import Room
from npcs import NPC
from weapons import Weapon
from solution import Solution
from threading import Thread

import tkinter as tk
import random

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

cards = []

gherahyme = NPC("Gherahyme")
bertrum = NPC("Bertrum")
anastasia = NPC("Anastasia")
gherahyme.set_opener("Oh well hello there my esteemed friend.")
bertrum.set_opener("Umm... wha' d'ya want?")
anastasia.set_opener("Hmm. I'm not the detective here but I know you murdered that outfit.")

knife = Weapon("Knife")
gun = Weapon("Gun")
lead_pipe = Weapon("Lead Pipe")
candlestick = Weapon("Candlestick")
rope = Weapon("Rope")
spanner = Weapon("Spanner")
axe = Weapon("Axe")

cards.append(knife)
cards.append(gun)
cards.append(lead_pipe)
cards.append(candlestick)
cards.append(rope)
cards.append(spanner)
cards.append(axe)
cards.append(kitchen)
cards.append(l_room)
cards.append(bathroom)
cards.append(bedroom)
cards.append(hallway)
cards.append(gherahyme)
cards.append(bertrum)
cards.append(anastasia)

answer_cards = []
answer_cards.append(Weapon.instances[random.randint(0, len(Weapon.instances) - 1)])
answer_cards.append(Room.instances[random.randint(0, len(Room.instances) - 1)])
answer_cards.append(NPC.instances[random.randint(0, len(NPC.instances) - 1)])
for i in answer_cards:
    cards.remove(i)

game_answers = Solution(answer_cards)

NPCtempList = ["None", "None"]
NPCtempList.extend(NPC.instances)


def setCharRooms(room, NPCtempList):
    ch = random.choice(NPCtempList)
    room.set_character(ch)
    NPCtempList.remove(ch)


setCharRooms(kitchen, NPCtempList)
setCharRooms(l_room, NPCtempList)
setCharRooms(hallway, NPCtempList)
setCharRooms(bathroom, NPCtempList)
setCharRooms(bedroom, NPCtempList)


def deal_cards(player, cards):
    dealt_cards = random.sample(cards, 3)
    player.set_cards(dealt_cards)
    for card in dealt_cards:
        cards.remove(card)


deal_cards(gherahyme, cards)
deal_cards(bertrum, cards)
deal_cards(anastasia, cards)

(random.choice(NPC.instances)).set_liar()

# Beginning
print("""
 ▄████████  ▄█        ▄██████▄   ▄██████▄     ▄███████▄  ▄██████▄  
███    ███ ███       ███    ███ ███    ███   ███    ███ ███    ███ 
███    █▀  ███       ███    ███ ███    ███   ███    ███ ███    ███ 
███        ███       ███    ███ ███    ███   ███    ███ ███    ███ 
███        ███       ███    ███ ███    ███ ▀█████████▀  ███    ███ 
███    █▄  ███       ███    ███ ███    ███   ███        ███    ███ 
███    ███ ███▌    ▄ ███    ███ ███    ███   ███        ███    ███ 
████████▀  █████▄▄██  ▀██████▀   ▀██████▀   ▄████▀       ▀██████▀  
           ▀                                                       
""")
print("Welcome to clOOPo!\nIn this thrilling game, you play the role of a detective, solving the murder of Estelle "
      "Montclaire.")
print("You must talk to the residents of the Montclaire Mansion, clawing clues from each of them to uncover the "
      "truth.\nBut watch out! Someone may be trying to cover up their own secrets and tell you lies.\nGood luck!")
print("--------------------------------------------")

# Starting Room
current = hallway
current.describe()

# Sheet window
root = None


def open_window():
    def create_window():

        def on_text_widget_key(event):
            if event.keysym == "BackSpace":
                handle_backspace(event.widget)
            else:
                insert_text_with_colour(event.widget, event.char)
            return "break"

        def insert_text_with_colour(text_widget, char):
            current_colour = colour_var.get()
            text_widget.insert(tk.INSERT, char, current_colour)

        def handle_backspace(text_widget):
            text_widget.delete("insert-1c", tk.INSERT)

        def setup_text_widget(text_widget):
            for colour in colours:
                text_widget.tag_configure(colour, foreground=colour)

        root = tk.Tk()
        root.title("Grid of Textboxes")

        columns = ["Me", "Gherahyme", "Bertrum", "Anastasia"]
        rows = ["Gherahyme", "Bertrum", "Anastasia", "Hallway", "Kitchen", "Bedroom", "Bathroom", "Living Room", "Gun",
                "Knife", "Lead Pipe", "Candlestick", "Rope", "Spanner", "Axe"]

        colours = ['Black', 'Red', 'Blue']
        colour_var = tk.StringVar(root)
        colour_var.set(colours[0])
        colour_menu = tk.OptionMenu(root, colour_var, *colours)
        colour_menu.grid(row=0, column=0, sticky="nsew")

        for i, column in enumerate(columns, start=1):
            label = tk.Label(root, text=column, borderwidth=2, relief="groove")
            label.grid(row=0, column=i, sticky="nsew")

        for i, row in enumerate(rows, start=1):
            label = tk.Label(root, text=row, borderwidth=2, relief="groove")
            label.grid(row=i, column=0, sticky="nsew")

        for i in range(1, len(rows) + 1):
            for j in range(1, len(columns) + 1):
                text_widget = tk.Text(root, height=1, width=20)
                text_widget.grid(row=i, column=j, sticky="nsew")
                setup_text_widget(text_widget)
                text_widget.bind("<Key>", on_text_widget_key)

        for i in range(len(columns) + 1):
            root.grid_columnconfigure(i, weight=1)

        for i in range(len(rows) + 1):
            root.grid_rowconfigure(i, weight=1)

        root.mainloop()

    Thread(target=create_window).start()


open_window()

while True:
    print("--------------------------------------------")
    print("Your clues:")
    for i in cards:
        print(i.get_name())
    print("\n'Help' for list of instructions.\n")
    choice = input("What do you do?").title()
    print("--------------------------------------------")
    if choice == "Help":
        print("\nTo move, enter compass directions as stated.\n'Talk' to speak to character in room.\n'Accuse' to "
              "make your final guesses and end the game.")
        print("\n--------------------------------------------")
    elif choice == "Talk":
        if current.character == "None":
            print("No one is here.\n")
        else:
            # Below for testing. Prints character's cards before guessing
            # for i in current.character.cards:
            # print(i.get_name())
            current.character.talk()
            pass
    elif choice == "Accuse":
        # Below for testing. Prints game answers before guessing
        # for i in game_answers.answers:
        # print(i.get_name())
        game_answers.accuse()
    else:
        current = current.move(choice)
    current.describe()
