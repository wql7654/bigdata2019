from xml.etree.ElementTree import Element, dump, SubElement

note=Element("note")
to=Element("tos") #자식 노드
to.text="Tove"
note.append(to)

SubElement(note,"from").text="Jani"
note.attrib["data"]="20120104"

dump(note)

