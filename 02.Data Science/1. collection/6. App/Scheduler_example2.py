import threading
import time
import ctypes

g_Balcony_windows=False
g_AI_Mode=False

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


def updata_scheduler():
    global g_Balcony_windows
    while True:
        if g_AI_Mode == False:
            continue
        else:
            time.sleep(5)
            g_Balcony_windows=not g_Balcony_windows



while True:
    print("메뉴를 선택하세요")
    print("1. 장비 상태 조회")
    print("2. 인공지능 모드 변경")
    print("3. 종료")

    menu_num= int(input("메뉴 입력: "))
    if(menu_num==1):
        print("발코니(베란다) 창문: ",end='')
        if g_Balcony_windows==True:
            print("열림")
        else:
            print("닫힘")
    elif(menu_num==2):
        print("인공지능 모드: ", end='')
        g_AI_Mode=not g_AI_Mode
        if g_AI_Mode==True:
            print("작동")
            ai_scheduler = threading.Thread(target=updata_scheduler)
            ai_scheduler.daemon = True
            ai_scheduler.start()
        else:
            while ai_scheduler.is_alive():
                try:
                    terminate_ai_mode()
                except:
                    pass
            print("정지")
    else:
        break