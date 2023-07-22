import streamlit as st
import pandas

st.set_page_config(layout="wide")
content = """Zim dreams of greatness. Unfortunately, though, he's hopelessly inept as a space invader. Desperate to be rid of the annoying Zim, 
            his planet's leaders send him on a mission to infiltrate Earth, providing him with leftover, cobbled-together equipment. 
            To their consternation, Zim succeeds in setting up a base on Earth and infiltrating human culture,
             posing as a human child as he plots the planet's downfall. Only Zim's archnemesis, Dib, recognizes that Zim is an alien, 
             and of course, nobody believes Dib's claims."""

st.header("The Best Company")
st.write(content)

st.subheader("Our Team")
col1, empty1, col2, empty2, col3 = st.columns([1.5, 1, 1.5, 1, 1.5])

df = pandas.read_csv("data_C.csv", sep=',')


with col1:
    for index, row in df[:4].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.image("company_images/" + row["image"])
        st.write(row["role"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.image("company_images/" + row["image"])
        st.write(row["role"])

with col3:
    for index, row in df[8:].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.image("company_images/" + row["image"])
        st.write(row["role"])
