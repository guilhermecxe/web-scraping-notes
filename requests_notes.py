import requests

# Utilizando headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
}

# Timeout é o tempo máximo que o programa espera para obter uma resposta do site requisitado
TIMEOUT = 10

# Fazendo a requisição
r = requests.get('https://books.toscrape.com/')

# Obtendo informações retornadas na requisição
# print(r.text) # HTML da página
print(r.status_code) # Código retornado