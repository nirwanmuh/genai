import streamlit as st
from google import genai

client = genai.Client()
st.set_page_config(page_title="Text Reverser", layout="centered")

st.title("🔄 Aplikasi Pembalik Teks")

# Input teks dari pengguna
user_input = st.text_input("Masukkan teks di sini:")

# Tombol untuk proses
if st.button("Proses"):
    if user_input.strip() == "":
        st.warning("Silakan masukkan teks terlebih dahulu.")
    else:
        # Proses: balikkan teks
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
        )

        # Output hasil
        st.success("✅ Teks yang dibalik:")
        st.code(response.text)
