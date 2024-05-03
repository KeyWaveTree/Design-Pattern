#스트레이지 패턴을 사용해서
# 뛰거나, 걸을 수 있는 "움직일 수 있는 " 기능(strategy1)과
# 총을 쏘거나 로켓을 발사할 수 있는 "공격할 수 있는" 기능(strategy2)이 있는
# 로봇(context)을 클래스들로 정의하고, 해당 로봇을 실행하는 클라이언트 코드를 작성해보자
#
# -클라이언트는 코드 실행중 걷다가 뛰는 것으로 변경하고, 총에서 로켓으로 변경하는 코드를 포함한다.
# -각 기능들은 print 함수를 이용하여 간단히 해당 기능에 대한 표현만 한다. (ex: print("총을 쏘다."))

from abc import *


class Move(metaclass=ABCMeta):
    move_state="걷기"

    def do_something(self):
        pass

    @abstractmethod
    def state_change(self):
        pass

class MoveTypeRun(Move):
    def do_something(self):
        print(f"{MoveTypeRun.move_state} 걸음으로 가는중")

    def state_change(self):
        print("뛰기로 변경됨")
        MoveTypeRun.move_state = "뛰기"

class MoveTypeBase(Move):
    def do_something(self):
        print(f"{MoveTypeBase.move_state} 걸음으로 가는중")

    def state_change(self):
        print("걷기로 변경됨")
        MoveTypeBase.move_state="걷기"
class Attack(metaclass=ABCMeta):
    mode_Attact="로켓"

    @abstractmethod
    def do_attack(self):
        pass

    @abstractmethod
    def change_weapon(self):
        pass

class AttactTypeRocket(Attack):
    def do_attack(self):
        print(f"{AttactTypeRocket.mode_Attact}으로 공격")

    def change_weapon(self):
        print("무기를 로켓으로 변경")
        AttactTypeRocket.mode_Attact="로켓"

class AttactTypeGun(Attack):
    def do_attack(self):
        print(f"{AttactTypeGun.mode_Attact}으로 공격")

    def change_weapon(self):
        print("무기를 총으로 변경")
        AttactTypeGun.mode_Attact="총"

class Robot:
    def __init__(self, ):
        self.__state = "None"
        self.__weapon = "None"

    def set_weapon(self, function1:Move , function2:Attack ):
        self.__state = function1
        self.__weapon =function2
        self.__state.state_change()
        self.__weapon.change_weapon()

    def attack(self):
        self.__weapon.do_attack()

    def move(self):
        self.__state.do_something()


if __name__ == "__main__":
    pass