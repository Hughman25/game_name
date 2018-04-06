import random

class Shop():

    def __init__(self):
        self.items = open("game_items.csv", "r")
        
        self.inventory = []
        for line in self.items:
            item = line.rstrip(",\n")
            item = game_item.split(",")
            if item[2] is "1":
                for loop in range(1, 10):
                    item[loop] = int(item[loop])
                self.inventory.append(item)
            else:
                continue

        self.items.close()

    def get_inventory(self):
        return self.inventory

    def change_player_gold(self, player, value)
        
                

    def __str__(self):
        line = ""
        return line
