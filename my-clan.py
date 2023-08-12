import streamlit as st
import requests

def fetch_clan_details():
    url = "https://api.clashofclans.com/v1/clans/%23RGRPVQUJ"
    headers = {
      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjRkZTM0YzA0LTMxYWYtNDRkNC1iZjdlLTkwYjZiMzA2NmRhYSIsImlhdCI6MTY5MTg0NDg3OSwic3ViIjoiZGV2ZWxvcGVyL2Q3ZGMwZTFiLTQwM2YtOTY1NC0xZDM2LTBmZGY4NjA2MTc1MCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEwMy4yMTkuMjI4LjIyNCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.96OZmdYxIFS7kZt-pnYK-X9anc8eJcj0ug8y_jR5E3zToKfm6p4UE2sE9oJuoSj_eu16yqPaQvrruA2M73Fmiw'
    }
    response = requests.request("GET", url, headers=headers)
    return response.json()

def display_clan_details():
    details = fetch_clan_details()
    st.title('Clan Details')
    #st.image(details['badgeUrls']['medium'], caption='Clan Badge')
    st.subheader('Name:')
    st.write(details['name'])
    st.subheader('Type:')
    st.write(details['type'])
    st.subheader('Description:')
    st.write(details['description'])
    st.subheader('Location:')
    st.write(details['location']['name'])
    st.subheader('Clan Level:')
    st.write(details['clanLevel'])
    st.subheader('Clan Points:')
    st.write(details['clanPoints'])
    st.subheader('Required Trophies:')
    st.write(details['requiredTrophies'])
    st.subheader('War Frequency:')
    st.write(details['warFrequency'])
    st.subheader('War Wins:')
    st.write(details['warWins'])
    st.subheader('Members:')
    st.write(details['members'])

if __name__ == '__main__':
    display_clan_details()
