from abc import *
import copy

#프로토타입
class PlayerState(metaclass=ABCMeta):
    def __init__(self, name:str= "None", job:str ="None"):
        self.name = name
        self.job = job
        self.hp : int = 100
        self.mp : int = 100
        self.defense : int = 100
        self.attack : int = 100
        self.magicAttack : int = 100
        self.agility : int = 100
        self.range : int = 100

    #프로토타입이 자신을 복사할 수 있는 clone을 가지고 있어야 한다.
    def clone(self):
        return copy.deepcopy(self)

    @abstractmethod
    def ability(self):
        pass

    @abstractmethod
    def skill(self):
        pass
class Warrior(PlayerState):
    def __init__(self):
        super().__init__(self, job= "Warrior")
        self.ability()
    def ability(self, hp:int=100, defense:int=100):
        self.hp += hp
        self.defense += defense

    def skill(self):
        print(f"{self.name}의 검 스윙")

class Wizard(PlayerState):
    def __init__(self):
        super().__init__(self, job='Wizard')
        self.ability()

    def ability(self, mp:int=100, magicAttack:int=100):
        self.mp+=mp
        self.magicAttack +=magicAttack

    def skill(self):
        print(f"{self.name}의 파이어 볼")



class Archer(PlayerState):
    def __init__(self):
        super().__init__(self, job="Archer")
        self.ability()

    def ability(self, agility:int=100, attack_range:int=100):
        self.agility +=agility
        self.range+=attack_range

    def skill(self):
        print(f'{self.name}의 정밀 사격')

#클라이언트 메니저
class Game:
    def __init__(self):
        self.playerObject = {}

    def player_create(self,  proto:PlayerState):
        name = self.player_name()
        proto_clone = proto.clone()
        proto_clone.name = name
        self.playerObject[name] = proto_clone
        print(f"{name} 플레이어 생성 완료 직업: {proto.job}")

    def player_name(self):
        while True:
            name_id = input("플레이어 명: ")
            if self.check_id(name_id) :
                print("같은 이름이 있음. 다시 입력")
                continue
            else: break

        return name_id

    def player_change_name(self, name_id: str):
        if not self.check_id(name_id):
            print("찾을려는 아이디 없음. 다시 입력")
            return

        copy_state = self.playerObject[name_id].clone()
        self.playerObject.pop(name_id, None)
        new_name=self.player_name()

        self.playerObject[new_name] = copy_state
        print(f"{name_id} 플레이어의 이름을 {new_name}으로 바꾸는데 성공했습니다.")

    def player_change_state(self, name_id: str):
        if not self.check_id(name_id):
            print("찾을려는 아이디 없음. 다시 입력")
            return

        player_state = self.playerObject[name_id].clone()
        total_state_value = 700

        try:
            while total_state_value>0:

                print("1.hp, 2.mp 3.defense 4.attack 5.magicAttack 6.agility 7.range 8.종료")
                change_state_name= input(f"바꿀 수치 요소를 입력 주세요. 남은 수치({total_state_value})")
                change_state = int(input('수치를 입력해주세요(숫자 형식): '))
                if change_state_name == 'hp' or change_state_name =='1':
                    player_state.hp = change_state

                elif change_state_name == 'mp' or change_state_name == '2':
                    player_state.mp = change_state

                elif change_state_name == 'defense' or change_state_name == '3':
                    player_state.defense = change_state

                elif change_state_name == 'attack' or change_state_name == '4':
                    player_state.attack = change_state

                elif change_state_name == 'magicAttack' or change_state_name == '5':
                    player_state.magicAttack = change_state

                elif change_state_name == 'agility' or change_state_name == '6':
                    player_state.agility = change_state

                elif change_state_name == 'range' or change_state_name == '7':
                    player_state.range = change_state
                else: break

                total_state_value -= change_state

        except:
            print("잘못 입력")
            return

        self.playerObject[name_id] = player_state
        print(self.playerObject[name_id].__dict__)
        print('수치를 모두 바꿈.')


    def check_id(self, id:str)-> bool:
        return id in self.playerObject.keys()

if __name__ == "__main__":

    game_server = Game()

    #같은 클래스는 불러오지 않겠다. 다 복사해서 사용
    base_warrior = Warrior()
    base_wizard = Wizard()
    base_archer = Archer()

    game_server.player_create(base_warrior)
    game_server.player_create(base_warrior)
    game_server.player_create(base_wizard)
    game_server.player_create(base_wizard)
    game_server.player_create(base_archer)
    game_server.player_create(base_archer)

    print(game_server.playerObject.keys())
    game_server.playerObject[input('스킬을 쓸 id 입력')].skill()

    print(game_server.playerObject.keys())
    game_server.player_change_name(input('이름을 바꿔줄 id 입력'))
    print(game_server.playerObject.keys())

    game_server.player_change_state(input('능력치를 바꿔줄 id 입력'))