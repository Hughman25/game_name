import random
import classes
import monster


def combat(player, enemy):
    player.set_stats()
    player.set_health()
    enemy.set_stats()
    enemy.set_health()
    
    print("Enemy:", enemy.change_health())
    print(player.get_name() + ":", player.change_health())
    print("\n")

    while player.change_health() > 0 and enemy.change_health() > 0:
        player_ability = player.sel_ability()

        player_attack = player_ability.get_damage() - enemy.get_armor()
                
        for effect in player_ability.get_effects():
            if effect is not None:
                if effect[3] == 0:
                    if effect[0] is "Finisher":
                        if player.get_class() == "Warrior":
                            multiplier = round(2 - (enemy.change_health() / enemy.get_health()), 2)
                            player_attack = int(effect[1] * player_attack) + (multiplier * int(effect[1] * player_attack))
                            
                            health_check = enemy.change_health()
                            
                            if health_check - player_attack > 0:
                                player_attack = player_attack * .3
                                
                    elif effect[0] is "Damage" or "AoE":
                        secondary = int(effect[1] * player_attack)
                        if effect[2] == 1:
                            enemy.change_health(-secondary)
                        if effect[2] == 2:
                            #for enemy in enemy_list??
                            player_attack = 0
                            enemy.change_health(-secondary)
                            
                
        enemy_attack = enemy.get_physical_damage()
        
        enemy_health = enemy.change_health(-int(player_attack))
        if enemy_health <= 0:
            print("You have slain the " + enemy.get_name() + "\n")
            continue
        print("Enemy:", enemy_health)

        for effect in player_ability.get_effects():
            if effect is not None:
                if effect[3] == 1:
                    if effect[0] == "Lifesteal":
                        secondary = int(effect[1] * player_attack)
                        if effect[2] == 0:
                            player.change_health(secondary)
                            print("You heal for yourself " + str(secondary) + "!")

        player_health = player.change_health(-int(enemy_attack))
        print(player.get_name() + ":", player_health)

        for effect in player_ability.get_effects():
            if effect is not None:
                if effect[3] == 1:
                    #+++ Add effect for stage 2 +++#
                    pass

        print("\n")
    
    if enemy.change_health() <= 0:
        reward = enemy.get_reward()
        player.gain_exp(reward[0])
        player.change_gold(reward[1])
        #get rewards
        item_reward = get_item(reward[2])
        if item_reward is False:
            print("No Item Found")
            return None #not sure what yet
        else:
            print("\nYou found " + item_reward[0] + "!")
            print(display_item(item_reward))
            
        
        equip = input("Would you like to equip this item? ").lower()
        if equip in "yes":
            player.set_equipment(item_reward[1], item_reward)
        print()
    else:
        print("You lost\n")
            

def get_item(enemy_loot_table):
    game_items = open("game_items.csv", "r")

    rand_line = random.randint(1, 22)
    counter = 0
        
    for line in game_items:
        if counter == rand_line:
            game_item = line.rstrip(",\n")
            game_item = game_item.split(",")
            for loop in range(1, 10):
                game_item[loop] = int(game_item[loop])
                               
            game_items.close()

            if game_item[2] > enemy_loot_table:
                return False
            
            return game_item
        
        counter += 1

    game_items.close()
    return False


def display_item(item):
    line = "-----------------------------------------------------------------\n"
    line += "{0: <64}".format("| " + item[0]) + "|\n"
    line += "{0: <64}".format("| " + classes.Item_Rarity(item[2]).name + " " + classes.Item(item[1]).name) + "|\n"
    line += "{0: <56}".format("| Attack Power:\t" + str(item[3]) + "\tStamina:\t" + str(item[7]) + "\tArmor:\t" + str(item[8])) + "|\n"
    line += "{0: <53}".format("| Strength:\t" + str(item[4]) + "\tAgility:\t" + str(item[5]) + "\tIntel:\t" + str(item[6])) + "|\n"
    line += "-----------------------------------------------------------------"
    return line

def get_enemy(): #maybe a difficulty too?
    choice = input("Enter the number of your challenge: ")
    if not choice.isdigit():
        return get_enemy()
    else:
        choice = int(choice)
    rand_hp = random.randint(8, 15) * choice
    rand_attack = random.randint(10, 20) * choice
    rand_armor = random.randint(5, 10) * choice
    if choice == 1:
        return monster.Enemy("Wolf", 2, rand_hp-3, rand_attack, rand_armor, [15, 5, 0])
    elif choice == 2:
        return monster.Enemy("Tiger", 3, rand_hp, rand_attack, rand_armor, [25, 8, 0])
    elif choice == 3:
        return monster.Enemy("Imperial Footsoldier", 4, rand_hp + 5, rand_attack, rand_armor + 10, [40, 15, 1])
    elif choice == 4:
        return monster.Enemy("Minotaur", 5, rand_hp + 15, rand_attack + 30, rand_armor + 15, [100, 25, 2])
    else:
        return get_enemy()


def menu():
    """ Displays the options for the user """
    print("\n1. Challenge!")
    print("2. Show Equipment")
    print("3. Show Stats")
    print("4. Quit")
    selection = input("Choose your path: ")
    return selection


def main():

    name = input("Enter the name of your character: ").capitalize()
    race = input("Enter your race: ").capitalize()
    class_ = input("Enter your class: ").lower()
    print()

    player = classes.Warrior(race, name)
    player.make_abilities()
    
    while True:
        selection = menu()
        if not selection.isdigit():
            continue
        else:
            selection = int(selection)
            if selection < 1 or selection > 4:
                continue

        if selection == 1:

            enemy = get_enemy()
            print("\n")
            combat(player, enemy)
        
        elif selection == 2:
            print("\n")
            for loop in range(9):
                print(player.get_equipment(loop))
            print("\n")
            continue

        elif selection == 3:
            print(player)
        
        elif selection == 4:
            break
        
    

if __name__ == '__main__':
    main()
