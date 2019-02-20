
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree, parse
import re


def sumup_xml():
    tree = parse("students_info.xml")  # 생성한 xml 파일 파싱하기
    note = tree.getroot()
    note.getiterator("student_list")

    for parent in tree.getiterator():
        ft = parent.findtext("student")
        if ft:
            print(ft)

    print("blog의 모든 속성 출력")
    print(note.findtext("student"))  # 리스트로 출력된다.
    print("subject 내용 출력")
    # to_tag = note.find("data")
    # print(to_tag.text)





def whole_xml():
    tree = parse("students_info.xml")  # 생성한 xml 파일 파싱하기
    note = tree.getroot()
    # dump(tree.getiterator())
    # note.getiterator("student_list")
    for parent in note.getiterator("student"):
        z = re.compile(".")
        c = z.search(parent)
        print(c)
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


whole_xml()

# while True:
#     print("학생정보 XML데이터 분석 시작..")
#     input_data=input("1.요약정보 \n2.전체데이터 조회 \n3.종료 \n메뉴입력: ")
#     if input_data=='3':
#         quit()
#     elif input_data=='2':
#         sumup_xml()
#     elif input_data == '1':
#         whole_xml()