import pickle

# 체크
def check_item(item, temp_inventory):
    return item in temp_inventory


# 1.아이템 추가
def add_item(item, amount, temp_inventory):
    if check_item(item, temp_inventory):
        temp_inventory[item] += Amount
        print(item + "의 수량은 ", str(temp_inventory[item]) + "입니다.")
    else:
        temp_inventory[item] = amount
        print(item + "이 추가되었습니다.")


# 2.아이템 버림
def remove_item(item, temp_inventory):
    if check_item(item, temp_inventory):
        temp_inventory[item] = 0
        print(item + "의 수량이 0이 되었습니다.")
    else:
        print(item + "이 존재하지 않습니다.")


# 4.아이템 사용
def consume_item(item, amount, temp_inventory):
    if temp_inventory[item] < 1:
        print(item + "의 수량이 부족함.")
    elif check_item(item, temp_inventory):
        temp_inventory[item] -= amount
        print(item + "을 사용하셨습니다.")
        print(item + "의 수량은 ", str(temp_inventory[item]) + "입니다.")

#아이템 매뉴
def print_imenu():
    print("0.끝내기")
    print("1.아이템 추가")
    print("2.아이템 삭제")
    print("3.아이템 확인")
    print("4.아이템 사용")

#아이템 매뉴 함수
def use_item(inventory):
    while True:
        print_imenu()
        option: int = int(input("메뉴 번호를 입력하세요)"))
        if option == 0:
            print("인벤토리를 종료합니다.")
            break
        elif option == 1:
            new_item = input("아이템을 입력하세요.)")
            amount = int(input("수량을 입력하세요.)"))
            add_item(new_item, amount, inventory)
        elif option == 2:
            del_item = input("아이템을 입력하세요.)")
            remove_item(del_item, inventory)
        elif option == 3:
            print(inventory)
        elif option == 4:
            use_item = input("아이템을 입력하세요.)")
            amount = int(input("수량을 입력해주세요.)"))
            consume_item(use_item, amount, inventory)
        else:
            print("잘못된 번호를 입력하셨습니다.")
#try 사용해보기
#try:
#    print("저장된 파일을 읽어왔습니다.")
#    load_file = open("game_file.p", "rb")
#    character = pickle.load(load_file)
#    load_file.close()
#    select_character = None
#except:
#    print("저장된 파일이 없습니다.")
#    character = {}


#os 사용해보기
import os
if os.path.isfile("game_save.p"):
    load_file = open("game_save.p","rb")
    charater = pickle.load(load_file)
    load_file.close()
    print("저장된 파일을 읽어왔습니다.")
else:
    print("읽어올 파일이 없습니다.")
    charater = {}

#캐릭터 리턴
def check_character(name, t_character):
    return name in t_character


#캐릭터 생성
def new_character(name, t_character):
    if name in t_character:
        print("이미 존재하는 캐릭터의 이름입니다.")
    else:
        inventory = {}
        t_character[name] = inventory



#캐릭터 매뉴 출력
def print_character():
    print("0.저장하고 끝내기")
    print("1.캐릭터 추가")
    print("2.캐릭터 이름 출력")
    print("3.캐릭터 선택")
    print("4.캐릭터 인벤토리 조작")

#캐릭터 매뉴 함수
while True:
    print_character()
    option = int(input("매뉴를 입력하세요)"))
    if option == 0:
        save_file = open("game_save.p", "wb")
        pickle.dump(character, save_file)
        print("게임 내용이 저장되었습니다.")
        print("종료되었습니다.")
        break
    elif option == 1:
        name = input("캐릭터 이름을 입력하세요)")
        new_character(name, character)
    elif option == 2:
        i = 1
        print("-------------------------------")
        for name in character.keys():
            print(str(1) + "." + name)
            i += 1
        print("-------------------------------")
    elif option == 3:
        temp_name = input("선택할 캐릭터의 이름을 입력해주세요.)")
        if check_character(temp_name, character):
            select_character = temp_name
            print(select_character + "이/가 선택되었습니다.")
        else:
            print(temp_name + "는 존재하지 않는 캐릭터입니다.")
    elif option == 4:
        if select_character == None:
            print("3번 매뉴로 캐릭터를 선택해주세요.")
        else:
            print("선택된 캐릭터는" + select_character + "입니다.")
            inventory = character[select_character]
            use_item(inventory)

# 캐릭터 장착기능
