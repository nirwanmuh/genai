import streamlit as st

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
        reversed_text = user_input[::-1]

        # Output hasil
        st.success("✅ Teks yang dibalik:")
        st.code(reversed_text, language="text")
