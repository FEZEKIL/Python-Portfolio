import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Fezekile Gxalaba")
    content = """
    Hi, Fezekile Gxalaba A Full Stack Developer, and Founder of FIG Digital Agency from South Africa, I like to build web applications using django, flask
    and Flutter, I'm passionate with technology, I'm kinda a techie gigyy person!
    """
    st.info(content)

content2 = """
Below you can find some of the apps i have built in Python. Feel free to contact me anytime!
"""
st.write(content2)