
import random
class Character:
    def __init__(self, name, health, attack_power, level=1):
        self.name = name
        self.attack_power = attack_power
        self.level = level
        
        # Validation initiale
        if not (0 <= health <= 100):
            raise ValueError("Health must be between 0-100")
        self._health = health
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Health must be between 0-100")
        self._health = value
    
    @property
    def is_alive(self):
        return self._health > 0
    
    def heal(self, amount):
        # Calculer nouvelle santé
        new_health = self._health + amount
        # Limiter à 100 maximum
        if new_health > 100:
            new_health = 100
        # Assigner avec le setter (validation)
        self.health = new_health
        return self.health
    
    def take_damage(self, amount):
        # Calculer nouvelle santé
        new_health = self._health - amount
        # Limiter à 0 minimum
        if new_health < 0:
            new_health = 0
        # Assigner avec le setter
        self.health = new_health
    
    def attack(self, target):
        target.take_damage(self.attack_power)
    
    def __str__(self):
        return f"{self.name} - Health: {self.health}/100, Attack: {self.attack_power}, Level: {self.level}"

class Warrior(Character):
    def __init__(self, name, attack_power, armor, level=1):
        """
        Warrior constructor - calls parent constructor with bonus health
        Override: Warriors start with 120 health instead of 100
        """
        # Call parent constructor with 120 health (Warrior gets +20 health)
        super().__init__(name, health=120, attack_power=attack_power, level=level)
        self.armor = armor  # Warrior-specific attribute
    
    def take_damage(self, amount):
        """
        OVERRIDE: Reduce damage by armor before applying
        This REPLACES Character.take_damage() for Warrior objects
        """
        # Calculate actual damage after armor reduction
        actual_damage = max(0, amount - self.armor)
        
        # Call PARENT'S version with reduced damage
        super().take_damage(actual_damage)
        
        # Optional: Add Warrior-specific logic
        if actual_damage == 0:
            print(f"{self.name}'s armor blocked all damage!")
        else:
            print(f"{self.name}'s armor reduced {amount} damage to {actual_damage}")
    
    def shield_bash(self, target):
        """
        Warrior SPECIAL attack (not in Character class)
        """
        # Deal extra damage (attack_power + 5)
        extra_damage = self.attack_power + 5
        target.take_damage(extra_damage)
        
        # Temporary armor reduction (special effect)
        self.armor -= 1
        if self.armor < 0:
            self.armor = 0
        
        return f"{self.name} used Shield Bash! Dealt {extra_damage} damage to {target.name}. Armor reduced to {self.armor}"
    
    def __str__(self):
        """
        OVERRIDE: Add armor to string representation
        """
        # Get parent's string, then add Warrior info
        parent_str = super().__str__()
        return f"{parent_str} | Armor: {self.armor}" 

class Mage(Character):
    def __init__(self, name , spell_power ,mana=100, level=1):
        super().__init__(name, health = 80, attack_power = 10, level = level)
        self.mana = mana
        self .spell_power = spell_power
    
    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Mana should be between 0 and 100 ")
        self._mana = value
    
    @property
    def can_cast_spell(self):
        return self.mana >= 10
    
    def cast_spell(self , target):
        if not self.can_cast_spell:
            return f"{self.name} has not enough mana"
        self.mana -= 10
        target.take_damage(self.spell_power)
        return f"{self.name} casts a fireball ! {target.name} takes {self.spell_power} damage"
    
    def meditate(self):
        self.mana += 20
        return f"{self.name} mana has been uped to {self.mana}"
    
    def heal_spell(self , target):
        if self._mana < 15:
            return f"Not enough mana for healing !"
        self.mana -= 15
        target.heal(25)
        return f"{self.name} has healed {target.name}"
    
    def take_damage(self, amount):
        super().take_damage(amount)
        self.mana -= 5 
        return f"Pertubation magique {self.name} a perdu 5 mana"
    
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} | Mana: {self.mana}/100 | Puissance des sorts: {self.spell_power}"
    
    import random

class Archer(Character):
    def __init__(self, name, attack_power, accuracy, arrows=20, level=1):
        super().__init__(name, health=90, attack_power=attack_power, level=level)
        
        if not (0.0 <= accuracy <= 1.0):
            raise ValueError("Accuracy must be between 0.0 and 1.0")
        self.accuracy = accuracy
        
        if not (0 <= arrows <= 30):
            raise ValueError("Arrows must be between 0 and 30")
        self.arrows = arrows
    
    @property
    def can_shoot(self):
        return self.arrows > 0
    
    def ranged_attack(self, target):
        if not self.can_shoot:
            return f"{self.name} n'a plus de flèches!"
        
        self.arrows -= 1
        
        if random.random() < self.accuracy:
            target.take_damage(self.attack_power)
            return f"{self.name} tire et touche {target.name}! {target.name} prend {self.attack_power} dégâts. Flèches: {self.arrows}/30"
        else:
            return f"{self.name} tire et rate {target.name}! Flèches: {self.arrows}/30"
    
    def reload(self, arrow_count):
        new_arrows = self.arrows + arrow_count
        self.arrows = min(30, new_arrows)
        return f"{self.name} recharge {arrow_count} flèches. Total: {self.arrows}/30"
    
    def attack(self, target):
        """Override: Use ranged attack if possible"""
        if self.can_shoot:
            return self.ranged_attack(target)
        else:
            super().attack(target)
            return f"{self.name} n'a plus de flèches et attaque au corps à corps!"
    
    def __str__(self):
        """Override: Show accuracy and arrows"""
        parent_str = super().__str__()
        return f"{parent_str} | Précision: {self.accuracy*100:.0f}% | Flèches: {self.arrows}/30"
    