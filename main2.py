import time
import random

print("""
  ___          _                    _   _____                         _               
 / _ \        (_)                  | | /  __ \                       (_)              
/ /_\ \ _ __   _  _ __ ___    __ _ | | | /  \/ _ __   ___   ___  ___  _  _ __    __ _ 
|  _  || '_ \ | || '_ ` _ \  / _` || | | |    | '__| / _ \ / __|/ __|| || '_ \  / _` |
| | | || | | || || | | | | || (_| || | | \__/\| |   | (_) |\__ \\__ \| || | | || (_| |
\_| |_/|_| |_||_||_| |_| |_| \__,_||_|  \____/|_|    \___/ |___/|___/|_||_| |_| \__, |
                                                                                 __/ |
                                                                                |___/ 
""")
print("~ 모여봐요 멋사의 숲 ~\n")


name = input("당신의 이름은?")
island = input("섬 이름은?")

print(name + "님 반가워요! " + island + "섬에 오신것을 환영합니다-!")
time.sleep(1)

animal = {'릴리안': 0, '탁호': 0, '미첼': 0, '리처드': 0}
my_bell = 3000
my_pocket = []
store = {'가습기': 1400, '강아지 인형': 2400, '강의실 책상': 2500, '몬스테라': 1700}

action_boolean = 1

# 4가지 반복하기
while action_boolean:
    print("\n어떤 것을 해볼까요?")
    answer_action = input("0. 종료 1. 상점가기 2. 주민 찾아가기 3. 나무 흔들기 4. 정보 확인하기 ")

    # 0. 게임 종료
    if answer_action == "0":
        print("게임을 종료합니다.")
        action_boolean = 0

    # 1. 상점가기를 선택한경우
    elif answer_action == "1":
        print("상점에 온 걸 환영해구리!")
        time.sleep(0.5)
        print("현재상점에는 이런 물건들이 있어구리")
        i=1
        for key,value in store.items():
            print("%d."%i,key,":",value,"벨")
            i+=1
            time.sleep(0.5)
        time.sleep(0.5)
        buy=int(input("어느물건을 구입하시겠어구리?(숫자로 입력)"))
        list_item=list(store.keys())
        list_price = list(store.values())
        if(my_bell>=list_price[buy-1]):
            print("\n")
            print(list_item[buy-1],"을(를)구매하셨습니다!")
            my_bell=my_bell-list_price[buy-1]
            print("남은 벨:", my_bell)
            my_pocket.append(list_item[buy-1])
            del store[list_item[buy-1]]
        else:
            print("돈이 부족합니다")

#돈부족하면 부족하다고 출력하기

    # 2. 주민 찾아가기를 선택한 경우
    elif answer_action == "2":
        print("우리 마을에 있는 주민이야")
        i=1
        for key,value in animal.items():
            print("%d."%i,key)
            i+=1
            time.sleep(0.5)

        meet=int(input("어떤 주민을 찾아갈까?"))
        list_animalname = list(animal.keys())
        print(list_animalname[meet-1]+"에게 무엇을 할까?")
        answer_animal_action = int(input("1.말걸기 2.선물하기 3.때리기"))


        # 2-1. 말걸기를 선택한경우
        if answer_animal_action == 1:
            if list_animalname[meet-1]=="릴리안":
                print("어머!",name,"잘 지냈어?");time.sleep(0.5)
                print("안에 들어와 간식이라도 먹고가~ 그렇지 뭐")
            elif list_animalname[meet-1]=="탁호":
                print("안녀엉~ %s아~ 반가워어~"%name);time.sleep(0.5)
                print("오늘 저녁은 뭘 먹을지 너무 고민이 돼~ 약히")
            elif list_animalname[meet - 1] == "미첼":
                print("%s아~!반가워! 오늘 날씨 되게 좋지않아?~"%name);time.sleep(0.5)
                print("마구마구 산책을 하고싶어져 동글")
            else:
                print("%s야아~!"%name);time.sleep(0.5)
                print("나무를 흔들었더니 100벨이 나왔어어~");time.sleep(0.5)
                print("%s도 한 번 흔들어봐아~ 그래유 "%name)
            animal[list_animalname[meet - 1]] += 1
            time.sleep(0.5)
            print(list_animalname[meet-1],"친밀도 +1")


        # 2-1. 선물하기를 선택한 경우
        elif answer_animal_action == 2:
            print("내 주머니엔 이렇게 있어\n")
            i=1
            for it in my_pocket:
                print("%d."%i,it)
                time.sleep(0.5)
            print("\n")
            time.sleep(0.5)
            present=int(input("어떤 것을 선물할까? (숫자로 입력) "));time.sleep(0.5)
            print(list_animalname[meet - 1]+"에게"+my_pocket[present-1]+"을(를) 선물했다!");time.sleep(0.5)
            del my_pocket[present-1]
            animal[list_animalname[meet - 1]]+= 5
            print(list_animalname[meet - 1], "친밀도 +5")

        # 2-3. 떄리기를 선택한 경우
        elif answer_animal_action == 3:
            print(list_animalname[meet - 1] +": 응..? 아야! 왜 그러는거야!");time.sleep(0.5)
            print(list_animalname[meet - 1] +"을(를) 때렸다!");time.sleep(0.5)
            animal[list_animalname[meet - 1]]-= 1
            print(list_animalname[meet - 1], "친밀도 -1")

    # 3. 나무 흔들기를 선택한 경우
    elif answer_action == "3":
        ran=["100벨","사과","벌"]
        result=random.choice(ran)
        # 100벨이 떨어질경우
        if result == "100벨":
            print("짤그랑");time.sleep(0.5)
            print("100벨을 획득하였습니다")
            my_bell+=100

        # 사과가 떨어질경우
        elif result == "사과":
            print("우르르");time.sleep(0.5)
            print("사과를 획들하였습니다")
            my_pocket.append("apple")


        # 벌이 나타날경우
        elif result == "벌":
            print("응...?");time.sleep(0.5)
            print("벌이 나타났습니다!");time.sleep(0.5)
            print("아야.. 벌에게 물렸어")



    # 4. 정보보기를 선택한 경우
    elif answer_action == "4":

    # 이름 출력
        print("-이름:",name)
        time.sleep(0.5)
    # 남은 벨 출력
        print("-남은 벨:", my_bell)
        time.sleep(0.5)
    # 주머니 출력
        print("-내 주머니:",end='')
        if not my_pocket:
            print("비어있음")
        else:
            for i in my_pocket:
                print(i)
                time.sleep(0.5)
    # 주민 친밀도 출력
        print("-주민과 친밀도:")
        for i in range(4):
            print("%d"%(1+i),list_animalname[i],":",animal[list_animalname[i]])
            time.sleep(0.5)

#친밀도 올려야해
    # 잘못된 입력을 했을경우
    else:
        print("1~4까지만 입력해주세요.")

