"""
xml 은 과거에 주로 사용하던 정보 교환 데이터
최근에는 json 을 이용한 데이터 교환이 더 이루어 지고 있음 [데이터 양이 적어서 빠르게 전송할 수 있음]
"""

import xml.etree.ElementTree as ET

root = ET.Element('root')
tree = ET.ElementTree(element=root)

employee = ET.SubElement(root, 'employee')

employ = ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '111'
employ_id = ET.SubElement(employ, 'name')
employ_id.text = 'Mike'


employ = ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '222'
employ_id = ET.SubElement(employ, 'name')
employ_id.text = 'Nancy'

tree.write('test.xml', encoding='utf-8', xml_declaration=True)

# 내용 확인
tree = ET.ElementTree(file='test.xml')
root = tree.getroot()

for employee in root:
    for employ in employee:
        for person in employ:
            print(person.tag, person.text)



