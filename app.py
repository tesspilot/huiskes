import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie
import time
from pathlib import Path
from streamlit_extras.let_it_rain import rain
from streamlit_particles import particles
import json

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

@keyframes climb {
    0% { transform: translate(0, 100vh) rotate(0deg); }
    25% { transform: translate(20px, 75vh) rotate(5deg); }
    50% { transform: translate(-20px, 50vh) rotate(-5deg); }
    75% { transform: translate(20px, 25vh) rotate(5deg); }
    100% { transform: translate(0, 0) rotate(0deg); }
}

.climbing-image {
    animation: climb 10s infinite alternate ease-in-out;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(255, 107, 107, 0.5);
    cursor: pointer;
}

.climbing-image-delayed {
    animation: climb 12s infinite alternate-reverse ease-in-out;
    animation-delay: 1s;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(78, 205, 196, 0.5);
    cursor: pointer;
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
    cursor: pointer;
}

.drink-box {
    background-color: #4ECDC4;
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(78, 205, 196, 0.5);
    margin: 2rem 0;
    transform: rotate(2deg);
    cursor: pointer;
}

.countdown {
    font-family: 'Permanent Marker', cursive;
    font-size: 3rem !important;
    color: #FFE66D;
    text-shadow: 2px 2px 0px #000000;
}

@keyframes explode {
    0% { transform: scale(0); opacity: 0; }
    50% { transform: scale(1.2); opacity: 1; }
    100% { transform: scale(1); opacity: 1; }
}

.explosion {
    animation: explode 0.5s ease-out;
}

div[data-testid="stImage"] {
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# Particle effect configuration
particles_config = {
    "particles": {
        "number": {
            "value": 30,
            "density": {
                "enable": True,
                "value_area": 800
            }
        },
        "color": {
            "value": ["#FF6B6B", "#4ECDC4", "#FFE66D"]
        },
        "shape": {
            "type": ["circle", "star", "triangle"]
        },
        "size": {
            "value": 6,
            "random": True
        },
        "move": {
            "enable": True,
            "speed": 3,
            "direction": "none",
            "random": True,
            "straight": False,
            "out_mode": "out",
            "bounce": False,
        }
    }
}

# Add particle effect
particles(particles_config, height="20rem")

# Load climbing animations
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None

# Load multiple climbing animations
climbing_animations = [
    load_lottieurl("https://lottie.host/86b57bb5-ab1c-4c0c-a1d7-02ef47c3a783/UkFEwbJ0Yl.json"),
    load_lottieurl("https://lottie.host/2d2960c0-2c1f-49c3-9962-93839ddd3dc1/HxqGQIrhWE.json"),
    load_lottieurl("https://lottie.host/ad5d326c-4f4e-4fce-9f6d-7d2d56a43c67/h4UOBMGTYt.json")
]

# Header with rain effect
rain(
    emoji="🧗‍♂️",
    font_size=54,
    falling_speed=5,
    animation_length="infinite",
)

st.markdown('<p class="big-font">FABRIES WORDT 30! 🎉</p>', unsafe_allow_html=True)

# Initialize session state for click effects
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
if 'explosions' not in st.session_state:
    st.session_state.explosions = []

# Two columns layout
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<p class="birthday-text">Guess what... Je krijgt een EPIC cadeau! 🎁</p>', unsafe_allow_html=True)
    
    # Display random climbing animations
    for anim in climbing_animations:
        if anim:
            st_lottie(anim, height=200, key=f"climbing_{climbing_animations.index(anim)}")

with col2:
    # Load and display images with labels
    images = list(Path(".").glob("*.png"))
    
    # First image (Fabries)
    if len(images) > 0:
        img = Image.open(images[0])
        st.markdown('<div class="climbing-image">', unsafe_allow_html=True)
        if st.image(img, use_column_width=True, caption="Fabries in action! 🧗‍♂️"):
            st.balloons()
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Second image (Dick)
    if len(images) > 1:
        img = Image.open(images[1])
        st.markdown('<div class="climbing-image-delayed">', unsafe_allow_html=True)
        if st.image(img, use_column_width=True, caption="Dick presenting the epic gift! 🎁"):
            st.snow()
        st.markdown('</div>', unsafe_allow_html=True)

# Gift reveal section with click effect
gift_container = st.container()
with gift_container:
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
    if st.button("🎁 KLIK HIER!", key="gift_button"):
        st.balloons()
        rain(
            emoji="💥",
            font_size=54,
            falling_speed=5,
            animation_length=1,
        )

# Drink bonus section with click effect
drink_container = st.container()
with drink_container:
    st.markdown("""
    <div class="drink-box">
        <h2 style="color: white; text-align: center;">🍺 BONUS SURPRISE! 🍺</h2>
        <h3 style="color: white; text-align: center;">Een drankje naar keuze bij het boulderen!</h3>
        <p style="color: white; text-align: center; font-size: 1.2rem;">
            Want na het klimmen moet er natuurlijk wel wat te drinken zijn...<br>
            Kies maar uit: 🍺 Biertje / 🧃 Smoothie / ☕️ Koffie / 🥤 Fris
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🍺 KIES JE DRANKJE!", key="drink_button"):
        st.snow()
        rain(
            emoji="🍺",
            font_size=54,
            falling_speed=5,
            animation_length=1,
        )

# Surprise button with multiple effects
if st.button("💥 SUPER SURPRISE! 💥", key="surprise_button"):
    st.balloons()
    st.snow()
    rain(
        emoji="🎉",
        font_size=54,
        falling_speed=5,
        animation_length=1,
    )
    st.markdown("""
    <div class="explosion">
        <h1 style="text-align: center; color: #FFE66D; font-size: 4rem; text-shadow: 2px 2px 0px #000000;">
            💥 BOOOM! 💥
        </h1>
        <h2 style="text-align: center; color: #FF6B6B;">
            Happy 30th Birthday Fabries! 🎉
        </h2>
    </div>
    """, unsafe_allow_html=True)

# Footer with climbing facts
st.markdown("""
---
### Boulder Facts! 🤔
* Bouldering originated in the late 1800s
* The hardest boulder problems in the world are graded V17
* Bouldering is excellent for both physical and mental strength
* Nu je 30 bent, ben je in je prime climbing jaren! 💪
""")

# Add final particle effect
particles(particles_config, height="20rem")
