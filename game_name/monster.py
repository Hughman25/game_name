import random

class Enemy():
    """ Sets the Enemy class """

    def __init__(self, name, level, stamina, attack_dmg, armor, reward):
        """ Initalizes the enemy mob with stats """
        self.name = name
        self.level = level
        self.stamina = stamina
        self.attack_dmg = attack_dmg
        self.armor = armor
        self.reward = reward
        self.all_stats = [name, level, self.get_health(), attack_dmg, armor, reward]

    def get_name(self):
        return self.name

    def get_abilities(self):
        return None

    def get_level(self):
        return self.level

    def get_reward(self):
        return self.reward

    def get_stamina(self):
        return self.stamina

    def get_physical_damage(self):
        return self.attack_dmg

    def set_health(self):
        self.current_health = self.get_health()

    def get_health(self):
        return self.stamina * 10

    def get_armor(self):
        return self.armor

    def set_stats(self):
        self.current_stats = self.get_all()

    def get_all(self):
        return self.all_stats

    #+++ Changable stats used during the fight +++#

    def change_health(self, value=0):
        self.current_health += value
        if self.current_health < 0:
            return 0
        return self.current_health

    def stat_adjust(self, stat, value):
        self.current_stats[stat] += value
        return self.current_stats

def main():
    enemy = Enemy("Wolf", 2, 3, 4, 0, [15, 5])
    print(enemy.get_name(), enemy.get_level(), (enemy.get_physical_damage()))
    stats = enemy.get_all()

    print("Name: " + stats[0] + " level:", stats[1], "health:", stats[2], "dmg:", stats[3], "exp:", stats[5][0], "gold:", stats[5][1])
    line = ""
    for loop in stats:
        line += str(loop) + " "
    print(line)

if __name__ == '__main__':
    main()
