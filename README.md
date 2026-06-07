# Internship Chatbot Deployment

This repository contains a Streamlit frontend and a FastAPI backend configured for free deployment.

## What is already set up

- `streamlit_app.py` loads a chatbot widget script from a configurable public URL.
- `main.py` serves static files from `/static`, including `widget-embed.js`.
- `docs/widget-embed.js` is ready for GitHub Pages hosting.
- `requirements.txt` includes `streamlit`, `fastapi`, and `uvicorn`.

## Free hosting path

### 1. Host the widget JS on GitHub Pages

1. In GitHub, go to this repository `jed771/test`.
2. Open **Settings > Pages**.
3. Set **Source** to **main** branch and folder **/docs**.
4. Save.

Your widget script will be available at:

```
https://jed771.github.io/test/widget-embed.js
```

### 2. Deploy the FastAPI backend for free

Use Railway (free tier) or another free host.

#### Railway steps

1. Sign in at https://railway.app.
2. Create a new project and link your GitHub repo `jed771/test`.
3. Set the start command to:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

4. Deploy the project.
5. Copy the public URL Railway gives you.

### 3. Deploy the Streamlit frontend

Use Streamlit Community Cloud:

1. Go to https://share.streamlit.io/
2. Sign in with GitHub.
3. Create a new app using repo `jed771/test`, branch `main`, and path `streamlit_app.py`.
4. In app settings, set environment variables:

- `BACKEND_URL` = your public backend URL
- `WIDGET_JS_URL` = https://jed771.github.io/test/widget-embed.js

5. Deploy.

## Local testing

Run the Streamlit app locally:

```bash
streamlit run streamlit_app.py
```

If you also want to run the backend locally, run:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Then the app will use the local backend unless you override `BACKEND_URL`.
