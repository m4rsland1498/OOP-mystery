import random
from rooms import Room
from weapons import Weapon


class NPC:
    instances = []

    def __init__(self, npc_name):
        self.name = npc_name
        self.description = None
        self.cards = None
        self.opener = None
        self.is_liar = False
        NPC.instances.append(self)

    def get_name(self):
        return self.name

    def get_answers(self, card1, card2, card3):
        suggestions = [card1, card2, card3]
        in_similar = []
        if not self.is_liar:
            # Truth tellers' response
            for i in self.cards:
                if i.get_name() in suggestions:
                    in_similar.append(i.get_name())
            if len(in_similar) > 0:
                print("\nI know it's not this one:", random.choice(in_similar))
                print("--------------------------------------------")
            else:
                print("\nI don't know anything about that.\n")
                print("--------------------------------------------")
        else:
            # Liar's response
            in_similar.extend(suggestions)
            for i in self.cards:
                if i.get_name() in suggestions:
                    in_similar.remove(i.get_name())
            if len(in_similar) == 0:
                print("\nI don't know anything about that.\n")
                print("--------------------------------------------")
            else:
                print("\nI know it's not this one:", random.choice(in_similar))
                print("--------------------------------------------")

    def set_cards(self, cards):
        self.cards = cards

    def set_opener(self, opener):
        self.opener = opener

    def talk(self):
        while True:
            print("\n" + self.opener, "\nWhat is your suspect suggestion? (A person from your sheet)\n")
            card1 = input().title()
            x = 0
            for i in NPC.instances:
                if i.get_name() == card1:
                    x = 1
                    break
            if x == 1:
                break
            print("Invalid choice.")
        while True:
            print("\nWhat is your room suggestion? (A room from your sheet)\n")
            card2 = input().title()
            x = 0
            for i in Room.instances:
                if i.get_name() == card2:
                    x = 1
                    break
            if x == 1:
                break
            print("Invalid choice.")
        while True:
            print("\nWhat is your weapon suggestion? (A weapon from your sheet)\n")
            card3 = input().title()
            x = 0
            for i in Weapon.instances:
                if i.get_name() == card3:
                    x = 1
                    break
            if x == 1:
                break
            print("Invalid choice.")

        self.get_answers(card1, card2, card3)

    def set_liar(self):
        self.is_liar = True
