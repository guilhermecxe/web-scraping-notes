import requests
from bs4 import BeautifulSoup

# Fazendo a requisição
r = requests.get('https://books.toscrape.com/')

# Criando um objeto parseável do HTML da página retornada
soup = BeautifulSoup(r.text, 'html.parser')

# Selecionando elementos com CSS
for el in soup.select('.product_pod h3 a', limit=5):
    print(el.get('title'))

# Selecionando um elemento com CSS
print(soup.select_one('.product_pod h3 a'))

# Encontrando elementos pela classe e pelo id
elements = soup.find_all(class_='product_pod')
print(elements[0].find('h3'))
print(soup.find(id='#promotions_left'))

# Encontrando elementos por um atributo específico
print(soup.find('img', attrs={'alt': 'A Light in the Attic'}))

# soup.find_all_next
# soup.find_all_previous
# soup.find_parent
# soup.find_next_siblings
# ...