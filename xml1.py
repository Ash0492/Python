import xml.etree.ElementTree as ET
data = '''
    <person>
        <name>Aishwarya</name>
        <phone type= 'intl'>
        </phone>
        <email hide="yes"/>
    </person> '''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Email:', tree.find('email').get('hide'))