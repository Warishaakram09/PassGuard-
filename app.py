import streamlit as st
import re
import random
import string
import time
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.let_it_rain import rain

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make it at least 8 characters long.")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one digit.")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Use at least one special character (!@#$%^&*).")
    
    return score, feedback

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

st.set_page_config(page_title="🔐 Ultimate Password Strength Meter", page_icon="🔒", layout="centered")
st.markdown("""
    <style>
        .password-box {
            background-color: #621a79;
            padding: 20px;
            border-radius: 12px;
            color: white;
            font-weight: bold;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #621a79;'>🔒 Secure Password Strength Meter </h1>", unsafe_allow_html=True)

with stylable_container(key="password_input", css_styles="border: 2px solid #621a79; padding: 10px; border-radius: 10px; background-color: #f5f5f5;"):
    password = st.text_input("🔑 Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)
    
    strength_levels = {1: "Weak 😞", 2: "Weak 😞", 3: "Moderate 😐", 4: "Moderate 🙂", 5: "Strong 💪"}
    strength_color = {1: "#ff4d4d", 2: "#ff4d4d", 3: "#ffcc00", 4: "#66cc66", 5: "#00b300"}
    
    with stylable_container(key="strength_box", css_styles=f"border: 2px solid {strength_color[score]}; padding: 15px; border-radius: 10px; background-color: {strength_color[score]+'33'};"):
        st.markdown(f"<h3 style='text-align: center; color: {strength_color[score]};'>Strength: {strength_levels[score]}</h3>", unsafe_allow_html=True)
    
    if score < 5:
        st.warning("Improve your password:")
        for tip in feedback:
            st.write(f"- {tip}")
    else:
        st.success("✅ Your password is strong!")
        rain(emoji="💜", font_size=30, falling_speed=5, animation_length="infinite")
        
    
if st.button("✨ Generate Strong Password ✨"):
    with stylable_container(key="generated_password", css_styles="border: 2px dashed #838fd2; padding: 10px; border-radius: 10px; background-color: #e6e6fa; text-align: center;"):
        st.text(f"Suggested Password: {generate_strong_password()}")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #621a79;'>💜 Developed by Warisha Akram 💜</p>", unsafe_allow_html=True)
