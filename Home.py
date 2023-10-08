import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Fezekile Gxalaba")
    content3 = """ 
    Junior Software Engineer, AI Engineer Student
    """
    st.write(content3)
    content = """
    Hi, I'm Fezekile Gxalaba a Junior Software Engineer using Python, and Founder of FIG Digital Agency from South Africa. I like to build web applications using Django, Flask
    and Flutter. And also building AI Applications with Tensorflow, Keras, PyTorch, SciPy, and ScikitLearn, I am passionate about technology and innovation. I'm sort of a techy, geeky kind of person! I really like to play with technology. I'm an AWS Certified Developer, Microsoft Azure Certified
    Developer, IBM Certified Associate Developer and Artificial Intelligence Student at IBM Cognitive Class.
    """
    st.info(content)

content2 = """
Below you can find some of the apps i have built in Python. Feel free to contact me anytime!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://pythonhow.com)")
