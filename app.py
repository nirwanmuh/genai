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
st.set_page_config(page_title="Gemini Chat", layout="centered")
st.title("💬 Gemini Chatbot")

# Inisialisasi session state untuk menyimpan history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan history percakapan
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("👤 Kamu"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("🤖 Gemini"):
            st.markdown(msg["content"])

# Input pengguna
user_input = st.chat_input("Tulis pesan...")

if user_input:
    # Simpan input ke history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("👤 Kamu"):
        st.markdown(user_input)

    # Respon dari Gemini
    with st.chat_message("🤖 Gemini"):
        with st.spinner("Gemini sedang mengetik..."):
            try:
                model = genai.GenerativeModel("gemini-2.5-flash")
                response = model.generate_content(user_input)
                reply = response.text
            except Exception as e:
                reply = f"❌ Terjadi kesalahan: {e}"
            st.markdown(reply)
            st.session_state.messages.append({"role": "gemini", "content": reply})
