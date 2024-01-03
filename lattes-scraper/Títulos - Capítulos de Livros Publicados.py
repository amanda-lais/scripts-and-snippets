from bs4 import BeautifulSoup
import xml.etree.ElementTree as et

tree = et.ElementTree(file='curriculo.xml')
root = tree.getroot()

e = list(root)[1][2]

f  = open("Capítulos de livros publicados.txt", "w")

for capitulo in e.iter('CAPITULO-DE-LIVRO-PUBLICADO'):
    x = capitulo[0].attrib["TITULO-DO-CAPITULO-DO-LIVRO"]
    y = capitulo[1].attrib["TITULO-DO-LIVRO"]
    f.write("NOME DO CAPÍTULO: " + x + "\nNOME DO LIVRO: " + y + "\n\n")

f.close()
