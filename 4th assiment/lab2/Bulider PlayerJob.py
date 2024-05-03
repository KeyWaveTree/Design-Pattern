class PlayerState:
    def __init__(self):
        self.name: str = "None"
        self.hp: int = 100
        self.mp: int = 100
        self.defense: int = 5
        self.attack: int = 5
        self.magicAttack: int = 5
        self.agility: int = 5
        self.range: int = 5

    def setName(self, name: str = "None") -> None:
        self.name = name

    def setHP(self, hp: int) -> None:
        self.hp = hp

    def setMP(self, mp: int) -> None:
        self.mp = mp

    def setDefense(self, defense: int) -> None:
        self.defense = defense

    def setAttack(self, attack: int) -> None:
        self.attack = attack

    def setAgility(self, agility: int) -> None:
        self.agility = agility

    def setRange(self, attackRange: int) -> None:
        self.range = attackRange