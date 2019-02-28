import json
import re
import os
import glob

g_Radiator = False
g_Gas_Value = False
g_Balcony_Window = False
g_Door = False
g_AI_Mode = False

def print_main_menu():
    print('\n1. 장비상태 확인')
    print('2. 장비제어')
    print('3. 스마트모드')
    print('4. 프로그램 종료')
    print('*********************************************')

def print_device_status(device_name, devcie_status):
    print('%s 상태: ' %device_name, end='')
    if devcie_status == True : print('작동')
    else: print('정지')

def check_device_status():
    print_device_status('난방기', g_Radiator)
    print_device_status('가스밸브', g_Gas_Value)
    print_device_status('발코니(베란다) 창문', g_Balcony_Window)
    print_device_status('출입문 상태', g_Door)

def print_device_menu():
    print('\n상태 변경할 기기를 선택하세요.')
    print('1. 난방기')
    print('2. 가스밸브')
    print('3. 발코니(베란다)창')
    print('4. 출입문')

def control_device():
    global g_Radiator, g_Gas_Value, g_Balcony_Window, g_Door
    check_device_status()
    print_device_menu()
    menu_num = int(input('번호를 입력하세요: '))

    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Value = not g_Gas_Value
    if menu_num == 3: g_Balcony_Window = not g_Balcony_Window
    if menu_num == 4: g_Door = not g_Door
    check_device_status()

def get_realtime_weather_info():
    file_folder=glob.glob('./동구*' )
    all2 = re.compile('_([0-9]+)')
    ss=all2.search(str(file_folder))
    with open('동구_신암동_초단기예보조회%s.json'%str(ss[0]), encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_big_data = json.loads(json_string)

    print('실시간 기상정보를 확인합니다.')
    fcstTime = 0; REH_value = 0
    for data in json_big_data:
        if data['category'] == 'REH':
            if fcstTime < data['fcstTime']:
                REH_value = data['fcstValue']

    print('습도는 %s입니다.' %REH_value)
    if 40 <= REH_value <= 60:
        print('습도가 정상입니다.')
    elif REH_value < 40:
        print('정상습도보다 낮습니다. \n가습기를 작동하겠습니까?')
    elif REH_value > 40:
        print('정상습도보다 높습니다. \n제습기를 작동하겠습니까?')

def smart_mode():
    global g_AI_Mode
    print('1. 인공지능 모드 조회')
    print('2. 인공지능 모드 상태 변경')
    print('3. 실시간 기상정보 Update')
    menu_num = int(input('메뉴를 선택하세요: '))

    if menu_num == 1:
        print('현재 인공지능 모드: ', end='')
        if g_AI_Mode == True: print('작동')
        else: print('중지')
    if menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print('현재 인공지능 모드: ', end='')
        if g_AI_Mode == True: print('작동')
        else: print('중지')
    elif menu_num == 3:
        get_realtime_weather_info()

print('<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>')
print('                              - 이현구 -')
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
        break