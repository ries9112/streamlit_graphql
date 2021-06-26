import streamlit as st
import requests
import json
import pandas as pd

# Add title
st.title('Pulling Uniswap data from GraphQL')

# Add a selectbox to enter address lookup:
address = st.text_input("Enter ETH wallet to look up", "0x8115AfD8DFfCE5579381AD27524b6Feeae917BEF")

# Set query (which uses text input to specify ETH wallet address)
query = '''query {
  swaps(where: {recipient: "%s"}){
    id
    timestamp
    pool{
      token0{
        symbol
      }
      token1{
        symbol
      }
    }
    amount0
    amount1
    amountUSD
    sender
    recipient
    tick
  }
}

''' % address

# Point to correct subgraph URL
url = 'https://api.thegraph.com/subgraphs/name/benesjan/uniswap-v3-subgraph'
# Make the request
r = requests.post(url, json={'query': query})
#print(r.status_code)
#print(r.text)

# JSON adjustment
json_data = json.loads(r.text)

# extract JSON to convert to a dataframe
df_data = json_data['data']['swaps']
# convert to dataframe
df = pd.DataFrame(df_data)    

# Add text before the table
st.text('Breakdown of Uniswap swaps for {} ETH wallet address'.format(address))

# Show dataframe
st.write(df)

