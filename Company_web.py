import streamlit as st

content = """Zim dreams of greatness. Unfortunately, though, he's hopelessly inept as a space invader. Desperate to be rid of the annoying Zim, 
            his planet's leaders send him on a mission to infiltrate Earth, providing him with leftover, cobbled-together equipment. 
            To their consternation, Zim succeeds in setting up a base on Earth and infiltrating human culture,
             posing as a human child as he plots the planet's downfall. Only Zim's archnemesis, Dib, recognizes that Zim is an alien, 
             and of course, nobody believes Dib's claims."""

st.header("The Best Company")
st.write(content)

st.subheader("Our Team")
col1, empty1 , col2, empty2, col3 = st.columns([1.5, .5, 1.5, .5, 1.5])


