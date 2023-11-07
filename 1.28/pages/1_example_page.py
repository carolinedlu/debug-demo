import streamlit as st
import os
from PIL import Image

st.write(os.getcwd())

path = os.path.dirname(__file__)
my_file_path = path+'/image.jpg'
st.write(my_file_path)
# image = Image.open('/mount/src/debug-demo/1.28/pages/image.jpg')
# # st.write(my_file)

# st.image(image)
