import streamlit as st
import io 
import os
from PIL import Image
from yolov5 import detect
import cv2 

st.set_page_config(page_title="Try me 🤩 !")
st.markdown("# Try me 🤩!")

st.sidebar.title("About")
st.sidebar.info(
    """
    This project is created by GSAD team in โครงการบัณฑิตพันธ์ใหม่, Aerothai innovation 2023.
    """
)

temporary_location = False

def detect_video():
	detect.run(weights='./src/weight.pt',img=640,conf_thres=0.5,source='./tmp/video.mp4',project='./tmp/',exist_ok=True)
	return open('./tmp/exp/video.mp4','rb')


def detect_image():
	detect.run(weights='./src/weight.pt',img=640,conf_thres=0.5,source='./tmp/image.jpg',project='./tmp/',exist_ok=True)
	return Image.open('./tmp/exp/image.jpg')
	
st.markdown("#### Now you can try to use our detection model by upload image file.")

img_file = st.file_uploader("Choose the Jpg file !",type=['png', 'jpeg', 'jpg'])
if img_file is not None :
	image = Image.open(img_file,mode='r')
	rgb_img = image.convert('RGB')
	rgb_img.save('./tmp/image.jpg')
	
	
	#with open('./tmp/image.jpg', 'wb') as f: 
	#	f.write(image)

	#detected_img = Image.open('./tmp/image.jpg')
	detected_img = detect_image()
	st.image(detected_img) 


st.markdown("#### Or Video")
vid_file = st.file_uploader("Choose retrain video file")
if vid_file is not None :
	g = io.BytesIO(vid_file.read())


	with open('./tmp/video.mp4','wb') as out:
		out.write(g.read())

	out.close()

	detected_vid = detect_video()
	vid_bytes = detected_vid.read()
	st.video(vid_bytes) 
