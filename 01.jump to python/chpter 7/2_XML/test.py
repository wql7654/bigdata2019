
from xml.etree.ElementTree import parse, Element, dump, SubElement, ElementTree

tree = parse("students_info.xml")  # 생성한 xml 파일 파싱하기
note = tree.getroot()
# note.find("student_list/student").text='name'
# elem.set('yes', 'no')

# print(elem)
# dump()


i='123006'
print(int(i[-3:]))
# for parent in note.getiterator("student"):
#     if(parent.get("ID")=='ITT001'):
#         sh =parent.find('age')
#         parent.find('age').text='hi'
#         sh.set('name', 'no')
#         parents = parent.getparent()
        # note.remove(parent)
# dump(note)

# ElementTree(note).write("students_info_2.xml", encoding='UTF-8', xml_declaration=True)