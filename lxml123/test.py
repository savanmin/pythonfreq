# # # import _elementtree
# # # print(dir(_elementtree))
# # #
# # #
# #
import xml.etree.cElementTree as ET
from lxml import etree

# print(dir(etree))



doc = etree.parse("setup123.xml")
code = doc.findall("heading")
# print (dir(code[0]))
print(code[0])