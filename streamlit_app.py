import os
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="My Internship Project", layout="wide")

# Allow configuring backend and widget JS via environment variables
backend_url = os.getenv("BACKEND_URL", "http://localhost:8000")
widget_js_url = os.getenv("WIDGET_JS_URL", f"{backend_url}/static/widget-embed.js")

html_path = Path(__file__).parent / "index.html"
# Build the widget script using the configured URLs
widget_script = (
    f'<script src="{widget_js_url}" '
    'data-agency-key="sk_af1141787f48fb3e85f5f4aad714f25143b5c0bc3d34c5a6" '
    f'data-api-url="{backend_url}"></script>'
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
    # Render HTML (Streamlit's components API will execute embedded JS)
    st.components.v1.html(html, height=900, scrolling=True)
else:
    # Fallback minimal page containing the widget script
    fallback = (
        "<!doctype html><html><head><meta charset=\"utf-8\"></head>"
        "<body><h3>Embedded widget</h3>" + widget_script + "</body></html>"
    )
    st.components.v1.html(fallback, height=600, scrolling=True)

# Warn if the widget or API URL still point to localhost (won't work when deployed)
if "localhost" in backend_url or "localhost" in widget_js_url:
    st.warning(
        "The widget script or API is using localhost. This will only work when testing locally; deploy the widget JS and API to public URLs for a deployed Streamlit app."
    )
