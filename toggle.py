import streamlit as st

# Initialize session state for selections
if "selected_messages" not in st.session_state:
    st.session_state.selected_messages = []

# Define chat messages
chat_messages = [
    {"role": "user", "content": "Hi there!"},
    {"role": "assistant", "content": "Hello! How can I help you?"},
    {"role": "user", "content": "Can you tell me about Streamlit?"},
    {"role": "assistant", "content": "Sure! Streamlit is an open-source Python library for building web apps."},
]

# Function to toggle message selection
def toggle_selection(index):
    if index in st.session_state.selected_messages:
        st.session_state.selected_messages.remove(index)
    else:
        st.session_state.selected_messages.append(index)

# Display chat messages
for idx, message in enumerate(chat_messages):
    is_selected = idx in st.session_state.selected_messages
    background_color = "#e6f7ff" if is_selected else "#ffffff"  # Highlight selected messages
    
    # Use a clickable container for each message
    with st.container():
        # Make the entire container clickable using `on_click` behavior
        st.button(
            f"""
            <div style="padding: 10px; background-color: {background_color}; border-radius: 5px; margin-bottom: 5px; cursor: pointer;">
                <b>{message['role'].capitalize()}:</b> {message['content']}
            </div>
            """,
            # unsafe_allow_html=True,
            key=f"message_{idx}",
            on_click=toggle_selection
        )
        # st.markdown(
        #     f"""
        #     <div style="padding: 10px; background-color: {background_color}; border-radius: 5px; margin-bottom: 5px; cursor: pointer;">
        #         <b>{message['role'].capitalize()}:</b> {message['content']}
        #     </div>
        #     """,
        #     unsafe_allow_html=True,
        #     # key=f"message_{idx}"
        # )
        # Add a hidden checkbox to detect clicks
        # if st.button("", key=f"toggle_{idx}", on_click=toggle_selection, args=(idx,)):
        #     pass

# Show selected messages
st.write("Selected Messages:")
for idx in st.session_state.selected_messages:
    st.write(chat_messages[idx]["content"])
