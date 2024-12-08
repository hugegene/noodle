import streamlit as st
import random
import time
from sticky import st_fixed_container

# Streamed response emulator
# def response_generator():
#     response = random.choice(
#         [
#             "Hello there! How can I assist you today?",
#             "Hi, human! Is there anything I can help you with?",
#             "Do you need help?",
#         ]
#     )
#     for word in response.split():
#         yield word + " "
#         time.sleep(0.05)

from streamlit_float import *

# initialize float feature/capability
float_init()

# col1, col2 = st.columns(2)

# # Fix/float the whole column
# col1.write("This entire column is fixed/floating")
# col1.float()

# with col2:
# container = st.container()
# # Fix/float a single container inside
# container.write("This text is in a container that is fixed")
# container.float()


with st.container():
    st.button("This is inside the container")

    # You can call any Streamlit command, including custom components:
    
    float_parent()



# with st_fixed_container(mode="fixed", position="top", border=True):
#     st.button("This is a fixed container.")
    # st.markdown(
    #     f"<div class='fixed-container-{key}'></div>",
    #     unsafe_allow_html=True,
    # )

# header = st.container()
# header.title("Here is a sticky header")
# header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)

# ### Custom CSS for the sticky header
# st.markdown(
#     """
# <style>
#     div[data-testid="stVerticalBlock"] div:has(div.fixed-header) {
#         position: sticky;
#         top: 2.875rem;
#         background-color: white;
#         z-index: 999;
#     }
#     .fixed-header {
#         border-bottom: 1px solid black;
#     }
# </style>
#     """,
#     unsafe_allow_html=True
# )
# st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


option_map = {
    0: ":material/add:",
    1: ":material/zoom_in:",
    2: ":material/zoom_out:",
    3: ":material/zoom_out_map:",
}


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if st.checkbox(message["content"]):
            selection = st.segmented_control(
                "Tool",
                options=option_map.keys(),
                format_func=lambda option: option_map[option],
                selection_mode="single",
            )


# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.checkbox(prompt)

    # Display assistant response in chat message container
    # with st.chat_message("assistant"):
    #     response = st.write_stream(response_generator())
    # # Add assistant response to chat history
    # st.session_state.messages.append({"role": "assistant", "content": response})
