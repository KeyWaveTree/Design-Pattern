#0~255
#8bit 8bit, 8bit - 24bit
import random as rand
class CarColor:
    colors_palette={}
    def __init__(self, color_name:str, rgb_value:dict)-> None:
        self.__color_name = color_name
        if self.__check_colors():
            self.__rgb_value = rgb_value
            CarColor.colors_palette[self.__color_name] = self.__rgb_value
        else:
            self.__rgb_value = CarColor.colors_palette[self.__color_name]

    def __check_colors(self)-> None:
        if self.__color_name not in CarColor.colors_palette: return True
        else: return False

    def change_colors(self)-> None:
        color_name = input('색깔 선택')
        temp = self.__color_name
        self.__color_name = color_name
        if self.__check_colors():
            self.__color_name = temp
        else:
            r,g,b = map(int, input("한줄로 입력 r(0~255) g(0~255) b(0~255)").split())
            r, g, b =r%256, g%256, b%256
            self.__rgb_value = {"r": r, "g":g, "b":b}
            CarColor.colors_palette[self.__color_name] = self.__rgb_value

    def __repr__(self)-> repr:
        return f"현재 지정 컬러{self.__color_name} ||| rgb value{self.__rgb_value}"



if __name__ == '__main__':
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'white','black']
    car_list = \
    [
    CarColor(rand.choice(colors), {'r':rand.randint(0, 255),'g':rand.randint(0, 255),'b': rand.randint(0, 255)})
    for _ in range(len(colors))
    ]

    for car_index,car_value in enumerate(car_list):
        print(f"{car_index+1}번째 차의 색은", car_value)
