from xml.etree.ElementTree import Element, dump, SubElement

note=Element("note")
note.attrib["data"]="20120104"

to=Element("tos") #자식 노드
to.text="Tove"
note.append(to)


SubElement(note,"from").text="Jani"
SubElement(note,"heading").text="Reminder"
SubElement(note,"body").text="Don't forget me this weekend!"

dump(note)

