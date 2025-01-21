class Enemy:
    def __init__(self, name, hp=100, damage=10, armor=1):
        print("Создаем противника")
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attack(self, player):
        print(f"\n{self.name} атакует {player.name}")
        player.hp -= self.damage
        print(f"{player.name} получает урон {self.damage}")
        print(f"У игрока осталось {player.hp} хп\n")