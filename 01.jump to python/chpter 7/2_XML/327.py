from xml.etree.ElementTree import Element, dump

note=Element("note")
to=Element("tos") #자식 노드
to.text="Tove" #현재 엘리먼트(tag)에 값 추가
note.append(to) #부모노드에 자식노드 추가

dump(note)  ##xml을 출력하는 함수
dump(to)