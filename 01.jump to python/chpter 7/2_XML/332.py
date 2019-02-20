from xml.etree.ElementTree import parse, Element, dump, SubElement ,ElementTree
tree=parse("note.xml")
note=tree.getroot()

print(note.get("data"))
print(note.get("from"))
print(note.get("foo","default"))
print(note.keys()) #현재노드의 속성을 가르킨다
print(note.items()) #노드의 속성과 값을 나타낸다

from_tag=note.find("from")
from_tags=note.findall("from")
from_text=note.findtext("from")


dump(from_tag)
dump(from_tags)
dump(from_text)

# childs = note.getiterator()
# print(childs)
# childs = note.getchildren()
# print(childs)