from bs4 import BeautifulSoup
import xml.etree.ElementTree as et

tree = et.ElementTree(file='curriculo.xml')
root = tree.getroot()

e = list(root)[1][4]

f  = open("Outras produções bibliográficas.txt", "w")

for outra_p in e.iter('DADOS-BASICOS-DE-OUTRA-PRODUCAO'):
    y = outra_p.attrib
    f.write(y["TITULO"] + "\n")

f.close()
