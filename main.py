import json
import pandas as pd
import requests

JSON_PATH = 'files/tickets.json'
EXCEL_PATH = 'files/output.xlsx'

# Configurações da API
subdomain = "seusubdominio"             # seu subdomínio Zendesk
email = "seuemail@exemplo.com"          # seu e-mail de login
api_token = "seu_api_token"             # seu token da API Zendesk
group_id = 67890                        # ID do grupo que quer filtrar

# Autenticação básica com API Token (email/token)
auth = (f"{email}/token", api_token)

# URL base para tickets filtrados por grupo
import requests

url = "https://hunterdouglas904.zendesk.com/api/v2/users/me.json"  # API pública de exemplo

response = requests.get(url)

if response.status_code == 200:
    print("✅ Sucesso!")
    print(response.json())  # ou response.text se for só texto
else:
    print(f"❌ Erro: {response.status_code}")


# Salva os tickets em um arquivo JSON
with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)

# Carrega o JSON do arquivo
with open(JSON_PATH, "r", encoding="utf-8") as f:
    dados = json.load(f)

# Acessa a lista de tickets
# tickets_output = []
# tickets = dados["tickets"]
# for ticket in tickets:
#     if ticket['status'] == 'closed' or ticket['status'] == 'solved':
#         tickets_output.append(ticket)

# Converte os tickets para um DataFrame
df = pd.DataFrame(dados)

# # Salva em um arquivo Excel
df.to_excel(EXCEL_PATH, index=False)
