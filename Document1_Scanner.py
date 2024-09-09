import streamlit as st
import cv2
import pytesseract
import numpy as np
from PIL import Image
import time

st.title('Document Scanner Application')

# Load pytesseract application to perform OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define a function to scan an image
def Extract_Text(img):
    text = pytesseract.image_to_string(img)  # No need to specify language
    return text

# Capture image from webcam
def capture_image():
    # Open the webcam
    cap = cv2.VideoCapture(0)
    st.write("Capturing image in 5 seconds...")
    
    # Wait for 5 seconds
    time.sleep(5)

    # Capture the image
    ret, frame = cap.read()
    if not ret:
        st.error("Failed to capture image")
        cap.release()
        return None
    
    # Release the webcam
    cap.release()
    
    # Convert the image to PIL format
    img_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    return img_pil

if st.button('Capture Image'):
    # Capture the image
    img = capture_image()
    
    if img is not None:
        # Convert image to array
        image_array = np.array(img)
        # Show image on Streamlit
        st.image(image_array, caption='Captured Image...', use_column_width=True)

        with st.spinner('Extracting Text From Your Image...'):
            # Call Extract_Text function
            extracted_text = Extract_Text(img)
            st.subheader('Text Scanned')

            # Display the entire extracted text
            st.write('Extracted Text:', extracted_text)

            text_list = extracted_text.splitlines()

            # Display extracted information with safeguards
            if len(text_list) > 0:
                st.write('Line 1:', text_list[0])
            if len(text_list) > 1:
                st.write('Line 2:', text_list[1])
            if len(text_list) > 2:
                st.write('Line 3:', text_list[2])
            if len(text_list) > 3:
                st.write('Line 4:', text_list[3])
            if len(text_list) > 4:
                st.write('Line 5:', text_list[4])

