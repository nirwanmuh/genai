# app.py
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key dari file .env
load_dotenv()
API_KEY = os.getenv("AIzaSyB3IiCtP8-BDL72BtPaXBSwsPwdnRZjttY")

# Konfigurasi Gemini
genai.configure(api_key=API_KEY)

# Konfigurasi UI
st.set_page_config(page_title="Chat dengan Gemini", layout="centered")
st.title("🤖 Nirwan-GPT")

# Input dari user
user_input = st.text_input("Tulis pertanyaan atau perintah kamu:")

if st.button("Kirim"):
    if not user_input.strip():
        st.warning("Silakan masukkan teks.")
    else:
        try:
            with st.spinner("Nirwan sedang mengetik... 🤖💭"):
                model = genai.GenerativeModel("gemini-2.5-flash")
                response = model.generate_content(user_input)
            st.subheader("💡 Jawaban dari Gemini:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
