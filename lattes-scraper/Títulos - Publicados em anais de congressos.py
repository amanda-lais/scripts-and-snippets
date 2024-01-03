from bs4 import BeautifulSoup
import xml.etree.ElementTree as et

tree = et.ElementTree(file='curriculo.xml')
root = tree.getroot()

e = list(root)[1][0]

f  = open("Publicados em anais de congressos.txt", "w")

for trabalho in e.iter('DADOS-BASICOS-DO-TRABALHO'):
    y = trabalho.attrib
    f.write(y["TITULO-DO-TRABALHO"] + "\n")

f.close()
