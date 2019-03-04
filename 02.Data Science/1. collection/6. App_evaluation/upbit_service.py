import json
import time
import requests
import jwt
import logging
from urllib.parse import urlencode
import urllib.request
from bs4 import BeautifulSoup
import re
import threading
import ctypes




class Upbitpy():
    # 업비트 개발자센터 https://docs.upbit.com/v1.0/reference

    def __init__(self):
        self.access_key = "KCTLlGysZ9ZhXhXnxLxCh1Mqnxv9JRDvoF8PPwhO"
        self.secret = "rdWgfDQbVt1EfoAHbuWPsJprNDmm5bygRgrv5Brp"
        self.markets = self._load_markets()


    def get_accounts(self): #계좌조회
        URL = 'https://api.upbit.com/v1/accounts'
        return self._get(URL, self._get_headers())

    def _load_markets(self):
        try:
            market_all = self.get_market_all()
            if market_all is None:
                return
            markets = []
            for market in market_all:
                markets.append(market['market'])
            return markets
        except Exception as e:
            logging.error(e)
            raise Exception(e)

    def get_market_all(self): #전체코인조회
        URL = 'https://api.upbit.com/v1/market/all'
        return self._get(URL)

    def get_market_ticket(self,coins):
        URL = "https://api.upbit.com/v1/ticker"
        querystring = {"markets": "KRW-"+coins}
        # response = requests.request("GET", url, params=querystring)
        return self._get(URL,params = querystring)

    def order(self, market, side, volume, price):
        '''
        주문하기
        주문 요청을 한다.
        https://docs.upbit.com/v1.0/reference#%EC%A3%BC%EB%AC%B8%ED%95%98%EA%B8%B0-1
        :param str market: 마켓 ID (필수)
        :param str side: 주문 종류 (필수)
            bid : 매수
            ask : 매도
        :param str volume: 주문량 (필수)
        :param str price: 유닛당 주문 가격. (필수)
            ex) KRW-BTC 마켓에서 1BTC당 1,000 KRW로 거래할 경우, 값은 1000 이 된다.
        :return: json object
        '''
        URL = 'https://api.upbit.com/v1/orders'
        if market not in self.markets:
            logging.error('invalid market: %s' % market)
            raise Exception('invalid market: %s' % market)

        if side not in ['bid', 'ask']:
            logging.error('invalid side: %s' % side)
            raise Exception('invalid side: %s' % side)

        if market.startswith('KRW') and not self._is_valid_price(price):
            logging.error('invalid price: %.2f' % price)
            raise Exception('invalid price: %.2f' % price)

        data = {
            'market': market,
            'side': side,
            'volume': str(volume),
            'price': str(price),
            'ord_type': 'limit'
        }
        return self._post(URL, self._get_headers(data), data)

    def _post(self, url, headers, data):
        resp = requests.post(url, headers=headers, data=data)
        if resp.status_code not in [200, 201]:
            logging.error('post(%s) failed(%d)' % (url, resp.status_code))
            if resp.text is not None:
                raise Exception('request.post() failed(%s)' % resp.text)
            raise Exception(
                'request.post() failed(status_code:%d)' % resp.status_code)
        return json.loads(resp.text)

    def _is_valid_price(self, price):
        '''
        원화 마켓 주문 가격 단위
        원화 마켓은 호가 별 주문 가격의 단위가 다릅니다. 아래 표를 참고하여 해당 단위로 주문하여 주세요.
        https://docs.upbit.com/v1.0/docs/%EC%9B%90%ED%99%94-%EB%A7%88%EC%BC%93-%EC%A3%BC%EB%AC%B8-%EA%B0%80%EA%B2%A9-%EB%8B%A8%EC%9C%84
        ~10         : 0.01
        ~100        : 0.1
        ~1,000      : 1
        ~10,000     : 5
        ~100,000    : 10
        ~500,000    : 50
        ~1,000,000  : 100
        ~2,000,000  : 500
        +2,000,000  : 1,000
        '''
        if price <= 10:
            if (price * 100) != int(price * 100):
                return False
        elif price <= 100:
            if (price * 10) != int(price * 10):
                return False
        elif price <= 1000:
            if price != int(price):
                return False
        elif price <= 10000:
            if (price % 5) != 0:
                return False
        elif price <= 100000:
            if (price % 10) != 0:
                return False
        elif price <= 500000:
            if (price % 50) != 0:
                return False
        elif price <= 1000000:
            if (price % 100) != 0:
                return False
        elif price <= 2000000:
            if (price % 500) != 0:
                return False
        elif (price % 1000) != 0:
            return False
        return True



    def _get(self, url, headers=None, data=None, params=None): #데이터 파싱
        resp = requests.get(url, headers=headers, data=data, params=params)
        if resp.status_code not in [200, 201]:
            logging.error('get(%s) failed(%d)' % (url, resp.status_code))
            if resp.text is not None:
                logging.error('resp: %s' % resp.text)
                raise Exception('request.get() failed(%s)' % resp.text)
            raise Exception(
                'request.get() failed(status_code:%d)' % resp.status_code)
        return json.loads(resp.text)

    def _get_headers(self, query=None):
        headers = {'Authorization': 'Bearer %s' % self._get_token(query)}
        return headers

    def _get_token(self, query): #암호화
        payload = {
            'access_key': self.access_key,
            'nonce': int(time.time() * 1000),
        }
        if query is not None:
            payload['query'] = urlencode(query)
        return jwt.encode(payload, self.secret, algorithm='HS256').decode('utf-8')


