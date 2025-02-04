import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie
import time
from pathlib import Path

# Page config
st.set_page_config(
    page_title="Fabries 30!",
    page_icon="🧗‍♂️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap');

.big-font {
    font-family: 'Permanent Marker', cursive;
    font-size: 4rem !important;
    color: #FF6B6B;
    text-shadow: 3px 3px 0px #000000;
    animation: shake 0.5s infinite;
}

.birthday-text {
    font-family: 'Permanent Marker', cursive;
    font-size: 2rem !important;
    color: #4ECDC4;
    text-shadow: 2px 2px 0px #000000;
}

@keyframes shake {
    0% { transform: translate(1px, 1px) rotate(0deg); }
    10% { transform: translate(-1px, -2px) rotate(-1deg); }
    20% { transform: translate(-3px, 0px) rotate(1deg); }
    30% { transform: translate(3px, 2px) rotate(0deg); }
    40% { transform: translate(1px, -1px) rotate(1deg); }
    50% { transform: translate(-1px, 2px) rotate(-1deg); }
    60% { transform: translate(-3px, 1px) rotate(0deg); }
    70% { transform: translate(3px, 1px) rotate(-1deg); }
    80% { transform: translate(-1px, -1px) rotate(1deg); }
    90% { transform: translate(1px, 2px) rotate(0deg); }
    100% { transform: translate(1px, -2px) rotate(-1deg); }
}

.stApp {
    background: linear-gradient(45deg, #1A1A1A, #2C3E50);
}

.gift-box {
    background-color: #FF6B6B;
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(255, 107, 107, 0.5);
    margin: 2rem 0;
    transform: rotate(-2deg);
}

.countdown {
    font-family: 'Permanent Marker', cursive;
    font-size: 3rem !important;
    color: #FFE66D;
    text-shadow: 2px 2px 0px #000000;
}
</style>
""", unsafe_allow_html=True)

# Load and display climbing animation
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None

# Load climbing animation
climbing_animation = load_lottieurl("https://lottie.host/86b57bb5-ab1c-4c0c-a1d7-02ef47c3a783/UkFEwbJ0Yl.json")

# Header
st.markdown('<p class="big-font">FABRIES WORDT 30! 🎉</p>', unsafe_allow_html=True)

# Two columns layout
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<p class="birthday-text">Guess what... Je krijgt een EPIC cadeau! 🎁</p>', unsafe_allow_html=True)
    if climbing_animation:
        st_lottie(climbing_animation, height=300, key="climbing")
    else:
        st.markdown("### 🧗‍♂️ Time to climb!")

with col2:
    # Load and display images
    images = Path(".").glob("*.png")
    for img_path in images:
        img = Image.open(img_path)
        st.image(img, use_column_width=True, caption="Fabries in action!")

# Gift reveal section
st.markdown("""
<div class="gift-box">
    <h2 style="color: white; text-align: center;">🎊 JOUW EPIC CADEAU 🎊</h2>
    <h3 style="color: white; text-align: center;">Een BOULDERBON om je inner climber los te laten! 🧗‍♂️</h3>
    <p style="color: white; text-align: center; font-size: 1.2rem;">
        Want wat is er beter dan je 30ste te vieren met een nieuwe uitdaging?<br>
        Time to crush some problems! 💪
    </p>
</div>
""", unsafe_allow_html=True)

# Countdown timer
def get_countdown():
    target_date = "2025-02-04"  # Set your target date here
    current_date = time.strftime("%Y-%m-%d")
    if current_date >= target_date:
        return "🎉 HAPPY BIRTHDAY! 🎉"
    else:
        # Add countdown logic here if needed
        return "The countdown is ON!"

st.markdown(f'<p class="countdown">{get_countdown()}</p>', unsafe_allow_html=True)

# Footer with some fun facts
st.markdown("""
---
### Did you know? 🤔
* Bouldering originated in the late 1800s
* The hardest boulder problems in the world are graded V17
* Bouldering is excellent for both physical and mental strength
* It's never too late to start climbing! 🧗‍♂️
""")

# Easter egg - click counter
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0

if st.button("🎁 Click me for a surprise!", key="surprise_button"):
    st.session_state.clicks += 1
    if st.session_state.clicks >= 5:
        st.balloons()
        st.markdown("### 🎉 SURPRISE! Keep crushing it, Fabries! 🧗‍♂️")
