import random
import classes
import enemy

def get_item():
    game_items = open("game_items.csv", "r")

    rand_line = random.randint(1, 7)
    counter = 0
        
    for line in game_items:
        if counter == rand_line:
            game_item = line.rstrip("\n")
            game_item = game_item.split(",")
            for loop in range(1,9):
                game_item[loop] = int(game_item[loop])
            game_items.close()
            return game_item
        counter += 1

    game_items.close()
    return False

def display_item(item):
    line = ""
    line += item[0] + "\n"
    line += classes.Item_Rarity(item[2]).name + " " + classes.Item(item[1]).name + "\n"
    line += "Attack Power:\t" + str(item[3]) +  "\tStamina:\t" + str(item[6]) +  "\tArmor:\t" + str(item[8]) + "\n"
    line += "Strength:\t" + str(item[4]) +  "\tAgility:\t" + str(item[5]) + "\tIntel:\t" + str(item[7]) + "\n"
    return line

def main():
    name = input("Enter the name of your character: ").capitalize()
    race = input("Enter your race: ")
    class_ = input("Enter your class: ").lower()

    if class_ == "warrior":
        Hughman = classes.Warrior(race, name)
        print(Hughman.get_stats())
        print(Hughman.get_physical_damage())
    item = get_item()
    print(display_item(item))
    Hughman.set_equipment(item[1], item)
    print(Hughman.get_equipment(item[1]))
    print(Hughman.get_stats())
    print(Hughman.get_physical_damage())
    

main()
#item = get_item()
#print(display_item(item))

