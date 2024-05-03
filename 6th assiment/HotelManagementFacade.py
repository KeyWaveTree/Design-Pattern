class ReservationSystem:
    def bookRoom(self, roomType):
        print(f"book a {roomType} room")

class CleaningService:
    def scheduleCleaning(self, roomId):
        print(f"scheduling cleaning for room {roomId}")

class DiningService:
    def orderFood(selfself, roomNumber, foodItem):
        print(f"Ordering {foodItem} for room {roomNumber}")

class CustomerRequests:
    def requestItem(self, roomNumber, item):
        print(f"Requesting {item} for room {roomNumber}")

class HotelManagement:
    hotel_room = {}  # 호텔 클래스만 가지고 있는 호텔 정보

    def __init__(self):
        self.__type_of_room= {'in_out':False , 'type':str("None"), 'id': int(-1), 'dinner': str("None"), 'request_item':str("None")}
        self.__current_room_id = self.__type_of_room['id']
        self.reservation = ReservationSystem()
        self.cleaning = CleaningService()
        self.dining = DiningService()
        self.requests = CustomerRequests()

        #만든 room 공유 키= room 번호, 값= 호텔 방 정보
        #방 번호는 101 부터 999까지 만든다.
        for room_number in range(101, 1000): HotelManagement.hotel_room[room_number]= self.__type_of_room.copy()


    def hotel_servise(self):
        #접근 가능한 호텔 서비스
        kernel = ''
        while True:
            print("호텔 명령 리스트")
            print("1: 예약 + 세팅, 2: 예약, 3.현재 관리할 방번호 지정, else. 종료")
            kernel = input("명령 입력: ")
            if kernel == '1': self.__reservation_room(input("룸 타입:")).__curstomer_requests().__dinner_choise()
            elif kernel == '2': self.__reservation_room(input("룸 타입:"))
            elif kernel == '3':
                self.__current_room_id = int(input("방 번호"))

                while True:
                    print("1:세팅, 2.방 정보, 3.청소 및 exit")
                    kernel = input(f"{self.__current_room_id}호의 관리 명령:")
                    if kernel=='1': self.__curstomer_requests().__dinner_choise()
                    elif kernel =='2': self.__check_and_set_hotel_room()
                    elif kernel =='3': self.__cleaning_room(); break

            else:
                print("시스템 종료")
                break

    def __check_and_set_hotel_room(self):
        if self.__current_room_id == -1: self.__current_room_id = int(input("호텔 방 번호"))

        if not self.__current_room_id in HotelManagement.hotel_room.keys():
            HotelManagement.hotel_room[self.__current_room_id] = self.__type_of_room['id'] = self.__current_room_id

        if HotelManagement.hotel_room[self.__current_room_id]["type"] == "None":
            HotelManagement.hotel_room[self.__current_room_id]["type"] = "Single"

        print(f"Hotel room number{self.__current_room_id}")
        print(HotelManagement.hotel_room[self.__current_room_id])


    #호텔 내부적 접근 가능 기능 private
    def __reservation_room(self, room_type:str):
        #내가 지정한 room형식이 호텔 룸 딕셔너리에 없다면 새로 임의의 방을 잡아 방을 만든다.
        #1. 먼저 지정한 룸 타입이 현재 호텔에 있는지 검색한다.
        # 검색한 방이 있으면 리스트에 방번호가 있을것이고 없으면 임의의 방을 잡는다.
        reser_room_list=[room_number for room_number, room_shape in HotelManagement.hotel_room.items()
                         #만약 지금 보는 방이 손님이 지정한 방형태와 맞고 방에 손님이 예약을 안했으면
                         if (room_shape['type'] == room_type or room_shape['type'] == "None") and room_shape['in_out']==False]

        #방을 예약 못하는 상황이면
        if len(reser_room_list)==0:
            print(f"현재 {room_type}형태의 룸 예약이 불가능합니다.")
            return

        #호텔 예약 정보 수정
        self.__current_room_id = reser_room_list[0]
        self.reservation.bookRoom(room_type)
        print(f"reservation room number {reser_room_list[0]}")
        self.__set_room_state(room_type, self.__current_room_id)

        return self

    def __set_room_state(self, room_type, room_number):
        HotelManagement.hotel_room[room_number]['type'] = room_type
        HotelManagement.hotel_room[room_number]['in_out'] = True
        HotelManagement.hotel_room[room_number]['id'] = room_number

    def __dinner_choise(self):
        self.__check_and_set_hotel_room()
        set_dinner = input("설정할 음식을 지정해주세요")
        HotelManagement.hotel_room['dinner'] =  set_dinner
        self.dining.orderFood(self.__current_room_id, set_dinner)
        return self


    def __curstomer_requests(self):
        self.__check_and_set_hotel_room()
        request_item = input("설정할 물건을 입력해주세요")
        HotelManagement.hotel_room['request_item']=request_item
        self.requests.requestItem(self.__current_room_id, request_item)
        return self

    def __cleaning_room(self):
        HotelManagement.hotel_room[self.__current_room_id] = self.__type_of_room
        self.cleaning.scheduleCleaning(self.__current_room_id)
        self.__current_room_id = self.__type_of_room['id']


if __name__ =='__main__':
    hotel = HotelManagement()
    hotel.hotel_servise()


#
# reservation.bookRoom("Deluxe")
# cleaning.scheduleCleaning(101)
# dining.orderFood(101, "Pizza")
# requests.requestItem(101, "ExtraPillow")
