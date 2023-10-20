import requests
import json

# variavel com link da api
api_url = 'https://sdw-2023-prd.up.railway.app'

def get_user(id):
    response = requests.get(f'{api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

def update_user(id):
  response = requests.put(f"{api_url}/users/{id}", json=id)
  return True if response.status_code == 200 else False

#extract so tinha 1 id logo não coloquei uma csv ou algo para pegar os dados de la
user = get_user(1)
print(json.dumps(user, indent=2))
print('-'*60)

#transform no caso temos so 1 id, logo vou colocar 2 mensagens pois não tenho grana pra pagar o chat gpt
msg1 = f"Ola {user['name']} você está no banco certo =)"
msg2 = f"O melhor banco está do seu lado {user['name']}"

user['news'].append({
  "id": "3",
  "icon": "Mensagem1.com",
  "description": msg1
})

user['news'].append({
  "id": "4",
  "icon": "Mensagem2.com",
  "description": msg2
})

print('-'*60)

#load

deubom = update_user(1)

print("Deu certo rei" if True else "Que abalo")
