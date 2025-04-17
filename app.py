import streamlit as st
from gtts import gTTS
import tempfile
import os

st.set_page_config(page_title="Text to Audio Generator", layout="centered")

# --- UI ---
st.title("🎧 Text to Audio Generator")
st.markdown("Enter your text below, click **Generate**, and listen or download the audio.")

text_input = st.text_area("📝 Enter Text", height=300)

if st.button("🔊 Generate Audio"):
    if not text_input.strip():
        st.warning("Please enter some text to convert.")
    else:
        tts = gTTS(text_input, lang="hi")
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tts.save(tmp_file.name)
            audio_path = tmp_file.name

        st.success("✅ Audio generated!")
        st.audio(audio_path, format="audio/mp3")

        with open(audio_path, "rb") as f:
            st.download_button(
                label="⬇️ Download Audio",
                data=f,
                file_name="generated_audio.mp3",
                mime="audio/mp3"
            )

        os.remove(audio_path)