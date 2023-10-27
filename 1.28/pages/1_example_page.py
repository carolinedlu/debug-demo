import streamlit as st
import os
from PIL import Image

st.write(os.getcwd())

path = os.path.dirname(__file__)
my_file = path+'/image.jpg'
image = Image.open(my_file)

st.image(image)
