import requests

cep = input(f"Digite o seu CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url)

resposta = dados.json()

print(f"\nVocê mora no seguinte endereço:\n\nRua: {resposta["logradouro"]}\nBairro: {resposta["bairro"]}\nCidade: {resposta["localidade"]}\n")