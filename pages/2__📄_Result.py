import streamlit as st
from PIL import Image

st.set_page_config(page_title="Result",page_icon="📄")

st.sidebar.title("About")
st.sidebar.info(
    """
    This project is created by GSAD team in โครงการบัณฑิตพันธ์ใหม่, Aerothai innovation 2023.
    """
)

st.markdown("# Training 📄")
st.write("How we train ?")
image1 = Image.open('./src/train.png')
st.image(image1,caption="Training diagram")


st.markdown("# Result 📄")
st.write("The training result was show by confusion matrix down below")
image2 = Image.open('./src/result.png')
st.image(image2,caption="Confusion matrix")
