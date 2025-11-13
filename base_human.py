from all_weapons import Weapons


class Human:
    def __init__(self,max_hp=100, hp=100, damage=10  ,armor=100, money=0,active_weapon="Деревянный меч", damage_of_active_weapon = 5,active_armor='leather_armor', attack_damage =1, klass = 'human'):
        self.hp = hp
        self.klass = klass
        self.damage = damage + damage_of_active_weapon
        self.max_hp = max_hp
        self.armor = armor
        self.money = money
        self.active_weapon = Weapons['heroes'][self.klass][active_weapon]
        self.active_armor = active_armor
        self.damage_of_active_weapon = self.active_weapon['damage']
        self.durability_of_active_weapon = self.active_weapon['durability']
        self.attack_damage = attack_damage
        '''self.effect_of_active_armor = effect_of_active_armor
        self.durability_of_active_armor = durability_of_active_armor '''

    def attack(self):
        self.durability_of_active_weapon -= 1
        return self.damage
    ''' def take_damage(self, attack_damage):
        self.hp -= attack_damage/self.effect_of_active_armor
        self.effect_of_active_armor -= 1
        return f'Здоровье: {self.hp}; прочность брони равна: {self.durability_of_active_armor}' '''
    def __str__(self):
        return f'hp: {self.hp}\nclass:{self.klass}\ndamage:{self.damage}'
hu1 = Human()
print(hu1) 
