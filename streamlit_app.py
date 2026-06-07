import streamlit as st
from pathlib import Path

st.set_page_config(page_title="My Internship Project", layout="wide")

html_path = Path(__file__).parent / "index.html"
# The widget script the user provided (keeps localhost URLs as requested)
widget_script = (
    '<script src="http://localhost:8080/widget-embed.js" '
    'data-agency-key="sk_af1141787f48fb3e85f5f4aad714f25143b5c0bc3d34c5a6" '
    'data-api-url="http://localhost:8000"></script>'
)

def inject_widget(html_content: str) -> str:
    if "widget-embed.js" in html_content:
        return html_content
    if "</body>" in html_content:
        return html_content.replace("</body>", f"    {widget_script}\n</body>")
    return html_content + widget_script


if html_path.exists():
    html = html_path.read_text(encoding="utf-8")
    html = inject_widget(html)
    # Allow JavaScript execution so the widget can run
    st.components.v1.html(html, height=900, scrolling=True, unsafe_allow_javascript=True)
else:
    # Fallback minimal page containing the widget script
    fallback = (
        "<!doctype html><html><head><meta charset=\"utf-8\"></head>"
        "<body><h3>Embedded widget</h3>" + widget_script + "</body></html>"
    )
    st.components.v1.html(fallback, height=600, scrolling=True, unsafe_allow_javascript=True)

# Warn if the widget or API URL still point to localhost (won't work when deployed)
if "localhost" in widget_script:
    st.warning(
        "The widget script or API is using localhost. This will only work when testing locally; deploy the widget JS and API to public URLs for a deployed Streamlit app."
    )
