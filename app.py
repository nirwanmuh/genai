# app.py
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import uuid

# Load API Key dari file .env
load_dotenv()
API_KEY = os.getenv("AIzaSyB3IiCtP8-BDL72BtPaXBSwsPwdnRZjttY")

# Konfigurasi Gemini
genai.configure(api_key=API_KEY)

# Konfigurasi UI
st.set_page_config(page_title="Ngobrol Sama Nirwan", layout="centered")
st.title("💬 Ngobrol Sama Nirwan")

# Styling bubble chat via HTML + CSS
def chat_bubble(role, text):
    bubble_id = str(uuid.uuid4()).replace("-", "")
    if role == "user":
        align = "flex-end"
        bg_color = "#009dff"
        sender = "👤 Aku"
    else:
        align = "flex-start"
        bg_color = "#eaeaea"
        sender = "🤖 Nirwan"

    st.markdown(f"""
    <div style='display: flex; justify-content: {align}; margin-bottom: 10px;'>
        <div style='background-color: {bg_color}; color: black; padding: 10px 15px; border-radius: 15px; max-width: 80%; position: relative;'>
            <strong>{sender}</strong><br>
            <div id='{bubble_id}' style='white-space: pre-wrap; margin-top: 5px;'>{text}</div>
            <button onclick="navigator.clipboard.writeText(document.getElementById('{bubble_id}').innerText)" style='margin-top:5px; font-size:12px;'>📋 Copy</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Inisialisasi session_state
if "chat" not in st.session_state:
    model = genai.GenerativeModel("gemini-2.5-flash")
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# Render semua chat bubble
for msg in st.session_state.messages:
    chat_bubble(msg["role"], msg["content"])

# Input pengguna
user_input = st.chat_input("Tulis pesan...")

if user_input:
    # Simpan & tampilkan input pengguna
    st.session_state.messages.append({"role": "user", "content": user_input})
    chat_bubble("user", user_input)

    # Kirim ke Gemini
    with st.spinner("Bentar, lagi mikir..."):
        try:
            response = st.session_state.chat.send_message(user_input)
            reply = response.text
        except Exception as e:
            reply = f"❌ Terjadi kesalahan: {e}"

    chat_bubble("nirwan", reply)
    st.session_state.messages.append({"role": "gemini", "content": reply})