def board_crawling():
    html = urllib.request.urlopen('https://gall.dcinside.com/board/lists/?id=bitcoins')
    soup = BeautifulSoup(html, 'html.parser')
    all3 = re.compile('''icon_\w+"></\w+>(.+)</a>\s+</td>''')  # 게시판 크롤링
    allline = all3.findall(str(soup), re.MULTILINE | re.DOTALL | re.VERBOSE)
    print(allline)

def all_coin():
    allcoin=Upbitpy().get_market_all()
    for i in allcoin:
        all3 = re.compile("""KRW.(.+)""")
        allline = all3.findall(str(i['market']))
        if allline:
            print("이름:%s"%i['korean_name'],end='\t\t')
            print("코인명:%s"%allline[0])

    print("-" * 30)

def coin_view():
    coin_str = str(input('코인명을 입력해주세요: ')).upper()
    coinview = Upbitpy().get_market_ticket(coin_str)
    print("코인명:%s"% coinview[0]["market"])
    print("현재가:%s원" % coinview[0]["trade_price"])
    print("고가:%s원" % coinview[0]["high_price"])
    print("저가:%s원" % coinview[0]["low_price"])
    print("시가:%s원" % coinview[0]["opening_price"])
    print("24시간 누적거래대금:%0.1f원"% coinview[0]["acc_trade_price_24h"])
    print("-"*30)

def market_price():
    while True:
        print("1.전체코인조회(KRW)\n2.지정코인시세조회\n3.되돌아가기")
        menu_num = int(input('메뉴를 선택하세요: '))
        if menu_num == 1:
            all_coin()
        elif menu_num == 2:
            coin_view()
        elif menu_num == 3:
            break


def trade_service():
    while True:
        print("1.매수(KRW)\n2.매도(KRW)\n3.되돌아가기")
        menu_num = int(input('메뉴를 선택하세요: '))
        if menu_num == 1:
            trade_coin("bid")
        elif menu_num == 2:
            trade_coin("ask")
        elif menu_num == 3:
            break

def trade_coin(side):
    print("거래할 코인명,거래할 갯수,가격을 적어주세요")
    market = 'KRW-'+str(input('코인명을 적어주세요(영어이름): ')).upper()
    volume = float(input('거래할 갯수를 적어주세요(코인의갯수): '))
    price = float(input('거래할 가격를 적어주세요(코인의가격): '))
    Upbitpy().order(market, side, volume, price)


def coin_management():
    wallet=Upbitpy().get_accounts()
    for wal_info in wallet:
        print("코인명:%s"%wal_info['currency']) # 코인명
        print("보유코인갯수:%s"%wal_info['balance']) # 보유코인갯수
        print("현재 주문량:%s"%wal_info['locked'])  # 현재 주문량
        print("매수 평균가:%s"%wal_info['avg_krw_buy_price']) #매수 평균가


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


g_AI_Mode=False

def updata_scheduler():
    global g_Balcony_windows
    while True:
        if g_AI_Mode == False:
            continue
        else:
            time.sleep(5)
            g_Balcony_windows=not g_Balcony_windows


def intelligence_mode():
    print("1.실시간 코인조회 서비스 \n2.인공지능 매도 서비스 \n")
    mode_sel = input('메뉴를 선택하세요: ')
    #         if menu_num == 1:
    #             market_price()
    #         elif menu_num == 2:
    #             trade_service()
    #         elif menu_num == 3:
    #             coin_management()
    #         elif menu_num == 4:
    #             intelligence_mode()
    #         elif menu_num == 5:
    #             quit()


def intelligence_order():
    mode_on = input('메뉴를 선택하세요: ')
    global ai_scheduler
    if mode_on:
        ai_scheduler = threading.Thread(target=updata_scheduler)
        ai_scheduler.daemon = True
        ai_scheduler.start()

    else:
        while ai_scheduler.is_alive():
            try:
                terminate_ai_mode()
            except:
                pass




coin_management()



print("upbit 인공지능 코인 서비스 시뮬레이터")
print("                         -by이정헌")
# while True:
#     while True:
#         print("1.시세조회\n2.트레이딩\n3.자산관리\n4.인공지능 서비스\n5.종료")
#         menu_num = int(input('메뉴를 선택하세요: '))
#
#         if menu_num == 1:
#             market_price()
#         elif menu_num == 2:
#             trade_service()
#         elif menu_num == 3:
#             coin_management()
#         elif menu_num == 4:
#             intelligence_mode()
#         elif menu_num == 5:
#             quit()

# with open("test_coin.json", 'w') as f:
#     f.write(str(name_food.get_accounts()))

# name_food=Upbitpy()
# print(name_food.get_accounts())