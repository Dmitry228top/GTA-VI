
class Player:
    def __init__(self, name, hp=100, mana=100, stamina=100, _class="НИЩИЙ", armor=2, damage=10,agility=5,strength=5, intellect=5):
        print("Создаем персонажа")
        
        self.name = name
        self.hp = hp
        self._class = _class
        self.armor = armor
        self.strength = strength
        self.intellect = intellect
        self.damage = damage
        self.mana = mana
        self.agility = agility
        self.stamina = stamina
        self.chooseClass()
    
    def show_info(self):
       print(f"\n Имя {self.name}\n Здоровье {self.hp}\n Мана {self.mana}\n Выносливость {self.stamina}\n Урон {self.damage}\n Сила {self.strength}\n Ловкость {self.agility}\n Интеллект {self.intellect}\nКласс {self._class}")

    def attack(self, enemy):
        print(f"\n{self.name} атакует {enemy.name}")
        enemy.hp -= self.damage
        print(f"{enemy.name} получает урон {self.damage}")
        print(f"У {enemy.name} осталось {enemy.hp} хп\n")

    def chooseClass(self):
        
        # 1. В соответствии с выбранным классом, увеличить нужные характеристики (силу, ловкость, интеллект)
        # 2. После изменения характеристик, увеличить ману, хп и выносливость в зависимости от характеристик
        # 3. Изменить переменную класса в в соответствии с выбором игрока
        # хп = 100 + сила * 2, мана = 100 + интеллект * 2
        choose = input("Выберите класс: 1.ВОИН 2.МАГ 3.ВОР\nНомер или название ")
        if choose == "1" or choose.lower() == "воин":
            self.strength  += 5
            self.agility += 2
            self.armor += 6
            self._class = "Воин"

        elif choose == "2" or choose.lower() == "маг":
            self.intellect += 6
            self.agility += 1
            self.armor +=2
            self._class = "Маг"

        elif choose == "3" or choose.lower() == "вор":
            self.strength += 2
            self.agility += 5
            self.intellect += 3
            self.armor +=4
            self._class = "Вор"

        else:
            print("НЕПРАВИЛЬНЫЙ ВЫБОР, ТЫ ТЕПЕРЬ НИЩИЙ -2 ко всему")
            self.strength -= 2
            self.agility -= 2
            self.intellect -= 2
            self.armor = 0
        self.show_info()
