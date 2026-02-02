from Config import Config
from characters import Character, Warrior, Mage, Archer

class Game:
    def __init__(self, name="RPG Adventure"):
        """Initialise un nouveau jeu"""
        # Stocke tous les personnages du jeu
        self.characters = []
        
        # Utilise TA classe Config pour les paramètres
        self.config = Config(
            game_name=name,
            max_players=4,
            difficulty="medium",
            auto_save=True,
            sound_volume=80
        )
        
        print(f"🎮 Jeu créé: {self.config.game_name}")
        print(f"   Difficulté: {self.config.difficulty}")
    
    def add_character(self, character):
        """Ajoute un personnage au jeu"""
        # Vérifie la limite de joueurs
        if len(self.characters) >= self.config.max_players:
            print(f"❌ Limite de {self.config.max_players} joueurs atteinte!")
            return False
        
        # Ajoute le personnage
        self.characters.append(character)
        print(f"✅ {character.name} rejoint le jeu!")
        print(f"   ({len(self.characters)}/{self.config.max_players} joueurs)")
        return True
    
    def remove_character(self, character_name):
        """Retire un personnage du jeu"""
        for character in self.characters:
            if character.name == character_name:
                self.characters.remove(character)
                print(f"👋 {character_name} quitte le jeu.")
                return True
        
        print(f"❌ Personnage '{character_name}' non trouvé.")
        return False
    
    def show_characters(self):
        """Affiche tous les personnages"""
        if not self.characters:
            print("Aucun personnage dans le jeu.")
            return
        
        print(f"\n{'='*50}")
        print(f"PERSONNAGES ({len(self.characters)}/{self.config.max_players})")
        print('='*50)
        
        for i, character in enumerate(self.characters, 1):
            print(f"{i}. {character}")
    
    def find_character(self, name):
        """Trouve un personnage par son nom"""
        for character in self.characters:
            if character.name.lower() == name.lower():
                return character
        return None
    
    def start_combat(self, char1_name, char2_name):
        """Commence un combat entre deux personnages"""
        # Trouve les personnages
        char1 = self.find_character(char1_name)
        char2 = self.find_character(char2_name)
        
        # Vérifications
        if not char1 or not char2:
            print("❌ Personnage(s) non trouvé(s)!")
            return None
        
        if char1 == char2:
            print("❌ Un personnage ne peut pas se battre contre lui-même!")
            return None
        
        print(f"\n{'='*50}")
        print(f"⚔️  COMBAT: {char1.name} vs {char2.name}")
        print('='*50)
        
        # Affiche l'état initial
        print(f"\nDébut du combat:")
        print(f"  {char1.name}: {char1.health} HP")
        print(f"  {char2.name}: {char2.health} HP")
        
        # Tour par tour (maximum 10 tours)
        for turn in range(1, 11):
            print(f"\n--- Tour {turn} ---")
            
            # Char1 attaque Char2
            print(f"{char1.name} attaque:")
            if isinstance(char1, Archer) and char1.can_shoot:
                print(f"  {char1.ranged_attack(char2)}")
            elif isinstance(char1, Mage) and char1.can_cast_spell:
                print(f"  {char1.cast_spell(char2)}")
            else:
                char1.attack(char2)
                print(f"  {char2.name} perd des points de vie!")
            
            # Vérifie si Char2 est mort
            if not char2.is_alive:
                print(f"\n💀 {char2.name} est vaincu!")
                print(f"🏆 {char1.name} remporte le combat!")
                return char1
            
            # Char2 attaque Char1
            print(f"\n{char2.name} contre-attaque:")
            if isinstance(char2, Archer) and char2.can_shoot:
                print(f"  {char2.ranged_attack(char1)}")
            elif isinstance(char2, Mage) and char2.can_cast_spell:
                print(f"  {char2.cast_spell(char1)}")
            else:
                char2.attack(char1)
                print(f"  {char1.name} perd des points de vie!")
            
            # Vérifie si Char1 est mort
            if not char1.is_alive:
                print(f"\n💀 {char1.name} est vaincu!")
                print(f"🏆 {char2.name} remporte le combat!")
                return char2
            
            # Affiche l'état après le tour
            print(f"\nÉtat après le tour {turn}:")
            print(f"  {char1.name}: {char1.health} HP")
            print(f"  {char2.name}: {char2.health} HP")
        
        # Match nul après 10 tours
        print(f"\n🤝 MATCH NUL après 10 tours!")
        return None
    
    def get_game_info(self):
        """Retourne les informations du jeu"""
        return {
            "game_name": self.config.game_name,
            "total_characters": len(self.characters),
            "max_characters": self.config.max_players,
            "difficulty": self.config.difficulty,
            "characters": [char.name for char in self.characters]
        }


# Fonction de test
def test_game():
    """Teste le système de jeu"""
    print("=== TEST DU SYSTÈME DE JEU ===")
    
    # 1. Créer le jeu
    game = Game("Python RPG Adventure")
    
    # 2. Créer des personnages
    warrior = Warrior("Conan", attack_power=20, armor=5)
    mage = Mage("Merlin", spell_power=25)
    archer = Archer("Legolas", attack_power=15, accuracy=0.9, arrows=10)
    
    # 3. Ajouter les personnages
    game.add_character(warrior)
    game.add_character(mage)
    game.add_character(archer)
    
    # 4. Afficher tous les personnages
    game.show_characters()
    
    # 5. Faire un combat
    print("\n" + "="*50)
    print("LANCEMENT D'UN COMBAT")
    game.start_combat("Conan", "Merlin")
    
    # 6. Afficher l'état après combat
    print("\n" + "="*50)
    print("ÉTAT APRÈS COMBAT:")
    game.show_characters()
    
    # 7. Afficher les infos du jeu
    print("\n" + "="*50)
    print("INFORMATIONS DU JEU:")
    info = game.get_game_info()
    for key, value in info.items():
        print(f"  {key}: {value}")
    
    # 8. Afficher la configuration
    print(f"\n🔧 Configuration: {game.config}")

# Exécute le test seulement si ce fichier est lancé directement
if __name__ == "__main__":
    test_game()