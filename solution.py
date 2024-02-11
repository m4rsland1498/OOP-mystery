import sys

from npcs import NPC
from weapons import Weapon
from rooms import Room


class Solution:
    def __init__(self, cards):
        self.answers = cards

    def accuse(self):
        while True:
            print("\nWhat is your suspect accusation? (A person from your sheet)\n")
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
            print("\nWhat is your room accusation? (A room from your sheet)\n")
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
            print("\nWhat is your weapon accusation? (A weapon from your sheet)\n")
            card3 = input().title()
            x = 0
            for i in Weapon.instances:
                if i.get_name() == card3:
                    x = 1
                    break
            if x == 1:
                break
            print("Invalid choice.")
        check = ""
        while check != "y" and check != "n":
            check = input("Are you sure you want to make an accusation? (y/n)").lower()
        print("\n--------------------------------------------")
        if check == "y":
            self.accusation_check(card1, card2, card3)

    def accusation_check(self, card1, card2, card3):
        accusations = [card1, card2, card3]
        correct = 0
        for i in self.answers:
            if i.get_name() in accusations:
                correct += 1
        if correct == 3:
            print("Well done, detective!\nYou cracked the case and successfully brought Estelle's murderer to justice.")
            print("\n\nIt was", (self.answers[2]).get_name(), "in the", (self.answers[1]).get_name(), "with the", (self.answers[0].get_name() + "."))
            sys.exit()
        elif correct == 0:
            print("I'm sorry detective but you have not done your job here.\nThe killer remains on the loose.")
            print("\n\nIt was", (self.answers[2]).get_name(), "in the", (self.answers[1]).get_name(), "with the", (self.answers[0].get_name() + "."))
            sys.exit()
        else:
            print("I'm sorry detective but this isn't good enough.\nWe need all the details.")
            print("\n\nIt was", (self.answers[2]).get_name(), "in the", (self.answers[1]).get_name(), "with the", (self.answers[0].get_name() + "."))
            sys.exit()
