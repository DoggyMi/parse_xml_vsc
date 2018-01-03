from xml.etree.ElementTree import parse
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring
import html
import csv

"""
1.将默认的strings.xml复制到同级目录下
2.参照transform.csv,将翻译给的excel转成csv,处理编码复制到同级目录下
3.执行代码
注意:strings.xml中不同的name有相同的value,需要手动处理
"""


def generate_xml(file_name, index_num):
    real_name = "result" + file_name + ".xml"
    with open(real_name, "w", encoding="utf-8") as g_file:
        elem = Element("resources")
        for name in index_list:
            child = Element("string")
            attr_dict = {"name": name}
            child.attrib = attr_dict
            try:
                child.text = str(data_dict[index_dict[name]][index_num])
                elem.append(child)
            except Exception as e:
                print(file_name + "翻译,没有" + str(e))

        data = str(tostring(elem), encoding="utf-8")
        g_file.write(html.unescape(data))


index_dict = {}
index_list = []
data_dict = {}
with open("strings.xml", "r", encoding="utf-8") as file:
    doc = parse(file)
    for item in doc.getroot():
        index_list.append(item.attrib.get("name"))
        index_dict[item.attrib.get("name")] = item.text

with open("transform.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        data_dict[row[0]] = row
    for item in headers:
        generate_xml(item, headers.index(item))
