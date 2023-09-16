# Obtendo produtos do mercado livre através de uma busca realizada pelo usuário

import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

# div = ui-search-pagination shops__pagination-content
page = site.find('div', attrs={'class': 'ui-search-pagination shops__pagination-content'})
print (page.prettify())
# li = andes-pagination__page-count
page_count = page.find('li', attrs={'class': 'andes-pagination__page-count'})
print ('Qtde de páginas: ', page_count.text)
print ('Última página: ', page_count.text[-1])

produtos = site.findAll('div', attrs={'class': 'ui-search-result__content-wrapper shops__result-content-wrapper'})

x = 0

for produto in produtos:
  titulo = produto.find('h2', attrs={'class': 'ui-search-item__title shops__item-title'})
  link = produto.find('a', attrs={'class': 'ui-search-link'})
  valor = produto.find('div', attrs={'class': 'ui-search-price__second-line shops__price-second-line'})

  real = valor.find('span', attrs={'class': 'andes-money-amount__fraction'})
  centavos = valor.find('span', attrs={'class': 'andes-money-amount__cents andes-money-amount__cents--superscript-24'})

  # print (produto.prettify())
  print ('Título do produto: ', titulo.text)
  x = x + 1
  print ('Link do produto: ', link['href'])

  if (centavos):
    print ('Preço do produto: R$', real.text + ',' + centavos.text)
  else:
    print ('Preço do produto: R$', real.text)

  print ('\n\n')

print (x)