from xml.etree.ElementTree import Element, dump, SubElement

note=Element("note")
note.attrib["data"]="20120104"
to=Element("to") #자식 노드
to.text="Tove"
note.append(to)


SubElement(note,"from").text="Jani"
SubElement(note,"heading").text="Reminder"
SubElement(note,"body").text="Don't forget me this weekend!"

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
indent(note)
dump(note)