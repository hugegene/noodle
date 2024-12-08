import streamlit as st

# CSS to define button colors and styles
st.markdown(
    """
    <style>
    .pressed-button {
        background-color: green !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# A button press changes this state variable
if "button_pressed" not in st.session_state:
    st.session_state["button_pressed"] = False

def toggle_button_state():
    st.session_state["button_pressed"] = not st.session_state["button_pressed"]

# Display a button with dynamic CSS classes
button_label = "Press Me"
button_class = "pressed-button" if st.session_state["button_pressed"] else ""

st.markdown(
    f'<button class="{button_class}" onclick="window.location.reload();">{button_label}</button>',
    unsafe_allow_html=True,
)

# Use an actual Streamlit button to toggle the state
if st.button("Toggle State"):
    toggle_button_state()
