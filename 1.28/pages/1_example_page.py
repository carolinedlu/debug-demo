import streamlit as st
import os
from PIL import Image

st.write(os.getcwd())
image = Image.open('mount/src/debug-demo/pages/image.jpg')

st.image(image)
