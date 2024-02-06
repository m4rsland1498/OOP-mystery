import random


class NPC:
    instances = []

    def __init__(self, npc_name):
        self.name = npc_name
        self.description = None
        self.cards = None
        NPC.instances.append(self)

    def get_name(self):
        return self.name

    def get_answers(self, card1, card2, card3):
        if card1 in self.cards or card2 in self.cards or card3 in self.cards:
            while True:
                x = random.randint(0, 2)
                if card1 == self.cards[x] or card2 == self.cards[x] or card3 == self.cards[x]:
                    print(self.cards[x])
                    break
        else:
            print("\nI don't know anything about that.\n")

    def set_cards(self, cards):
        self.cards = cards
