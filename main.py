import streamlit as st

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