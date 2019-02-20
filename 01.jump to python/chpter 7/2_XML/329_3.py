from xml.etree.ElementTree import Element, dump, SubElement

note=Element("note", date="20120104")
to=Element("tos") #자식 노드
to.text="Tove"
note.append(to)
SubElement(note,"from").text="Jani"

dump(note)

