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
st.set_page_config(page_title="Ngobrol Sama Nirwan", layout="centered")
st.title("💬 Ngobrol Sama Nirwan")

# Inisialisasi session state untuk menyimpan history
# Inisialisasi session_state untuk history dan chat
if "chat" not in st.session_state:
    model = genai.GenerativeModel("gemini-2.5-flash")
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan seluruh history percakapan
for msg in st.session_state.messages:
    with st.chat_message("👤 Kamu" if msg["role"] == "user" else "🤖 Nirwan"):
        st.markdown(msg["content"])

# Input pengguna
user_input = st.chat_input("Tulis pesan...")

if user_input:
    # Simpan dan tampilkan input pengguna
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("👤 Kamu"):
        st.markdown(user_input)

    # Kirim ke Gemini dengan konteks (menggunakan chat instance)
    with st.chat_message("🤖 Nirwan"):
        with st.spinner("Bentar, lagi mikiri..."):
            try:
                response = st.session_state.chat.send_message(user_input)
                reply = response.text
            except Exception as e:
                reply = f"❌ Terjadi kesalahan: {e}"

        st.markdown(reply)
        st.session_state.messages.append({"role": "gemini", "content": reply})
