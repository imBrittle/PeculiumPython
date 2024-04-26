class Item():
    def __init__(self) -> None:
        print("Creating a new item")
        
class Consumable():
    def __init__(self) -> None:
        print("Creating a new consumable")
        
class Weapon(Item):
    def __init__(self) -> None:
        print("Creating a new weapon")
        
class Armour(Item):
    def __init__(self) -> None:
        print("Creating a new armour")