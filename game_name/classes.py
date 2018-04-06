import random
import ability
#import sys
from enum import IntEnum

class Item(IntEnum):
    weapon, head, neck, shoulders, chest, gloves, ring, legs, boots = range(9)

class Item_Rarity(IntEnum):
    Common, Uncommon, Rare, Epic = range(4)

class Race():
    """ Sets the race of a character """

    def __init__(self, race, name):
        """ Sets the race and their given special racial """
        self.race = race
        self.name = name

    def get_name(self):
        return self.name

    def racial(self):
        """ Getter for the racial of the character """
        if race == "Orc":
            return "Rage"

class Warrior(Race):
    """ Sets the Warrior class """
    #can potentially define items here, specific to class
    
    def __init__(self, race, name, gold=0):
        """ Initalizes the warrior class stats """
        super(Warrior, self).__init__(race, name)
        self.class_name = "Warrior"
        #stats[strength, agility, intellect, stamina, armor]
        self.stats = [6, 6, 5, 6, 0]
        
        self.scale = [3, 1, 0, 2, 0]           #rate at which each stat scales per level
        self.level = 1
        self.levelexp = 50
        self.exp = 0
        self.gold = gold

        self.equipment = [False, False, False, False, False, False, False, False, False]
        #[Weapon, Head, Neck, Shoulder, Chest, Gloves, Ring, Legs, Boots]
        #Maybe belt can be added, as a supplement to Legs, similar to sockets in games

        #+++ Create Abilities here +++#

    def make_abilities(self):
        #tuples are ("name_affix", damage_ratio, target(0 = player, 1 = monster, 2 = AoE), stage (0 before, 1 midway, 2 at the end)
        self.abilities = []
        
        self.abilities.append(ability.Abilities("Vampiric Strike", "warrior", 1, ("Lifesteal", .35, 0, 1), None, None))
        self.abilities[0].set_description("Deals damage and heals for a portion of the damage dealt")
        
        self.abilities.append(ability.Abilities("Slice N' Dice", "warrior", .75, ("Damage", 1, 1, 0), None, None))
        self.abilities[1].set_description("Attacks twice, each attack dealing a large portion of the player's damage")
        
        self.abilities.append(ability.Abilities("Cleave", "warrior", 1, ("AoE", .6, 2, 0), None, None))
        self.abilities[2].set_description("Cleaves enemies, dealing damage to all enemies on the field")

        self.abilities.append(ability.Abilities("Execute", "warrior", 1, ("Finisher", 1.25, 1, 0), None, None))
        self.abilities[3].set_description("Execute deals more damage based on enemies missing health, but deals significantly less if it does not kill")

        

    def get_abilities(self):
        for each_ability in self.abilities:
            print(each_ability)

    def sel_ability(self):
        #abilities = abilities.warrior_abilities()
        print("Q - Vampiric Strike")
        print("W - Slice N' Dice")
        print("E - Cleave")
        print("R - Execute")
        choice = input("Make your move: ").lower()
        if choice == "q":
            self.abilities[0].set_damage(self.get_physical_damage())
            return self.abilities[0]
        elif choice == "w":
            self.abilities[1].set_damage(self.get_physical_damage())
            return self.abilities[1]
        elif choice == "e":
            self.abilities[2].set_damage(self.get_physical_damage())
            return self.abilities[2]
        elif choice == "r":
            self.abilities[3].set_damage(self.get_physical_damage())
            return self.abilities[3]
        else:
            print("try again\n")
            return self.sel_ability()

    def gain_exp(self, exp):
        self.exp += exp
        while self.exp >= self.levelexp:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp -= self.levelexp
        if self.level % 2 == 0:
            self.levelexp += (50 * (self.level-1))
        else:
            self.levelexp += 50 + (25 * (self.level-2))
            
        self.levelstats()

    def levelstats(self):
        for number in range(len(self.stats)):
            self.stats[number] += self.scale[number]

    #+++ These are the stats used at the beginning/end of a fight and work as a base +++#

    def get_level(self):
        return self.level

    def get_exp(self):
        return self.exp, self.levelexp

    def get_stats(self):
        return self.stats

    def __str__(self):
        line = "Character: " + self.name + "\n"
        line += "Race: " + self.race + " Class: " + self.class_name + " Gold: " + str(self.gold) + "\n"
        line += "Level: " + str(self.get_level()) + " EXP needed for next level: " + str(self.levelexp-self.exp) + "\n"
        line += "Health: " + str(self.get_health()) + " Physical AD: " + str(self.get_physical_damage()) + "\n"
        line += "Stamina: " + str(self.stats[3]) + " Armor: " + str(self.stats[4]) + "\n"
        line += "Strength: " + str(self.stats[0]) + " Agility: " + str(self.stats[1]) + " Intellect: " + str(self.stats[2]) + "\n\n"
        return line        
        

    def get_strength(self):
        return self.stats[0]

    def get_agility(self):
        return self.stats[1]

    def get_intellect(self):
        return self.stats[2]
    
    def get_stamina(self):
        return self.stats[3]

    def change_stat(self, stat, value):
        self.stats[stat] += value

    def set_stats(self):
        self.current_stats = self.stats

    def calculate_atk_pwr(self):
        AP = self.stats[0] * 2 + self.stats[1]  * 1
        for item in self.equipment:
            if item == False:
                continue
            else:
                AP += item[3]
        return AP

    def get_physical_damage(self):
        #for when weapon dmg is added
        weapon = self.get_equipment("weapon")
        if weapon == False:
            damage = 1 + self.calculate_atk_pwr()
        else:
            #weapon types can have different typical ranges
            low_range = weapon[9]/2
            high_range = weapon[9]
            weapon_damage = random.randint(low_range, high_range)
            damage = weapon_damage + self.calculate_atk_pwr()
        return damage

    def set_health(self):
        self.current_health = self.stats[3] * 10

    def get_health(self):
        return self.stats[3] * 10

    def get_armor(self):
        return self.stats[4]

    def get_class(self):
        return self.class_name

    def set_equipment(self, slot, item):
        #may have to either remove self or move equipment initialization into __init__
        try:
            #test if item is already equipped
            if self.equipment[slot] == False:
                self.equipment[slot] = item
            #remove stats from old item
            else:
                for stat in range(5):
                    self.change_stat(stat, -(self.get_equipment(slot)[stat+4]))
                self.equipment[slot] = item
                
        except TypeError:
            if self.equipment[Item[slot].value] == False:
                self.equipment[Item[slot].value] = item
            else:
                for stat in range(5):
                    self.change_stat(stat, -(self.get_equipment(slot)[stat+4]))
                self.equipment[Item[slot].value] = item

        #increase stats by new item
        for stat in range(5):
            self.change_stat(stat, item[stat+4])
        
    def get_equipment(self, slot):
        try:
            return self.equipment[slot]
        except TypeError:
            return self.equipment[Item[slot].value]

    #+++ Temporary stats that are used/adjusted during the fight, such as health and attack power buffs/debuffs +++#

    def change_health(self, value=0):
        self.current_health += value
        if self.current_health > self.get_health():
            self.current_health = self.get_health()
        elif self.current_health < 0:
            return 0
        return self.current_health
    
    def stat_effect(self, stat, value):
        self.current_stats[stat] += value
        return self.current_stats

    def change_gold(self, value):
        self.gold += value

    def get_gold(self):
        return self.gold

def main():
    name = input("Enter the name of your character: ").capitalize()
    race = input("Enter your race: ").capitalize()
    class_ = input("Enter your class: ").lower()

    if class_ == "warrior":
        Hughman = Warrior(race, name)
    #print(Item_Rarity(0).name)
    #print(Hughman.get_physical_damage())
    #Hughman.set_equipment("head", ["idk"])
    #print(Hughman.get_equipment("head"))
    Hughman.make_abilities()
    Hughman.get_abilities()

if __name__ == '__main__':
    main()
