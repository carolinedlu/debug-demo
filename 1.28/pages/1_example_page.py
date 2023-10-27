import streamlit as st
import os
from PIL import Image

st.write(os.getcwd())
image = Image.open('/debug-demo/1.28/pages/image.jpg')

st.image(image)
