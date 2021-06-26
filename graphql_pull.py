import streamlit as st
import requests
import json
import pandas as pd

# Add title
st.title('Pulling data from GraphQL')

# Add a selectbox to enter address lookup:
address = st.text_input("Enter ETH wallet to look up", "0x00000000af5a61acaf76190794e3fdf1289288a1")

# Choose query to run
query = '''query {
  account(id: "%s" ) {
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
''' % address

st.text(query)


