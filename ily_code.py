import streamlit as st

# --- App Configuration (Sets the browser tab title and icon) ---
st.set_page_config(page_title="For You", page_icon="💖")

# --- Data: Define your keywords and the content to show ---
# We use a dictionary to make it easy to manage.
keyword_links = {
    # The key is the button label (e.g., "Happy")
    "Happy": {
        "message": "So glad you're happy! Here's a happy tune:",
        "link": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"
    },
    "Sad": {
        "message": "It's okay to feel sad. Maybe this will help:",
        "link": "https://open.spotify.com/track/1e1o2zV2g2I0sAPZ21I6aD?si=411993202e77454b"
    },
    "I'm Sorry": {
        "message": "Here is a virtual hug for you:",
        "link": "https://i.pinimg.com/originals/e3/9d/2d/e39d2d322ad24a35f396263438a35f7c.gif"
    },
    "Eepy": {
        "message": "Time for a nap! Here are some relaxing sounds:",
        "link": "https://www.youtube.com/watch?v=rUxyKA_-grg"
    },
    "IMY": {
        "message": "Thinking of you too! Here's a song for that feeling:",
        "link": "https://open.spotify.com/track/4uSfw3Lu390bB5g9I3K4A5?si=5a285d85d7b545a1"
    }
}

# --- App Layout (What the user sees on the page) ---

# 1. A main title for the app
st.title("A Little Something For You")
st.write("How are you feeling today? Click a button below.")

# 2. Create columns to arrange the buttons neatly side-by-side
#    This creates 5 columns of equal width.
col1, col2, col3, col4, col5 = st.columns(5)

# 3. Create the buttons and check if they are clicked.
#    We use a `with` block to place each button inside a column.
with col1:
    if st.button("Happy"):
        st.session_state.choice = "Happy" # Store the choice
with col2:
    if st.button("Sad"):
        st.session_state.choice = "Sad"
with col3:
    # Use a different label for the button for a cleaner look
    if st.button("Sorry?"): 
        st.session_state.choice = "I'm Sorry"
with col4:
    if st.button("Eepy"):
        st.session_state.choice = "Eepy"
with col5:
    if st.button("IMY"):
        st.session_state.choice = "IMY"
        
# 4. Display the result only AFTER a button has been clicked.
#    `st.session_state` is Streamlit's way of remembering variables.
if 'choice' in st.session_state:
    choice = st.session_state.choice
    result = keyword_links[choice]
    
    st.divider() # Adds a nice horizontal line for separation
    st.subheader(result["message"]) # Display the custom message
    st.write(f"[Click here to open!]({result['link']})") # Display the link
    
    # Bonus: If the link is a GIF or image, show it directly on the page!
    if result['link'].endswith(('.gif', '.png', '.jpg', '.jpeg')):
        st.image(result['link'])