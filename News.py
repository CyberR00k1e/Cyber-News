import os
import requests
import datetime
import streamlit as st
today = datetime.date.today()
apikey=os.getenv("apikey")

url = f"https://newsapi.org/v2/everything?q='cyberattack'&from={today}&sortBy=publishedAt&apiKey={apikey}"
response = requests.get(url, verify=False).json()
length = len(response["articles"])
print(length)


st.title("Today's News About Cyber Attacks")
y=1

#col1, col2, col3,col4, col5, col6 = st.columns([4,2,4,2,4,2])

new_i_value=0
for i in range(length):
    i = new_i_value
    if i < length-1:
        col1, col2, col3, col4, col5, col6 = st.columns([4, 2, 4, 2, 4, 2])
        for repeat in range(3):
                print(i)
                news = response["articles"][i]
                title = news["title"]
                description = news["description"]
                url = news["url"]
                image = news["urlToImage"]
                content = news["content"]
                source= news["source"]["name"]

                if y==1:
                    with col1:
                        st.header(title)
                        st.write(f"source - {source}")
                        st.write(description)
                        st.write(url)

                    with col2:
                        st.empty()


                elif y==2:
                    with col3:
                        st.header(title)
                        st.write(f"source - {source}")
                        st.write(description)
                        st.write(url)
                    with col4:
                        st.empty()


                else:
                    with col5:
                        st.header(title)
                        st.write(f"source - {source}")
                        st.write(description)
                        st.write(url)
                    with col6:
                        st.empty()

                y=y+1

                if y >3:
                    y=1
                i=i+1
        new_i_value=i
        print(f"new i value is {new_i_value}")





