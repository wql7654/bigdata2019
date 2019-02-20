from xml.etree.ElementTree import Element, dump, SubElement, ElementTree

note=Element("blog")
note.attrib["data"]="20151231"


SubElement(note,"subject").text="Why python?"
SubElement(note,"author").text="Eric"
SubElement(note,"content").text="Life is too short, You need Python!"

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
ElementTree(note).write("tree.xml")

