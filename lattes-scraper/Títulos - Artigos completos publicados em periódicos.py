from bs4 import BeautifulSoup
import xml.etree.ElementTree as et

tree = et.ElementTree(file='curriculo.xml')
root = tree.getroot()

e = list(root)[1][1]

f  = open("Artigos completos publicados em periódicos.txt", "w")

for artigo in e.iter('DADOS-BASICOS-DO-ARTIGO'):
    y = artigo.attrib
    f.write(y["TITULO-DO-ARTIGO"] + "\n")

f.close()
