import requests

resposta = requests.get('https://www.google.com')
print(resposta.status_code)

# Retorna header
print(resposta.headers)

for chave, valor in resposta.headers.items():
    print(chave, '   ', valor)

# O que são requests responses: https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html
# O que são server headers: https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html
