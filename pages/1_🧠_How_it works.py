import streamlit as st 
from PIL import Image

st.set_page_config(page_title = "How it works ?",page_icon="")
st.sidebar.title("About")
st.sidebar.info(
    """
    This project is created by GSAD team in โครงการบัณฑิตพันธ์ใหม่, Aerothai innovation 2023.
    """
)
image = Image.open('./src/yolov5.jpg')

st.markdown("# How this work ?")
st.markdown("> The model was trained by the most famous CNN model name You only \
	look once(YOLOv5)")
st.markdown("### Yolo V5 model architecture  :brain: ")
st.image(image,caption="source : https://github.com/ultralytics/yolov5/issues/280")

st.markdown("""##### CSP Backbone Layer""")
st.markdown(""" >The CSP models are based on DenseNet. DenseNet was designed to connect layers in convolutional neural networks\n""")
st.markdown("##### PA-Net Neck Layer")
st.markdown("""> Aggregate features layer from CSP backbone """)
st.markdown("##### Output Layer" )
st.markdown("""> Classification to the labeling output """)

with st.expander("Yolov5 resource"):
	st.write("""YOLOv5 🚀 is the world's most loved vision AI, representing Ultralytics open-source research into future vision AI methods, incorporating lessons learned and best practices evolved over thousands of hours of research and development.
		https://github.com/ultralytics/yolov5""")