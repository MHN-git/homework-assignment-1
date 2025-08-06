import xmltodict
import json


def formatAdapter(data):
    data_dict = xmltodict.parse(data)
    return json.dumps(data_dict)


with open('data.xml', 'r') as xml_file:
    xml_data = xml_file.read()

json_data = formatAdapter(xml_data)
print(json_data)

