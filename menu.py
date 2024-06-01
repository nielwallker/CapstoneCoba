import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np

from util import classify

# Function to include Bootstrap 5
def include_bootstrap():
    st.markdown('''
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/5.1.3/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background-image: url('bgrd/bg.jpg');
                background-size: cover;
                background-repeat: no-repeat;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .title {
                color: #4CAF50;
                font-family: 'Arial', sans-serif;
                font-size: 3em;
                text-align: center;
                margin-top: 20px;
            }
            .header {
                color: #333;
                font-family: 'Arial', sans-serif;
                text-align: center;
                margin-top: 20px;
            }
            .subheader {
                color: #555;
                font-family: 'Arial', sans-serif;
                text-align: center;
                margin-top: 10px;
            }
            .stImage {
                display: flex;
                justify-content: center;
                margin-top: 20px;
            }
            .stFileUploader {
                display: flex;
                justify-content: center;
                margin-top: 20px;
            }
        </style>
    ''', unsafe_allow_html=True)

# Apply Bootstrap
include_bootstrap()

# Container for content
with st.container():
    # set title
    st.markdown('<h1 class="title">Casting Quality Control</h1>', unsafe_allow_html=True)

    # set header
    st.markdown('<h2 class="header">Please upload a Casting Product Image</h2>', unsafe_allow_html=True)

    # upload file
    file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

    # load classifier
    model = load_model('./model/modelcast.h5')

    # load class names
    with open('./model/labels.txt', 'r') as f:
        class_names = [a[:-1].split(' ')[1] for a in f.readlines()]

    # display image
    if file is not None:
        image = Image.open(file).convert('RGB')
        st.image(image, use_column_width=True)

        # classify image
        class_name, conf_score = classify(image, model, class_names)

        # write classification
        st.markdown(f'<h2 class="subheader">{class_name}</h2>', unsafe_allow_html=True)
        st.markdown(f'<h3 class="subheader">score: {int(conf_score * 1000) / 10}%</h3>', unsafe_allow_html=True)