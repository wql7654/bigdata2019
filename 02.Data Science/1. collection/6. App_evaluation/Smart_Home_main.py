import glob
import threading
import ctypes
from smart_Home_weather_data import *
from upbit_service import *




g_Radiator = False
g_Gas_Value = False
g_Balcony_windows = False
g_Door = False
g_AI_Mode = False
g_save_Mode=False
g_air_condition = False
g_humidifier = False
g_dehumidifier = False
mode_ta = '정지'
mode_ti = '정지'

def print_main_menu():
    print('\n1. 장비상태 확인')
    print('2. 장비제어')
    print('3. 스마트모드')
    print('4. 오늘의뉴스')
    print('5. 코인관리 서비스')
    print('6. 프로그램 종료')
    print('*********************************************')

def print_device_status(device_name, devcie_status):
    print('%s 상태: ' %device_name, end='')
    if devcie_status == True : print('작동')
    else: print('정지')

def check_device_status():
    print_device_status('난방기', g_Radiator)
    print_device_status('가스밸브', g_Gas_Value)
    print_device_status('발코니(베란다) 창문', g_Balcony_windows)
    print_device_status('출입문 상태', g_Door)
    print_device_status('공기청정기 상태', g_air_condition)
    print_device_status('가습기 상태', g_humidifier)
    print_device_status('제습기 상태', g_dehumidifier)

def print_device_menu():
    print('\n상태 변경할 기기를 선택하세요.')
    print('1. 난방기')
    print('2. 가스밸브')
    print('3. 발코니(베란다)창')
    print('4. 출입문')
    print('5. 공기청정기')
    print('6. 가습기')
    print('7. 제습기')



def control_device():
    global g_Radiator, g_Gas_Value, g_Door,g_Balcony_windows, g_air_condition,g_humidifier,g_dehumidifier
    check_device_status()
    print_device_menu()
    menu_num = int(input('번호를 입력하세요: '))

    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Value = not g_Gas_Value
    if menu_num == 3: g_Balcony_windows = not g_Balcony_windows
    if menu_num == 4: g_Door = not g_Door
    if menu_num == 5: g_air_condition = not g_air_condition
    if menu_num == 6: g_humidifier = not g_humidifier
    if menu_num == 7: g_dehumidifier = not g_dehumidifier
    check_device_status()

def get_realtime_weather_info():
    global g_humidifier,g_Truedehumidifier,g_air_condition,g_Radiator
    main_weather()

    file_folder=glob.glob('./동구*' )
    all2 = re.compile('_([0-9]+)')
    ss=all2.search(str(file_folder))
    with open('동구_신암동_초단기예보조회%s.json'%str(ss[0]), encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)

    with open("인공지능모드 저장데이터.csv", 'r') as f:
        all_value=''
        while True:
            c_line = f.readline()
            if not c_line: break
            all_value=c_line.split(',')
    dust_value = all_value[6]
    temp_value = int(all_value[2][:2])

    print('실시간 기상정보를 확인합니다.')
    fcstTime = 0; REH_value = 0
    for data in json_big_data:
        if data['category'] == 'REH':
            if fcstTime < data['fcstTime']:
                REH_value = data['fcstValue']

    print('오늘은 온도는 %s입니다.' % dust_value)
    if temp_value <= 15:
        print('온도가 15도 이하 입니다.')
        hi_temp=input("난방기를 작동하겠습니까?(y/n)")
        if hi_temp=='y': g_Radiator=True
    elif temp_value >= 22:
        print('온도가 22도 보다 높습니다.')
        print("난방기를 중단하겠습니다")
        g_Radiator=False

    print('습도는 %s입니다.' %REH_value)
    if 40 <= REH_value <= 60:
        print('습도가 정상입니다.')
    elif REH_value < 40:
        print('정상습도보다 낮습니다.')
        ga_air=input("가습기를 작동하겠습니까?(y/n)")
        if ga_air=='y': g_humidifier=True

    elif REH_value > 40:
        print('정상습도보다 높습니다.')
        ga_airs = input("제습기를 작동하겠습니까?(y/n)")
        if ga_airs=='y': g_Truedehumidifier=True

    print('오늘은 미세먼지등급은 %s입니다.' % dust_value)
    if dust_value =='매우나쁨' or  dust_value =='나쁨':
        print('공기가 많이 좋지않습니다.')
        ga_air=input("공기청정기 작동하겠습니까?(y/n)")
        if ga_air=='y': g_air_condition=True




