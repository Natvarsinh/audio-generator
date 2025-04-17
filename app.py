import streamlit as st
from gtts import gTTS
import tempfile
import os

st.set_page_config(page_title="Text to Audio Generator", layout="centered")

# Language label mappings
lang_options = {
    "English": {
        "title": "🎧 Text to Audio Generator",
        "desc": "Enter your text below, click **Generate**, and listen or download the audio.",
        "text_input": "📝 Enter Text",
        "generate": "🔊 Generate Audio",
        "warn_empty": "Please enter some text to convert.",
        "success": "✅ Audio generated!",
        "download": "⬇️ Download Audio",
        "lang_label": "🌐 Select UI Language"
    },
    "Hindi": {
        "title": "🎧 टेक्स्ट से ऑडियो जनरेटर",
        "desc": "अपना टेक्स्ट नीचे दर्ज करें, **जनरेट** पर क्लिक करें, और ऑडियो सुनें या डाउनलोड करें।",
        "text_input": "📝 टेक्स्ट दर्ज करें",
        "generate": "🔊 ऑडियो जनरेट करें",
        "warn_empty": "कृपया कन्वर्ट करने के लिए कुछ टेक्स्ट दर्ज करें।",
        "success": "✅ ऑडियो जनरेट हो गया!",
        "download": "⬇️ ऑडियो डाउनलोड करें",
        "lang_label": "🌐 भाषा चुनें"
    },
    "Gujarati": {
        "title": "🎧 લખાણથી ઑડિયો જનરેટર",
        "desc": "તમારું લખાણ નીચે દાખલ કરો, **જનરેટ કરો** ક્લિક કરો અને ઑડિયો સાંભળો કે ડાઉનલોડ કરો.",
        "text_input": "📝 લખાણ દાખલ કરો",
        "generate": "🔊 ઑડિયો જનરેટ કરો",
        "warn_empty": "કૃપા કરીને કન્વર્ટ કરવા માટે લખાણ દાખલ કરો.",
        "success": "✅ ઑડિયો જનરેટ થયો!",
        "download": "⬇️ ઑડિયો ડાઉનલોડ કરો",
        "lang_label": "🌐 ભાષા પસંદ કરો"
    }
}

# Persist language selection in session state
if "selected_lang" not in st.session_state:
    st.session_state.selected_lang = "English"

# Language selector
selected_ui_lang = st.selectbox(
    lang_options[st.session_state.selected_lang]["lang_label"],
    list(lang_options.keys()),
    index=list(lang_options.keys()).index(st.session_state.selected_lang),
    key="selected_lang"
)

# Use selected language dictionary
txt = lang_options[st.session_state.selected_lang]


# --- UI ---
st.title(txt["title"])
st.markdown(txt["desc"])

text_input = st.text_area(txt["text_input"], height=300)

if st.button(txt["generate"]):
    if not text_input.strip():
        st.warning(txt["warn_empty"])
    else:
        tts = gTTS(text_input, lang="hi")
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tts.save(tmp_file.name)
            audio_path = tmp_file.name

        st.success(txt["success"])
        st.audio(audio_path, format="audio/mp3")

        with open(audio_path, "rb") as f:
            st.download_button(
                label=txt["download"],
                data=f,
                file_name="generated_audio.mp3",
                mime="audio/mp3"
            )

        os.remove(audio_path)