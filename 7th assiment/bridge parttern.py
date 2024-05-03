#두개의 시스템(안드로이드, ios) 존재할때 각 시스템에서 개발된
# 알고리즘들의 성능을 테스트하고자 한다.
#시스템: android, ios
#알고리즘: Dijkstra, Minimum Spanning Tree, A_star

#1) bridge 패턴을 사용하지 않을때  각 만들어야 할 클래스의 개수는 몇개인가?


#2) 브릿지 패턴을 적용해보자 system은 Abstraction의 api이며,
# TestUnit은 Implementor의 api이다.
# 이들을 브릿지로 연결하고 1번 문제를 해결하는 코드를 작성하시오.
'''
class System:
    def __init__(self):
        pass

    def start_test(self):
        pass

class TestUnit:
    def run(self):
        pass

'''



#abstruction
class System:
    def __init__(self):
        pass
    def start_test(self):
        pass

# implementor 구체화
class TestUnit:
    def run(self):
        pass

class IOS(System):
    def __init__(self, algorithm: TestUnit):
        super().__init__()
        self.__algorithm = algorithm
        self.__os = "IOS"

    def start_test(self):
        print(f'os is {self.__os}, {self.__algorithm.run()} algorithm start', end=' /// ')

class Android(System):
    def __init__(self, algorithm: TestUnit):
        super().__init__()
        self.__algorithm = algorithm
        self.__os ="Android"

    def start_test(self):
        print(f'os is {self.__os}, {self.__algorithm.run()} algorithm start')


class Dijkstra(TestUnit):
    def run(self):
        return "다익스트라 알고리즘 실행"

class A_star(TestUnit):
    def run(self):
        return "A* 알고리즘 실행"

class  Minimum_Spanning_Tree(TestUnit):
    def run(self):
        return "MST 알고리즘 실행"

if __name__ == '__main__':
    dijkstar= Dijkstra()
    a_star = A_star()
    mst = Minimum_Spanning_Tree()

    algrithm_list = [dijkstar, a_star, mst]
    for alg in algrithm_list:
        IOS(alg).start_test()
        Android(alg).start_test()