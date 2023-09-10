import streamlit as st
import requests
import pandas as pd

# Function to fetch data from the Clash of Clans API
def fetch_data():
    url = "https://api.clashofclans.com/v1/clans/%23RGRPVQUJ"
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjI5NWZiNjkzLTUwN2EtNDQ1NS04MGYwLTZjZjYxMGUyZjcxYyIsImlhdCI6MTY5MTg1MDIwMSwic3ViIjoiZGV2ZWxvcGVyL2Q3ZGMwZTFiLTQwM2YtOTY1NC0xZDM2LTBmZGY4NjA2MTc1MCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjM1LjIzMC41OC4yMTEiXSwidHlwZSI6ImNsaWVudCJ9XX0.fp5f0HjUagNzwjDChqJ2veO9Da9RgPfl7Hjcyj80TW5eUyrsGW0Z8u8bVBL-tp24XOifnpr5TiBL5AptM8mh-Q'
    }
    response = requests.request("GET", url, headers=headers)
    return response.json()

# Fetching clan data
clan_data = fetch_data()

# Extracting member details



# Metrics
#st.subheader('Metrics')
# st.write('Clan Name:', clan_data['name'])
# st.write('Clan Tag:', clan_data['tag'])
# st.write('Clan War Wins:', clan_data['warWins'])
# st.write('Clan Builder Points:', clan_data['clanBuilderBasePoints'])
# st.write('Clan Capital Points:', clan_data['clanCapitalPoints'])
# st.write('Total Members:', clan_data['members'])
# st.write('Clan Points:', clan_data['clanPoints'])
# st.write('Clan Level:', clan_data['clanLevel'])

# Member details table
# st.subheader('Member Details')
# st.dataframe(member_df)
