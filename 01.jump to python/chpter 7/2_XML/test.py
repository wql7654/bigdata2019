# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
tree = ET.parse('x.xml')
root = tree.getroot()
AAA = root.findall('AAA')  # 모든 AAA를 찾음.
BBB_below_CCC_list = [a.findall('CCC/BBB') for a in AAA]  #  모든 AAA를 돌면서 자식중에 CCC 아래의 BBB들을 찾음.


for c in BBB_below_CCC_list:  # CCC아래의 BBB리스트를 돌면서
    if len(c) > 1:  # 엘리먼트가 2개 이상일 경우.
        _text = ''.join([each.text for each in c])  # 한줄로 합침.
        print(_text)
    else:  # 엘리먼트가 한개인 경우 그냥 출력함.
        print(c[0].text)