def updata_scheduler():
    global g_Balcony_windows
    global g_Door
    global g_Gas_Value
    global g_Radiator
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0

    while True:
        time.sleep(1)
        count1+=1
        count2+=1
        count3+=1
        count4+=1

        if g_Balcony_windows:
            if count1==3600 :
                g_Balcony_windows=False
        else:
            count1=0
        if g_Door:
            if count2==100 :
                g_Door=False
        else:
            count2=0
        if g_Gas_Value:
            if count3==600 :
                g_Gas_Value=False
        else:
            count3=0
        if g_Radiator:
            if count4==3600 :
                g_Radiator=False
        else:
            count4=0



def scheduler_saved():

    while True:
        if time.strftime("%M%S") == "4530":
            day_time = time.strftime("%H%M", time.localtime(time.time()))
            data_saved_csv(day_time)
            time.sleep(10)
        else:
            continue

def terminate_ai_mode():
    """Terminates a python thread from another thread.
    :param thread: a threading.Thread instance
    """
    if not ai_scheduler.isAlive():
        return
    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(ai_scheduler.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ai_scheduler.ident, None)
        raise SyntaxError("PyThreadState_SetAsyncExc failed")


def terminate_ai_mode2():
    """Terminates a python thread from another thread.
    :param thread: a threading.Thread instance
    """
    if not ai_scheduler2.isAlive():
        return
    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(ai_scheduler2.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ai_scheduler2.ident, None)
        raise SyntaxError("PyThreadState_SetAsyncExc failed")


def upbit_order_scheduler():
    global g_air_condition
    while True:
        if g_AI_Mode == False:
            continue
        else:
            time.sleep(5)
            # if 매매가 > 현재가15퍼-
            #     sell
            # else 현재가15퍼 > 매매가
            #     sell
            #     coinservice=not coinservice



def intelligence_service():
    global ai_scheduler
    global ai_scheduler2
    global g_save_Mode
    global g_AI_Mode
    global g_save_Mode
    global mode_ti
    global mode_ta
    while True:
        print("1.장비 인공지능모드\n2.데이터 자동저장모드\n3.뒤로가기")
        menu_num= int(input("메뉴 입력: "))
        if(menu_num==1):

            if g_AI_Mode: mode_ta='작동'
            else: mode_ta='정지'
            print("지금 인공지능모드가 %s중입니다 "%mode_ta)
            menu_sel = input("인공지능모드 켜시겠습니까?(y/n): ")

            if menu_sel == 'y':
                mode_ta = '작동'
                g_AI_Mode=True
                ai_scheduler = threading.Thread(target=updata_scheduler)
                ai_scheduler.daemon = True
                ai_scheduler.start()
            elif menu_sel == 'n':
                mode_ta = '정지'
                g_AI_Mode=False
                while ai_scheduler.is_alive():
                    try:
                        terminate_ai_mode()
                    except:
                        pass


        elif(menu_num==2):

            if g_save_Mode: mode_ti='작동'
            else: mode_ti='정지'
            print("지금 자동저장모드가 %s중입니다 "%mode_ti)
            menu_sel = input("자동저장모드 켜시겠습니까?(y/n): ")

            if menu_sel == 'y':
                mode_ta = '작동'
                g_save_Mode=True
                ai_scheduler2 = threading.Thread(target=scheduler_saved)
                ai_scheduler2.daemon = True
                ai_scheduler2.start()
            elif menu_sel == 'n':
                mode_ti = '정지'
                g_save_Mode=False
                while ai_scheduler2.is_alive():
                    try:
                        terminate_ai_mode2()
                    except:
                        pass
        else:
            break




def smart_mode():
    print('1. 인공지능 모드 조회')
    print('2. 인공지능 모드 상태 설정')
    print('3. 실시간 기상정보 Update')
    menu_num = int(input('메뉴를 선택하세요: '))

    if menu_num == 1:

        print('인공지능모드:%s'%mode_ta)
        print('자동저장모드모드:%s'%mode_ti)

    if menu_num == 2:
        intelligence_service()
    elif menu_num == 3:
        get_realtime_weather_info()

print('<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>')
print('                              - 이정헌 -')
while True:
    print_main_menu()
    menu_num = int(input('메뉴를 선택하세요: '))

    if menu_num == 1:
        check_device_status()
    elif menu_num == 2:
        control_device()
    elif menu_num == 3:
        smart_mode()
    elif menu_num == 4:
        crawring_data()
    elif menu_num == 5:
        coin_main()
    elif menu_num == 6:
        break