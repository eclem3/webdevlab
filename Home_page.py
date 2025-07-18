import streamlit as st
import info

def homepage():
    st.header("Home")
    st.image(info.home_picture, width = 350)
    st.subheader("Ella Clem - CS 1301")
    st.write("**Portfolio**: A portfolio page that exemplifies my skills and involvment.")
    st.write("**Data About Me**: A page all about me.")
    st.write('---')
homepage()

def links_section():
    st.sidebar.header("Pages")
links_section()
def home_page():
    info.set_background()
home_page()
