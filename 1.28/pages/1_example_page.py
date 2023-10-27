import streamlit as st
import os
from PIL import Image

st.write(os.getcwd())
image = Image.open('pages/image.jpg')

st.image(image)
