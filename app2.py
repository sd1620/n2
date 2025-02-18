import streamlit as st
import time
from datetime import datetime
import turtle
import matplotlib.pyplot as plt
import numpy as np
import folium
from folium.plugins import MarkerCluster

# Anniversary Date
anniversary_date = datetime(2025, 3, 23)

# Streamlit App configuration
st.set_page_config(page_title="For My WIFEY ❤️", layout="wide")
st.title("💖 Happy 11-Month Anniversary, My Love! 💖")
st.subheader("A special Gift just for you, Abhipsa! 😘")

# Love Letter Section
st.markdown("### 💌 Some Lines Just For You, Pari💖")
st.markdown(
    """
    **My Love,**  
    Every day with you is a beautiful chapter in our love story.  
    From our laughs to our quiet moments, every second is precious.  
    I can't wait for a lifetime more with you.  
    **I love you endlessly! ❤️**  
    """
)

# Countdown Timer (Realistic Update)
st.markdown("### ⏳ Countdown to Our 1-Year Anniversary")

# Create an empty placeholder for the countdown
countdown_placeholder = st.empty()

# Function to update countdown
def update_countdown():
    today = datetime.now()
    time_remaining = anniversary_date - today

    # If the anniversary has passed
    if time_remaining.total_seconds() <= 0:
        countdown_placeholder.markdown(f"🎉 **Happy 1-Year Anniversary!** 🎉")
    else:
        # Extract days, hours, minutes, and seconds
        days_left = time_remaining.days
        hours_left, remainder = divmod(time_remaining.seconds, 3600)
        minutes_left, seconds_left = divmod(remainder, 60)

        countdown_str = f"⏳ **{days_left} days, {hours_left} hours, {minutes_left} minutes, {seconds_left} seconds** remaining until our 1st Anniversary on **March 23, 2025**!"
        countdown_placeholder.markdown(countdown_str)

# Display the countdown
update_countdown()

# Adding a small delay to simulate a countdown without manually triggering a rerun
time.sleep(1)

# Rest of your content below...
# Memories Section
st.markdown("### 📸 Our Beautiful Memories")
images = ["uss1.png", "uss2.jpg"]  # Replace with your images
cols = st.columns(len(images))
for i, img in enumerate(images):
    with cols[i]:
        st.image(img, caption=f"Dekh how beautiful we look with each other <3", use_container_width=True)

# Interactive Love Quiz
st.markdown("### 💕 How Well Do You Know Our Love Story?")
quiz_questions = {
    "Where did we first meet?": ["School", "Cafe", "Park", "Mall"],
    "What's my favorite dish you make?": ["Pasta(WhiteSauce)", "Maggi/Yippee", "Paneer", "Parathe"],
    "Our first movie together?": ["Shershaah", "12TH Fail", "Aashiqui2", "YJHD"],
}

score = 0
for question, options in quiz_questions.items():
    answer = st.radio(question, options)
    if answer == options[0]:  # Adjust correct answers
        score += 1

if st.button("Submit Quiz"):
    st.success(f"Your Score: {score}/{len(quiz_questions)}! 🥰 Love you!")

# Song Section
st.markdown("### 🎶 Our Special Song")
audio_file = "hey-shona.mp3"  # Replace with the path to your song file (e.g., mp3 or wav)
st.audio(audio_file, format="audio/mp3", start_time=0) 

st.markdown("### 🎶 The Song We Relate To ❤️")
audio_file = "thsd.mp3"  # Replace with the path to your song file (e.g., mp3 or wav)
st.audio(audio_file, format="audio/mp3", start_time=0)

# Map Section
pune_coords = [18.5204, 73.8567]  # Pune, Maharashtra
bhubaneswar_coords = [20.2961, 85.8189]  # Bhubaneswar, Odisha

# Create a map centered around the midpoint
map_center = [(pune_coords[0] + bhubaneswar_coords[0]) / 2,
              (pune_coords[1] + bhubaneswar_coords[1]) / 2]
m = folium.Map(location=map_center, zoom_start=5)

# Add a marker cluster
marker_cluster = MarkerCluster().add_to(m)

# Add markers for Pune and Bhubaneswar
folium.Marker(
    location=pune_coords,
    popup="Pune",
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(marker_cluster)

folium.Marker(
    location=bhubaneswar_coords,
    popup="Bhubaneswar",
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(marker_cluster)

# Add a line connecting Pune and Bhubaneswar
folium.PolyLine(
    locations=[pune_coords, bhubaneswar_coords],
    color='red',
    weight=2.5,
    opacity=1
).add_to(m)

# Save the map as an HTML file
map_path = "pune_bhubaneswar_map.html"
m.save(map_path)

# Display the map in Streamlit
st.title("Physical distance between us :- ")
st.write(f"AIR Distance :- 1,270 km.")
st.write(f"Road distance :- 1,623 km.")
st.components.v1.html(open(map_path, 'r').read(), width=700, height=500)
st.write("Distance between our hearts :- 0 km")

# Footer
st.markdown("---")
st.markdown("❤️ **By Your Husband <3, just for you!** ❤️")
st.markdown("I love u so much Abhipsa❤️")
st.markdown(
    """
    Manuche,
    Bahut bhul kare mu
    Ragejae
    But, tate jeban thu baleke bhala pae ❤️
    Manuche bhul kare but buleke to pakhaku hi asebe na
    Kie hi achi to chada ❤️
    Mo jeban ta tu ❤️
    Sabubele khusi re tha dhana ❤️
    """
)
