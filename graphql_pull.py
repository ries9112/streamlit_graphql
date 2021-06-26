import streamlit as st
import requests
import json
import pandas as pd

# Add title
st.title('Pulling data from GraphQL')

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Choose query to run
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


