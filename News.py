import os
import requests
import datetime
import streamlit as st
today = datetime.date.today()
apikey=os.getenv("apikey")
print(apikey)
url = f"https://newsapi.org/v2/everything?q='cyberattack'&from={today}&sortBy=publishedAt&apiKey={apikey}"
response = requests.get(url, verify=False).json()
length = len(response["articles"])


st.title("Today's News About Cyber Attacks")
y=1
col1, col2, col3 = st.columns(3,gap="large")
for i in range(length):
    news = response["articles"][i]
    title = news["title"]
    description = news["description"]
    url = news["url"]
    image = news["urlToImage"]
    content = news["content"]

    if y==1:
        with col1:
                st.header(title)
                st.write(description)
                st.write(url)

    elif y==2:
        with col2:
            st.header(title)
            st.write(description)
            st.write(url)

    else:
        with col3:
            st.header(title)
            st.write(description)
            st.write(url)
    y=y+1
    if y >3:
        y=1






