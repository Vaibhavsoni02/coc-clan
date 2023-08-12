import streamlit as st
import requests
import json

st.title('Clash of Clans Clan Information')

url = "https://api.clashofclans.com/v1/clans/%23RGRPVQUJ"
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjI5NWZiNjkzLTUwN2EtNDQ1NS04MGYwLTZjZjYxMGUyZjcxYyIsImlhdCI6MTY5MTg1MDIwMSwic3ViIjoiZGV2ZWxvcGVyL2Q3ZGMwZTFiLTQwM2YtOTY1NC0xZDM2LTBmZGY4NjA2MTc1MCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjM1LjIzMC41OC4yMTEiXSwidHlwZSI6ImNsaWVudCJ9XX0.fp5f0HjUagNzwjDChqJ2veO9Da9RgPfl7Hjcyj80TW5eUyrsGW0Z8u8bVBL-tp24XOifnpr5TiBL5AptM8mh-Q'
}

@st.cache
def fetch_clan_data():
    response = requests.request("GET", url, headers=headers)
    return response.json()

clan_data = fetch_clan_data()

st.json(clan_data)
