import streamlit as st

# Initialize session state
if "chat_messages" not in st.session_state:
    st.session_state["chat_messages"] = []  # To store chat messages
if "selected_messages" not in st.session_state:
    st.session_state["selected_messages"] = set()  # To track selected messages

# Function to handle message selection toggle
def toggle_message(message):
    if message in st.session_state["selected_messages"]:
        st.session_state["selected_messages"].remove(message)
    else:
        st.session_state["selected_messages"].add(message)


st.write("### Chat Messages")
for i, msg in enumerate(st.session_state["chat_messages"]):
    is_selected = msg in st.session_state["selected_messages"]
    button_style = "color: white; background-color: green;" if is_selected else ""
    # if st.button(msg, key=f"msg_{i}", on_click=toggle_message, args=(msg,), help="Click to select/deselect"):
    #     pass  # Button already handles action via callback
    if st.button(msg, key=f"msg_{i}", help="Click to select/deselect"):
        # pass  # Button already handles action via callback
        toggle_message(msg)
        st.rerun()

# Input box for user to enter chat messages
user_message = st.text_input("Enter your message", key="input_message")

if st.button("Send"):
    if user_message.strip():
        st.session_state["chat_messages"].append(user_message.strip())
        st.rerun()
        # st.session_state["input_message"] = ""  # Clear the input


st.write("### Selected Messages")
if st.session_state["selected_messages"]:
    st.write(", ".join(st.session_state["selected_messages"]))
else:
    st.write("No messages selected.")

