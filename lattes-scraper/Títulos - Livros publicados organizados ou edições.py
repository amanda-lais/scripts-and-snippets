from bs4 import BeautifulSoup
import xml.etree.ElementTree as et

tree = et.ElementTree(file='curriculo.xml')
root = tree.getroot()

e = list(root)[1][2]

f  = open("Livros publicados organizados ou edições.txt", "w")

for livro in e.iter('DADOS-BASICOS-DO-LIVRO'):
    y = livro.attrib
    f.write(y["TITULO-DO-LIVRO"] + "\n")

f.close()
