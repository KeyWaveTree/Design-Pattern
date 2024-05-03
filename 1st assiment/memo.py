import sys
import os

class Memo:
    def __init__(self, text:str = ''):
        #priavate memo list
        self.__memo_list = [text]
        self.__name =" "
        self.__path =" "

    def change_info(self, ch_name: str = 'None', ch_path: str = "./Memo") -> None:
        self.__name = ch_name
        self.__path = ch_path

    def push_text(self, memo_text: str = " ") -> None:
        self.__memo_list.append(memo_text)

    def save_file_memos(self)->None:
        if not os.path.exists(self.__path): os.mkdir(self.__path)

        # f{name}.txt file generate and save
        txt_file = open(self.__path + '/'+self.__name, 'w')
        map(lambda memo_word: txt_file.write(memo_word),self.__memo_list)
        txt_file.close()

    def load_file_memos(self)->None:
        if not os.path.isdir(self.__path): os.mkdir(self.__path)
        if not os.path.isfile(self.__path + '/'+self.__name):
            sys.stdout.write("file not found. check your infomation\n")
            return

        txt_file = open(self.__path + '/'+self.__name, 'r')
        self.__memo_list = map(lambda load_txt_data: load_txt_data.strip(), txt_file.readlines())

    def print_memo(self):
        map(lambda memo_word: sys.stdout.write(memo_word+"\n"), self.__memo_list)


