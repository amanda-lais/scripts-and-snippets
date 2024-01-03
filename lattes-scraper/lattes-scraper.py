from bs4 import BeautifulSoup
import xml.etree.ElementTree as et

tree = et.ElementTree(file='curriculo.xml')
root = tree.getroot()

def scrape_lattes(x):
    if x==1:
        txt_nome = "Artigos completos publicados em periódicos.txt"
        v_iter = 'DADOS-BASICOS-DO-ARTIGO'
        v_write = 'TITULO-DO-ARTIGO'
        y = 1
    elif x==2:
        txt_nome = "Textos em jornais de notícias revista.txt"
        v_iter = 'DADOS-BASICOS-DO-TEXTO'
        v_write = 'TITULO-DO-TEXTO'
        y = 3
    elif x==3:
        txt_nome = "Capítulos de livros publicados.txt"
        v_iter = 'CAPITULO-DE-LIVRO-PUBLICADO'
        v_write = 'TITULO-DO-CAPITULO-DO-LIVRO'
        v_write1 = 'TITULO-DO-LIVRO'
        y = 2
    elif x==4:
        txt_nome = "Livros publicados organizados ou edições.txt"
        v_iter = 'DADOS-BASICOS-DO-LIVRO'
        v_write = 'TITULO-DO-LIVRO'
        y = 2
    elif x==5:
        txt_nome = "Publicados em anais de congressos.txt"
        v_iter = 'DADOS-BASICOS-DO-TRABALHO'
        v_write = 'TITULO-DO-TRABALHO'
        y = 0
    elif x==6:
        txt_nome = "Outras produções bibliográficas.txt"
        v_iter = 'DADOS-BASICOS-DE-OUTRA-PRODUCAO'
        v_write = 'TITULO'
        y = 4
    e = list(root)[1][y]
    f  = open(txt_nome, "w")
    for i in e.iter(v_iter):
        if x!=3:
            f.write(i.attrib[v_write] + '\n')
        else:
            f.write("NOME DO LIVRO\nNOME DO CAPÍTULO\n" + i[1].attrib[v_write1] + "\n" + i[0].attrib[v_write] + "\n\n")
    f.close()
    print('\n' + txt_nome + ' criado com sucesso!\n\n')

while True:
    print("Opção 1: Títulos - Artigos completos publicados em perioódicos")
    print("Opção 2: Títulos - Textos em jornais de notícias/revistas")
    print("Opção 3: Títulos - Capítulos de Livros Publicado")
    print("Opção 4: Títulos - Livros publicados/organizados ou edições")
    print("Opção 5: Títulos - Publicados em anais de congressos")
    print("Opção 6: Títulos - Outras produções bibliográficas")
    print("Opção 7: Sair")
    opcao = input("Digite a opção desejada: ")
    if int(opcao) == 7:
        break
    else:
        scrape_lattes(int(opcao))
exit()
