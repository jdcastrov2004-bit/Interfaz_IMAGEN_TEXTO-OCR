import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

st.title("Reconocimiento óptico de caracteres")
image = Image.open('lupa.jpg')
st.image(image, width=350)

st.write(
    "En esta actividad podrás experimentar con el reconocimiento óptico de caracteres (OCR). "
    "Toma una foto con la cámara de tu dispositivo, y el sistema intentará identificar y extraer el texto presente en la imagen. "
    "Puedes elegir aplicar un filtro para invertir los colores (útil cuando el fondo es oscuro y las letras son claras) o dejar la imagen sin filtro."
)

img_file_buffer = st.camera_input("Toma una foto para analizar")

with st.sidebar:
    filtro = st.radio("Selecciona el tipo de procesamiento", ('Con filtro', 'Sin filtro'))
    st.write(
        "**Con filtro:** invierte los colores de la imagen, lo que puede mejorar la lectura del texto en algunos casos.\n\n"
        "**Sin filtro:** mantiene la imagen original tal como fue capturada."
    )

if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    if filtro == 'Con filtro':
        cv2_img = cv2.bitwise_not(cv2_img)
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img_rgb)
    st.subheader("Texto detectado:")
    st.write(text)
