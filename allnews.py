import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# print (type(site))
# print (site.prettify())

# HTML da notícia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
  # Título
  titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
  print (titulo.text)
  print (titulo['href']) # link da notícia

  # Subtítulo
  subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
  if (subtitulo):
    print (subtitulo.text)

  print()