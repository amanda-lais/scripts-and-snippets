from bs4 import BeautifulSoup
import xml.etree.ElementTree as et

tree = et.ElementTree(file='curriculo.xml')
root = tree.getroot()

e = list(root)[1][3]

f  = open("Textos em jornais de notícias revistas.txt", "w")

for texto in e.iter('DADOS-BASICOS-DO-TEXTO'):
    y = texto.attrib
    f.write(y["TITULO-DO-TEXTO"] + "\n")

f.close()
