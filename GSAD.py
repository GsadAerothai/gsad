import streamlit as st
import cv2 


st.set_page_config(page_title="GSAD ",page_icon="👋")
st.write(cv2.__version__)
st.sidebar.title("About")
st.sidebar.info(
    """
    This project is created by GSAD team in โครงการบัณฑิตพันธ์ใหม่, Aerothai innovation 2023.
    """
)

st.write("# Welcome to GSAD web app demo !")
st.markdown("GSAD is the object detection model of suspicious things in airport \
eg. Human, UAV, Car which using Machine Learning for detection process.")
#st.sidebar.success("Select a demo above.")

st.markdown("### Example of this project.")

video_file = open('./src/demo.mp4','rb')
video_bytes = video_file.read()

st.video(video_bytes,start_time=15)
st.snow()
