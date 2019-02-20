
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree, parse
import re

age=[]
def sumup_xml():
    tree = parse("students_info.xml")  # 생성한 xml 파일 파싱하기
    note = tree.getroot()
    count=0

    for parent in note.getiterator("student"):
        age.append(parent.get("age"))
        print("- 성별: %s" % parent.get("sex"))
        print("- 전공: %s" % parent.findtext("age"))
        print("- 전공: %s" % parent.findtext("major"))
        for pr_lang in parent.getiterator("language"):
            if pr_lang:
                for period_value in pr_lang.getiterator("period"):
                    print("> %s 학습기간:%s,level:%s" % (
                    pr_lang.get("name"), period_value.get("value"), pr_lang.get("level")))

        count+=1

    print("전체 학생수:%d"%count)
    print(note.findtext("student"))  # 리스트로 출력된다.
    print("subject 내용 출력")
    # to_tag = note.find("data")
    # print(to_tag.text)


def whole_xml():
    tree = parse("students_info.xml")  # 생성한 xml 파일 파싱하기
    note = tree.getroot()
    for parent in note.getiterator("student"):
        print("* %s"%parent.get("name"))
        print("- 성별: %s"%parent.get("sex"))
        print("- 나이: %s"%parent.findtext("age"))
        print("- 전공: %s"%parent.findtext("major"))
        for pr_lang in parent.getiterator("language"):
            if pr_lang:
                for period_value in pr_lang.getiterator("period"):
                    print("> %s 학습기간:%s,level:%s"%(pr_lang.get("name"),period_value.get("value"),pr_lang.get("level")))
        print("----------------------")



def indent(elem, level=0):
    i="\n"+ level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + " "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
           elem.tail=i


sumup_xml()

# while True:
#     print("학생정보 XML데이터 분석 시작..")
#     input_data=input("1.요약정보 \n2.전체데이터 조회 \n3.종료 \n메뉴입력: ")
#     if input_data=='3':
#         quit()
#     elif input_data=='2':
#         sumup_xml()
#     elif input_data == '1':
#         whole_xml()