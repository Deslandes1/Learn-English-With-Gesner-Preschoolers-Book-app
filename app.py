import streamlit as st
import asyncio
import tempfile
import base64
import os
import subprocess
import random

st.set_page_config(page_title="Let's Learn English With Gesner – Preschoolers", layout="wide")

def set_colorful_style():
    st.markdown("""
        <style>
        .stApp { background: linear-gradient(135deg, #ffe6f0, #ffd9e6, #ffe6f0); }
        .main-header { background: linear-gradient(135deg, #ff99cc, #ff66b5, #ff3388); padding: 1.5rem; border-radius: 20px; text-align: center; margin-bottom: 1rem; }
        .main-header h1 { color: white; text-shadow: 2px 2px 4px #000000; font-size: 2.5rem; margin: 0; }
        .main-header p { color: #fff5cc; font-size: 1.2rem; margin: 0; }
        html, body, .stApp, .stMarkdown, .stText, .stRadio label, .stSelectbox label, .stTextInput label, .stButton button, .stTitle, .stSubheader, .stHeader, .stCaption, .stAlert, .stException, .stCodeBlock, .stDataFrame, .stTable, .stTabs [role="tab"], .stTabs [role="tablist"] button, .stExpander, .stProgress > div, .stMetric label, .stMetric value, div, p, span, pre, code, .element-container, .stTextArea label, .stText p, .stText div, .stText span, .stText code { color: #1a1a2e !important; }
        .stText { color: #1a1a2e !important; font-size: 1rem; background: transparent !important; }
        .stTabs [role="tab"] { color: #1a1a2e !important; background: rgba(255,255,255,0.5); border-radius: 10px; margin: 0 2px; }
        .stTabs [role="tab"][aria-selected="true"] { background: rgba(255,255,255,0.9); color: #ff3388 !important; }
        .stRadio [role="radiogroup"] label { background: rgba(255,255,255,0.3); border-radius: 10px; padding: 0.3rem; margin: 0.2rem 0; color: #1a1a2e !important; }
        .stButton button { background-color: #ff66b5; color: white !important; border-radius: 30px; font-weight: bold; }
        .stButton button:hover { background-color: #ff3388; color: white !important; }
        section[data-testid="stSidebar"] { background: linear-gradient(135deg, #ffe6f0, #ffd9e6); }
        section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] .stText, section[data-testid="stSidebar"] label { color: #1a1a2e !important; }
        section[data-testid="stSidebar"] .stSelectbox label { color: #1a1a2e !important; }
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] { background-color: #ffffff; border: 1px solid #ff66b5; border-radius: 10px; }
        div[data-baseweb="popover"] ul { background-color: #ffffff; border: 1px solid #ff66b5; }
        div[data-baseweb="popover"] li { color: #1a1a2e !important; background-color: #ffffff; }
        div[data-baseweb="popover"] li:hover { background-color: #ffe6f0; }
        .color-box { display: inline-block; width: 40px; height: 40px; border-radius: 10px; margin-right: 10px; vertical-align: middle; border: 1px solid #ccc; }
        </style>
    """, unsafe_allow_html=True)

def show_logo():
    st.markdown("""
        <div style="display: flex; justify-content: center; margin-bottom: 1rem;">
            <svg width="100" height="100" viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="45" fill="url(#gradLogo)" stroke="#ff66b5" stroke-width="3"/>
                <defs><linearGradient id="gradLogo" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#ff99cc"/>
                    <stop offset="50%" stop-color="#ff66b5"/>
                    <stop offset="100%" stop-color="#ff3388"/>
                </linearGradient></defs>
                <text x="50" y="65" font-size="40" text-anchor="middle" fill="white" font-weight="bold">📘</text>
            </svg>
        </div>
    """, unsafe_allow_html=True)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    set_colorful_style()
    st.title("🔐 Access Required")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        show_logo()
        st.markdown("<h2 style='text-align: center;'>Let's Learn English With Gesner</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #ff66b5;'>Preschoolers Book – Lessons 1 to 20</p>", unsafe_allow_html=True)
        password_input = st.text_input("Enter password to access", type="password")
        if st.button("Login"):
            if password_input == "20082010":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect password. Access denied.")
    st.stop()

