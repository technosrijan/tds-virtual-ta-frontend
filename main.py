import streamlit as st
import requests
import base64

API_URL = "https://tds-virtual-ta-jue2.onrender.com/api/"

# === Page Config with Custom Logo ===
st.set_page_config(page_title="TDS Virtual TA", page_icon="logo.png", layout="centered")

# === Header with Logo ===
st.image("logo.png")
st.title("TDS Virtual TA")
st.markdown("Ask a question and upload any relevant screenshot or image.")

# === Input Fields ===
question = st.text_area("✍️ Enter your question", height=100)
uploaded_file = st.file_uploader("📸 Optionally upload an image", type=["png", "jpg", "jpeg", "webp"])

# === Button and Logic ===
if st.button("🔍 Get Answer"):
    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    image_base64 = None
    if uploaded_file:
        bytes_data = uploaded_file.read()
        image_base64 = base64.b64encode(bytes_data).decode("utf-8")

    payload = {
        "question": question,
        "image": image_base64
    }

    try:
        with st.spinner("Thinking..."):
            response = requests.post(API_URL, json=payload)
            response.raise_for_status()
            data = response.json()

        # === Show Answer ===
        st.success("✅ Answer")
        st.markdown(f"**{data.get('answer', 'No answer returned.')}**")

        # === Show Links ===
        links = data.get("links", [])
        if links:
            st.markdown("🔗 **Relevant Links:**")
            for link in links:
                st.markdown(f"- [{link['text']}]({link['url']})")
        else:
            st.info("No relevant links found.")

    except requests.exceptions.RequestException as e:
        st.error(f"❌ Request failed: {e}")
    except Exception as e:
        st.error(f"❌ Unexpected error: {e}")