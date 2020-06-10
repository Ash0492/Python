import xml.etree.ElementTree as ET

input = ''' 
<stuff>
<users>
<user x='2'>
<id>001</id>
<name>Aishwarya</name>
</user>
<user x='7'> 
<id> 009 </id>
<name> Shreya </name>
</user>
</users>
</stuff> '''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('usercount', len(lst))

for item in lst:

    print('Name', item.find('name').text)
    print('id', item.find('id').text)
    print('Attribute', item.get('x'))