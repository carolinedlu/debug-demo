import streamlit as st
import os
st.write(os.getcwd())
image = Image.open('image.jpg')

st.image(image)
