import cv2
import numpy as np
import streamlit as st
from tensorflow import keras


model = keras.models.load_model('best_model21.h5')

def preprocess_image(image):

    img=cv2.resize(image,(128,128))
    resize_img=cv2.resize(img,(128,128),3)
    img=resize_img.reshape((1,128,128,3))
    
    return img

def predict_cardio(image):
    preprocessed_image = preprocess_image(image)
    prediction = model.predict(preprocessed_image)[0]
    
    return prediction


# Streamlit app
def main():
    st.title("Cardiomegaly Detection")
    uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
        st.image(image, caption='Uploaded Image', use_column_width=True)
    else:
        st.error("Upload the Image")

    if st.button('Predict'):
        prediction = predict_cardio(image)
        if prediction ==1:
            st.error("Heart Inlargement")
        else:
            st.success("Normal Heart ")
        
main()
