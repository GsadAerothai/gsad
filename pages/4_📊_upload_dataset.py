import streamlit as st
from PIL import Image
import io 
import os
import cv2 

st.set_page_config(page_title="Update Datasets 📊")
st.markdown("# Update Datasets 📊")

st.sidebar.title("About")
st.sidebar.info(
    """
    This project is created by GSAD team in โครงการบัณฑิตพันธ์ใหม่, Aerothai innovation 2023.
    """
)

def split_img(vid):
	vidcap = cv2.VideoCapture(vid)
	count = 0
	success = True
	fps =  int(vidcap.get(cv2.CAP_PROP_FPS))

	while success:
		success,img = vidcap.read()
		if count %(10*fps) == 0:
			cv2.imwrite('./data/Frame%d.jpg'%count,img)

		count += 1


exam_file = st.file_uploader("Choose retrain video file")
if exam_file is not None :
	g = io.BytesIO(exam_file.read())
	temporary_location = "./data/Temp_uploaded.mp4"

	with open(temporary_location,'wb') as out:
		out.write(g.read())

	out.close()

	split_img(temporary_location)
	filelist=[]
	for root, dirs, files in os.walk("./data"):
	      for file in files:
	             filename=os.path.join(root, file)
	             filelist.append(filename)
	st.write(filelist)

