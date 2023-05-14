import streamlit as st
import pandas as pd 


st.set_page_config(layout= "wide")


col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Sunil Santhosh")
    content =""" 
    Hi, This is me Sunil Santhosh blablabla
    """
    st.info(content )



content2 = """
    Below you can find some of the apps i have built in python. Feel free to contact me !

    """
st.write(content2)

col3,emptycol,col4 = st.columns([1.5,0.5,1.5])

df = pd.read_csv("data.csv", sep= ";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        #print(row["title"])
        st.image("images/"+ row["image"])
        st.write(f"[source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write("[source Code](https://pythonhow.com)")