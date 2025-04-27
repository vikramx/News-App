import streamlit as st
import json
import requests

st.title("News App 📰")
st.subheader("An app to show you the news for the day")


topic=st.text_input("Enter news topic here:")
ps=st.number_input("Enter number of articles in 1 page here:",min_value=1)
api_key="d6294e9b2ca842c1815660bfdcfabd42"
base_url=(f"https://newsapi.org/v2/everything?q={topic}&apiKey=d6294e9b2ca842c1815660bfdcfabd42")
p={
    "pageSize":ps
}
response=requests.get(base_url,params=p)
data=response.json()
if st.button("Show articles"):
    if response.status_code==200 and data["totalResults"] != 0:
        art_list = data['articles']
        num = 1
        st.write("Headlines")
        for i in art_list:
            st.write(f"{num}: Headlines {num}\n")
            img = i["urlToImage"]
            st.image(img, caption='Article Image')
            st.write(f"Title: {i['title']}")
            st.write(f"Author: {i["author"]}")
            st.write(f"News: {i['description']}")
            st.write(f"Link to the article: {i["url"]}")
            st.write('---------------------------------')

            num = num + 1
    else:
        st.error("Please enter a valid news category 😡")
