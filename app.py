import streamlit as st
import google.generativeai as genai

# Konfigurasi API Key Gemini
genai.configure(api_key="AIzaSyB3IiCtP8-BDL72BtPaXBSwsPwdnRZjttY")

# Streamlit UI
st.title("💬 Gemini Text Generator")

user_input = st.text_input("Masukkan pertanyaan atau perintah:")

if st.button("Kirim"):
    if user_input.strip() == "":
        st.warning("Tolong masukkan teks.")
    else:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(user_input)
        st.subheader("Jawaban:")
        st.write(response.text)