set_colorful_style()
st.markdown("""
<div class="main-header">
    <h1>📘 Let's Learn English With Gesner</h1>
    <p>Preschoolers Book – 20 fun lessons | Songs | Colors | Numbers | Ordinals</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    show_logo()
    st.markdown("## 🎯 Select a lesson")
    lesson_number = st.selectbox("Lesson", list(range(1, 21)), index=0)
    st.markdown("---")
    st.markdown("### 📚 Your progress")
    st.progress(lesson_number / 20)
    st.markdown(f"✅ Lesson {lesson_number} of 20 completed")
    st.markdown("---")
    st.markdown("**Founder & Developer:**")
    st.markdown("Gesner Deslandes")
    st.markdown("📞 WhatsApp: (509) 4738-5663")
    st.markdown("📧 Email: deslandes78@gmail.com")
    st.markdown("🌐 [Main website](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
    st.markdown("---")
    st.markdown("### 💰 Price")
    st.markdown("**$299 USD** (full book – 20 lessons, source code included)")
    st.markdown("---")
    st.markdown("### © 2025 GlobalInternet.py")
    st.markdown("All rights reserved")
    st.markdown("---")
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.authenticated = False
        st.rerun()

# ---------- Generate lesson content ----------
# Song themes for 20 lessons (each lesson gets 5 unique songs)
song_themes = [
    ["Hello Song", "Good Morning", "Let's Play", "Clap Your Hands", "Happy Day"],
    ["Animal Friends", "Old MacDonald", "Five Little Ducks", "Bingo", "Itsy Bitsy Spider"],
    ["Colors of the Rainbow", "Red and Yellow", "Blue and Green", "Purple Song", "Brown Bear"],
    ["Numbers Song", "One Two Three", "Count to Ten", "Five Little Monkeys", "Ten in the Bed"],
    ["Alphabet Song", "ABC", "Letter A", "Letter B", "Letter C"],
    ["Weather Song", "Sunny Day", "Rainy Day", "Cloudy Sky", "Windy Weather"],
    ["Family Song", "Mommy and Daddy", "Brother and Sister", "Grandma and Grandpa", "I Love My Family"],
    ["Shape Song", "Circle", "Square", "Triangle", "Rectangle"],
    ["Transport Song", "Wheels on the Bus", "Train Song", "Airplane", "Car Song"],
    ["Food Song", "Apple Banana", "Pizza Time", "Ice Cream", "Yummy Yummy"],
    ["Action Song", "Jump and Run", "Hop and Skip", "Dance and Spin", "Stomp Your Feet"],
    ["Feelings Song", "Happy and Sad", "Angry and Calm", "Excited and Tired", "I Feel Good"],
    ["Days of the Week", "Monday Monday", "Tuesday Tuesday", "Wednesday", "Weekend Song"],
    ["Months of the Year", "January", "February", "March", "April Song"],
    ["Season Song", "Spring is Here", "Summer Sun", "Autumn Leaves", "Winter Snow"],
    ["Opposites Song", "Big and Small", "Fast and Slow", "Hot and Cold", "Up and Down"],
    ["Job Song", "Doctor", "Teacher", "Firefighter", "Police Officer"],
    ["Place Song", "School", "Park", "Zoo", "Beach"],
    ["Bedtime Song", "Twinkle Twinkle", "Rock-a-bye Baby", "Goodnight", "Sweet Dreams"],
    ["Celebration Song", "Happy Birthday", "Party Time", "Dance Together", "We Are Friends"]
]

# Colors (10 basic)
colors = [
    {"name": "Red", "hex": "#FF0000"},
    {"name": "Blue", "hex": "#0000FF"},
    {"name": "Green", "hex": "#00FF00"},
    {"name": "Yellow", "hex": "#FFFF00"},
    {"name": "Orange", "hex": "#FFA500"},
    {"name": "Purple", "hex": "#800080"},
    {"name": "Pink", "hex": "#FFC0CB"},
    {"name": "Brown", "hex": "#A52A2A"},
    {"name": "Black", "hex": "#000000"},
    {"name": "White", "hex": "#FFFFFF"}
]

# Cardinal numbers 1-10
cardinal_numbers = [
    (1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five"),
    (6, "six"), (7, "seven"), (8, "eight"), (9, "nine"), (10, "ten")
]

# Ordinal numbers 1st-10th
ordinal_numbers = [
    (1, "first"), (2, "second"), (3, "third"), (4, "fourth"), (5, "fifth"),
    (6, "sixth"), (7, "seventh"), (8, "eighth"), (9, "ninth"), (10, "tenth")
]

def get_lesson_data(lesson_num):
    songs = []
    themes = song_themes[lesson_num - 1]
    for i, theme in enumerate(themes, 1):
        songs.append({
            "title": f"Song {i}: {theme}",
            "lyrics": f"Let's sing {theme} together! {theme} is fun, {theme} is great. La la la, sing along!"
        })
    return {
        "songs": songs,
        "colors": colors,
        "cardinal_numbers": cardinal_numbers,
        "ordinal_numbers": ordinal_numbers
    }

lesson_data = get_lesson_data(lesson_number)
st.markdown(f"## 📖 Lesson {lesson_number}: Fun with Songs, Colors, and Numbers!")

tab1, tab2, tab3 = st.tabs(["🎵 Let's Sing!", "🎨 Colors", "🔢 Numbers"])

# Audio function
def generate_audio(text, output_path):
    cmd = ["edge-tts", "--voice", "en-US-JennyNeural", "--text", text, "--write-media", output_path]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=30)
    except Exception as e:
        st.error(f"Audio error: {e}")

def play_audio(text, key):
    if st.button(f"🔊", key=key):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            generate_audio(text, tmp.name)
            with open(tmp.name, "rb") as f:
                audio_bytes = f.read()
                b64 = base64.b64encode(audio_bytes).decode()
                st.markdown(f'<audio controls src="data:audio/mp3;base64,{b64}" autoplay style="width: 100%;"></audio>', unsafe_allow_html=True)
            os.unlink(tmp.name)

# Tab 1: Songs
with tab1:
    st.subheader("🎵 Sing Along!")
    st.markdown("Click the 🔊 button to hear the song. Sing with me!")
    for i, song in enumerate(lesson_data["songs"], 1):
        st.markdown(f"**{song['title']}**")
        st.markdown(f"*{song['lyrics']}*")
        play_audio(song['lyrics'], f"song_{lesson_number}_{i}")
        st.markdown("---")

# Tab 2: Colors
with tab2:
    st.subheader("🎨 Learn Colors")
    st.markdown("Look at the color, read the name, and click 🔊 to hear it.")
    cols = st.columns(2)
    for idx, color in enumerate(lesson_data["colors"]):
        with cols[idx % 2]:
            st.markdown(f'<div><span class="color-box" style="background-color: {color["hex"]};"></span> <strong>{color["name"]}</strong></div>', unsafe_allow_html=True)
            play_audio(color["name"], f"color_{lesson_number}_{idx}")
    st.markdown("---")
    st.info("Can you find something red in your room? Try to say the color name!")

# Tab 3: Numbers (Cardinal and Ordinal)
with tab3:
    st.subheader("🔢 Cardinal Numbers (1 to 10)")
    st.markdown("Learn to count from one to ten.")
    cols = st.columns(5)
    for idx, (num, word) in enumerate(lesson_data["cardinal_numbers"]):
        with cols[idx % 5]:
            st.markdown(f"**{num}** – {word}")
            play_audio(f"{num} {word}", f"card_{lesson_number}_{idx}")
    st.markdown("---")
    st.subheader("🔢 Ordinal Numbers (1st to 10th)")
    st.markdown("Learn the order: first, second, third...")
    cols = st.columns(5)
    for idx, (num, word) in enumerate(lesson_data["ordinal_numbers"]):
        with cols[idx % 5]:
            st.markdown(f"**{num}** – {word}")
            play_audio(f"{num} {word}", f"ord_{lesson_number}_{idx}")
    st.markdown("---")
    st.success("Great job! Practice counting your toys and telling their order!")

if lesson_number == 20:
    st.markdown("---")
    st.markdown("## 🎓 Congratulations! You have completed the Preschoolers Book.")
    st.markdown("""
    ### 📞 To continue with Book 2, contact us:
    - **Gesner Deslandes** – Founder
    - 📱 WhatsApp: (509) 4738-5663
    - 📧 Email: deslandes78@gmail.com
    - 🌐 [GlobalInternet.py](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)
    
    Book 2 will contain more advanced topics: phonics, simple words, and short sentences.
    """)

st.markdown("---")
st.caption("📘 Let's Learn English With Gesner – Preschoolers Book. Sing, learn colors, and count with fun!")
