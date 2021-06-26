import streamlit as st
import requests
import json
import pandas as pd

# Add title
st.title('Pulling data from GraphQL')

# Add a selectbox to enter address lookup:
address = st.text_input("Enter ETH wallet to look up", "0x00000000af5a61acaf76190794e3fdf1289288a1")

# Choose query to run
query = f'''query {
  account(id: {address} ) {
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
'''.format(address)

# Point to correct subgraph URL
url = 'https://api.thegraph.com/subgraphs/name/graphprotocol/compound-v2'
# Make the request
r = requests.post(url, json={'query': query})
#print(r.status_code)
#print(r.text)

# JSON adjustment
json_data = json.loads(r.text)

# extract JSON to convert to a dataframe
df_data = json_data['data']['account']['tokens']
# convert to dataframe
df = pd.DataFrame(df_data)    

# Add text before the table
st.text('Breakdown of tokens for {} address on the ETH blockchain'.format(address))

# Show dataframe
st.write(df)



