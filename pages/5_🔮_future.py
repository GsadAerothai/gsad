import streamlit as st
from PIL import Image

st.set_page_config(page_title=" Future plan")

st.sidebar.title("About")
st.sidebar.info(
    """
    This project is created by GSAD team in โครงการบัณฑิตพันธ์ใหม่, Aerothai innovation 2023.
    """
)

st.markdown("# Future Plan 🔮")

st.markdown("### MLops")
image1 = Image.open('./src/future.png')
st.image(image1,caption="Diagram for future plan")

