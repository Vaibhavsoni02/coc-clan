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
members = clan_data['memberList']
member_details = [[
    member['league']['name'],
    member['name'],
    member['role'],
    member['expLevel'],
    member['trophies'],
    member['builderBaseTrophies'],
    member['donations'],
    member['tag'],
    #member['league']['iconUrls']['small']
] for member in members]

# Creating a Pandas DataFrame with custom column names
columns = ['League', 'Name', 'Role', 'Exp Level', 'Trophies', 'Builder Base Trophies', 'Donations', 'Tag']
#if we want to include icon url 'league.Icon'
member_df = pd.DataFrame(member_details, columns=columns)

# Frontend
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('''
    <a href="https://link.clashofclans.com/en?action=OpenClanProfile&tag=RGRPVQUJ">
        <img src="https://static.wikia.nocookie.net/clashofclans/images/f/f4/Super_Dragon_info.png" />
    </a>''',
    unsafe_allow_html=True
)
    #st.image("https://link.clashofclans.com/build/0.7/images/clashofclans/deco_clashofclans_m.png")
    st.write("")
with col2:
    st.markdown('''
    <a href="https://link.clashofclans.com/en?action=OpenClanProfile&tag=RGRPVQUJ">
        <img src="https://link.clashofclans.com/build/0.7/images/clashofclans/logo_clashofclans_m.png" />
    </a>''',
    unsafe_allow_html=True
    )
    #st.image("logo_clashofclans_m.png", width=225)
    st.write("")
with col3:
    st.image(clan_data['badgeUrls']['large'])
    st.write("")

st.write("----")


# Metrics in Sidebar
st.sidebar.subheader('Metrics')
st.sidebar.write('Clan Name:', clan_data['name'])
st.sidebar.write('Clan Tag:', clan_data['tag'])
st.sidebar.write('Clan War Wins:', clan_data['warWins'])
st.sidebar.write('Clan Builder Points:', clan_data['clanBuilderBasePoints'])
st.sidebar.write('Clan Capital Points:', clan_data['clanCapitalPoints'])
st.sidebar.write('Total Members:', clan_data['members'])
st.sidebar.write('Clan Points:', clan_data['clanPoints'])
st.sidebar.write('Clan Level:', clan_data['clanLevel'])


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
st.subheader('Member Details')
st.dataframe(member_df)
