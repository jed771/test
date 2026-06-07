import streamlit as st
from pathlib import Path

st.set_page_config(page_title="My Internship Project", layout="wide")

html_path = Path(__file__).parent / "index.html"
if html_path.exists():
    html = html_path.read_text(encoding="utf-8")
    st.components.v1.html(html, height=800, scrolling=True)
else:
    st.write("index.html not found. Place your frontend files in the project root.")
