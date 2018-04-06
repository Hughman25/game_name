import random

#need to figure out traits/special effects of some abilities

"""
class Ability_Collection( dict ):
     def __init__( self, *arg, **kw ):
         super( Ability_Collection, self ).__init__( *arg, **kw ):
     def new_ability( self, *arg, **kw ):
         something = Foobar( *arg, **kw )
         self[something.name]= something
         return fb
"""
class Abilities():
    """ Allows creation of unique abilities for each class or commands"""
    warrior_abilities = []

    def __init__(self, name, class_type, affix, effect_one = None, effect_two = None, effect_three = None): #Maybe try False & switch to True
        self.name = name
        self.damage_affix = affix
        #if class_type == "warrior":
            #Abilities.warrior_abilities.append(self)
        self.effect_list = [effect_one, effect_two, effect_three]
        #effects are typically tuples ('effect_trait', affix, cooldown)
        self.effect1 = effect_one
        self.effect2 = effect_two
        self.effect3 = effect_three

    def warrior_abilities(self):
        return warrior_abilities

    def get_effects(self):
        return (self.effect1, self.effect2, self.effect3)
                #(affix_type, ability_affix, target)

    def set_description(self, text):
        self.desc = text

    def set_damage(self, damage = 1):
        self.damage = damage * self.damage_affix

    def get_damage(self):
        return self.damage

    def get_stage(self):
        return self.stage

    def __str__(self):
        line = ""
        line += self.name + "\n" #self.class_type + ": " + self.name + "\n"
        for effect in self.effect_list:
            if effect is None:
                break
            else:
                for value in effect:
                    line += str(value) + " "
                line += "\n"
        #line += self.desc
        return line

    
