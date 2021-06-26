import requests
import json
import pandas as pd

query = """query {
  account(id: "0x00000000af5a61acaf76190794e3fdf1289288a1") {
    id
    tokens(first: 7) {
      id
      symbol
      cTokenBalance
    }
  }
  markets {
    exchangeRate
    symbol
  }
}
"""


url = 'https://api.thegraph.com/subgraphs/name/graphprotocol/compound-v2'
r = requests.post(url, json={'query': query})
#print(r.status_code)
#print(r.text)

json_data = json.loads(r.text)


#json_data


df_data = json_data['data']['account']['tokens']

#print(df_data)


df = pd.DataFrame(df_data)    

print(df)
