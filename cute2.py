import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="A story about the girl i adore ❤️", page_icon="💖", layout="centered")

# --- INITIALIZE SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 0

def next_step():
    st.session_state.step += 1

# --- GET CURRENT DIRECTORY ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- CSS: THEME & BACKGROUND EFFECTS ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffdde1 0%, #ee9ca7 100%);
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    /* Fade-in animation for new steps */
    .fade-in {
        animation: fadeIn 1.5s;
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    h1 {
        color: #c9184a !important;
        font-family: 'Dancing Script', cursive;
        font-size: 3.5rem !important;
        text-align: center;
    }
    .message-box {
        text-align: center;
        color: #800f2f;
        font-size: 1.5rem;
        background: rgba(255, 255, 255, 0.3);
        padding: 20px;
        border-radius: 20px;
        margin: 20px 0;
    }
    
    /* Floating background hearts */
    .bg-heart {
        color: rgba(201, 24, 74, 0.3); 
        font-size: 20px;
        position: fixed;
        top: -10%;
        z-index: 0; 
        animation: heartFloat 8s linear infinite;
    }
    @keyframes heartFloat {
        0% { transform: translateY(0) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
    
    <div class="bg-heart" style="left:10%; animation-delay:0s;">❤️</div>
    <div class="bg-heart" style="left:40%; animation-delay:2s;">💖</div>
    <div class="bg-heart" style="left:80%; animation-delay:1s;">💕</div>
    """, unsafe_allow_html=True)

# Background Music Player
music_path = os.path.join(BASE_DIR, "adele_song.mp3")
st.audio(music_path, format="audio/mpeg", loop=True, autoplay=True)

# --- THE JOURNEY LOGIC ---

# STEP 0: THE START
if st.session_state.step == 0:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.markdown("<h1>Hey Nahed... ❤️</h1>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>I made somthing special as a sorry its a little story. Are you ready to see it?</div>", unsafe_allow_html=True)
    st.button("Yes, I'm Ready! 🥰", on_click=lambda: setattr(st.session_state, 'step', 2))
    st.button("No, I'm Not Ready! ", on_click=next_step)
    st.markdown("</div>", unsafe_allow_html=True)

# STEP 1: warning
elif st.session_state.step == 1:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>Stop being idiotic and go back 😡 </div>", unsafe_allow_html=True)
    st.button("go back✨", on_click=lambda: setattr(st.session_state, 'step', 0) or st.rerun())
    st.markdown("</div>", unsafe_allow_html=True)

# STEP 2: FIRST PHOTO
elif st.session_state.step == 2:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.image(os.path.join(BASE_DIR, "PIC1.jpg"), use_container_width=True)
    st.markdown("<div class='message-box'>this beautiful girl sudnly appeared in my life and changed everything like literally everything she is my world</div>", unsafe_allow_html=True)
    st.button("Continue... ❤️", on_click=next_step)
    st.markdown("</div>", unsafe_allow_html=True)

# STEP 3: SECOND PHOTO
elif st.session_state.step == 3:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.image(os.path.join(BASE_DIR, "PIC2.jpg"), use_container_width=True)
    st.markdown("<div class='message-box'>this beautiful girl means the world to me</div>", unsafe_allow_html=True)
    st.button("Continue... ❤️", on_click=next_step)
    st.markdown("</div>", unsafe_allow_html=True)

# STEP 4: THIRD PHOTO
elif st.session_state.step == 4:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.image(os.path.join(BASE_DIR, "PIC3.jpg"), use_container_width=True)
    st.markdown("<div class='message-box'>you know why ?</div>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>actualy i don't know why but i can tell that this girl is special it'snot like any other girl in the world she's different </div>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>she is the most beautiful girl i have ever seen i adore every small detail about her</div>", unsafe_allow_html=True)
    st.button("Continue... ❤️", on_click=next_step)
    st.markdown("</div>", unsafe_allow_html=True)

# STEP 5: FOURTH PHOTO
elif st.session_state.step == 5:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.image(os.path.join(BASE_DIR, "PIC4.jpg"), use_container_width=True)
    st.markdown("<div class='message-box'>i was so lost, sad and stressed</div>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>but when she appeared she found me she wake something inside me i don't know it even exists</div>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>she was like an angel she always made me smile without doing anything</div>", unsafe_allow_html=True)
    st.button("Continue... ❤️", on_click=next_step)
    st.markdown("</div>", unsafe_allow_html=True)

# STEP 6: FIFTH PHOTO
elif st.session_state.step == 6:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.image(os.path.join(BASE_DIR, "PIC5.jpg"), use_container_width=True)
    st.markdown("<div class='message-box'>ohhh sh!t how do i forgot the most important thing</div>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>her EYESSSSSSS!!!!! </div>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>how can i describe the beauty of this almond hazel beautiful eyes</div>", unsafe_allow_html=True)
    st.button("Continue... ❤️", on_click=next_step)
    st.markdown("</div>", unsafe_allow_html=True)

# STEP 7: SIXTH PHOTO
elif st.session_state.step == 7:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.image(os.path.join(BASE_DIR, "PIC6.jpg"), use_container_width=True)
    st.markdown("<div class='message-box'>ohh!</div>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>her she is Winning </div>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>she is soo beautiful and i'm soo proud of her, im greatful for having her in my life</div>", unsafe_allow_html=True)
    st.button("Continue... ❤️", on_click=next_step)
    st.markdown("</div>", unsafe_allow_html=True)


# STEP 8: SEVENTH PHOTO
elif st.session_state.step == 8:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.image(os.path.join(BASE_DIR, "PIC7.jpg"), use_container_width=True)
    st.image(os.path.join(BASE_DIR, "PIC8.jpg"), use_container_width=True)
    st.markdown("<div class='message-box'>this is us</div>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>this is what i will never risk losing it your smile, your laugh, your love</div>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>you desirve the whole world in between your hands</div>", unsafe_allow_html=True)
    st.button("Continue... ❤️", on_click=next_step)
    st.markdown("</div>", unsafe_allow_html=True)

# STEP 9: THE FINAL MESSAGE
elif st.session_state.step == 9:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.markdown("<h1>I Love You to the Moon and Back ❤️</h1>", unsafe_allow_html=True)
    st.write(""" last thing i want to say that 
        I am sorry for what i did to you, but I swear i wasn't mean it to hurt you, i just wanted to make you happy and i know that i failed but i will never stop trying to make you happy because your happiness is my happiness. 
        I want to make all your wishes come true because you deserve the world.
    """)
    if st.button("Click for the ultimate Surprise! 🎁"):
    # Show your video (replace "surprise.mp4" with your actual video filename or URL)
        st.video(os.path.join(BASE_DIR, "surprise.mp4"))
    
    # Optional: Keep the heart burst animation if you still want it
    st.markdown("""
        <script>
            // your javascript heart code here...
        </script>
    """, unsafe_allow_html=True)
    
    if st.button("Restart Journey 🔄"):
        st.session_state.step = 0
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)