import streamlit as st
import requests
import json

def fetch_data():
    url = "https://api.clashofclans.com/v1/clans/%23RGRPVQUJ"
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjRkZTM0YzA0LTMxYWYtNDRkNC1iZjdlLTkwYjZiMzA2NmRhYSIsImlhdCI6MTY5MTg0NDg3OSwic3ViIjoiZGV2ZWxvcGVyL2Q3ZGMwZTFiLTQwM2YtOTY1NC0xZDM2LTBmZGY4NjA2MTc1MCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEwMy4yMTkuMjI4LjIyNCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.96OZmdYxIFS7kZt-pnYK-X9anc8eJcj0ug8y_jR5E3zToKfm6p4UE2sE9oJuoSj_eu16yqPaQvrruA2M73Fmiw'
    }
    response = requests.get(url, headers=headers)
    return response.json()

def display_data(data):
    st.title("Clan Information")
    st.write("Name:", data["name"])
    st.write("Clan Level:", data["clanLevel"])
    st.write("Location:", data["location"]["name"])
    # Add more fields here as needed

def main():
    st.sidebar.title("Clash of Clans Clan Information")
    if st.sidebar.button("Fetch Clan Data"):
        data = fetch_data()
        display_data(data)
    else:
        st.write("Click the button to fetch the clan data.")

if __name__ == "__main__":
    main()
